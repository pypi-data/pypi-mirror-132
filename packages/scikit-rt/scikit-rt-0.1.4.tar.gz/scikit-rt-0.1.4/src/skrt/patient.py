"""Classes related to Patients and Studies."""

import os
import pydicom
import shutil
import time

import skrt.core
from skrt.image import Image
from skrt.structures import StructureSet


class Study(skrt.core.Archive):
    def __init__(self, path=""):

        skrt.core.Archive.__init__(self, path, allow_dirs=True)

        special_dirs = ["RTPLAN", "RTSTRUCT", "RTDOSE"]
        self.image_types = []
        for file in self.files:

            subdir = os.path.basename(file.path)
            if subdir in special_dirs:
                continue
            self.image_types.append(subdir)

            # Get images
            im_name = f"{subdir.lower()}_images"
            setattr(
                self,
                im_name,
                self.get_dated_objects(dtype=Image, subdir=subdir, load=False),
            )

            # Assign the original subdir name to the images
            for im in getattr(self, im_name):
                im.image_type = subdir

            # Get associated structure sets
            struct_subdir = f"RTSTRUCT/{subdir}"
            if os.path.exists(os.path.join(self.path, struct_subdir)):
                setattr(
                    self,
                    f"{subdir.lower()}_structure_sets",
                    self.get_structure_sets(
                        subdir=struct_subdir, images=getattr(self, im_name)
                    ),
                )

        # Plans, dose etc: leave commented for now
        #  self.plans = self.get_plan_data(dtype='RtPlan', subdir='RTPLAN')
        #  self.doses = self.get_plan_data(
        #  dtype='RtDose',
        #  subdir='RTDOSE',
        #  exclude=['MVCT', 'CT'],
        #  images=self.ct_images    
        #  )

        # Load CT-specific RT doses
        #  self.ct_doses = self.get_plan_data(
        #  dtype='RtDose', subdir='RTDOSE/CT', images=self.ct_images    
        #  )
        #  self.ct_doses = self.correct_dose_image_position(self.ct_doses)

    def add_image(self, im, image_type="CT"):
        '''Add a new image of a given image type.'''

        # Ensure we have a list of this type of image
        im_name = f"{image_type.lower()}_images"
        if not hasattr(self, im_name):
            setattr(self, im_name, [])
        if image_type not in self.image_types:
            self.image_types.append(image_type)

        # Add image to the list
        images = getattr(self, im_name)
        if isinstance(im, Image):
            im_to_add = im
        else:
            im_to_add = Image(im)
        images.append(im)

        # Ensure image has a timestamp
        if not im.timestamp:
            im.timestamp = skrt.core.generate_timestamp()

        # Ensure corresponding structure list exists
        struct_subdir = f"RTSTRUCT/{image_type}"
        struct_name = f"{image_type.lower()}_structure_sets"
        if not hasattr(self, struct_name):
            setattr(self, struct_name, [])

        # Add the image's structure sets to structure set list
        structure_sets = getattr(self, struct_name)
        for structure_set in im.get_structure_sets():
            structure_sets.append(structure_set)
            if not structure_set.timestamp:
                structure_set.timestamp = skrt.core.generate_timestamp()

    def correct_dose_image_position(self, doses=[]):
        """Correct for image positions from CheckTomo being offset by one slice
        relative to image positions."""

        for dose in doses:
            dx, dy, dz = dose.voxel_size
            x0, y0, z0 = dose.image_position
            dose.image_position = (x0, y0, z0 + dz)
        return doses

    def get_machine_sublist(self, dtype="", machine="", ignore_case=True):
        """Get list of doses or treatment plans corresponding to a specific
        machine."""

        sublist = []
        if dtype.lower() in ["plan", "rtplan"]:
            objs = self.plans
        elif dtype.lower() in ["dose", "rtdose"]:
            objs = self.doses
        else:
            objs = []

        if ignore_case:
            for obj in objs:
                if objs.machine.lower() == machine.lower():
                    sublist.append(obj)
        else:
            for obj in objs:
                if objs.machine == machine:
                    sublist.append(object)
        return sublist

    def get_mvct_selection(self, mvct_dict={}, min_delta_hours=0.0):
        """Get a selection of MVCT images which were taken at least
        <min_delta_hours> apart. <mvct_dict> is a dict where the keys are
        patient IDs, and the paths are directory paths from which to load images
        for that patient."""

        # Find images meeting the time separation requirement
        if min_delta_hours > 0:
            mvct_images = get_time_separated_objects(self.mvct_images, min_delta_hours)
        else:
            mvct_images = self.mvct_images

        # Find images matching the directory requirement
        selected = []
        patient_id = self.get_patient_id()
        if patient_id in mvct_dict:

            # Get all valid directories for this patient
            valid_dirs = [skrt.core.fullpath(path) for path in mvct_dict[patient_id]]

            # Check for images matching that directory requirement
            for mvct in mvct_images:
                mvct_dir = os.path.dirname(mvct.files[-1].path)
                if skrt.core.fullpath(mvct_dir) in valid_dirs:
                    selected.append(mvct)

        # Otherwise, just return all images for this patient
        else:
            selection = mvct_images

        return selection

    def get_patient_id(self):
        patient_id = os.path.basename(os.path.dirname(self.path))
        return patient_id

    def get_plan_data(self, dtype="RtPlan", subdir="RTPLAN", exclude=[], images=[]):
        """Get list of RT dose or plan objects specified by dtype='RtDose' or
        'RtPlan' <dtype>, respectively) by searching within a given directory,
        <subdir> (or within the top level directory of this Study, if
        <subdir> is not provided).

        Subdirectories with names in <exclude> will be ignored.

        Each dose-like object will be matched by timestamp to one of the images
        in <images> (which should be a list of DatedStores), if provided."""

        doses = []

        # Get initial path to search
        if subdir:
            path1 = os.path.join(self.path, subdir)
        else:
            path1 = self.path

        # Look for subdirs up to two levels deep from initial dir
        subdirs = []
        if os.path.isdir(path1):

            # Search top level of dir
            path1_subdirs = os.listdir(path1)
            for item1 in path1_subdirs:

                if item1 in exclude:
                    continue
                path2 = os.path.join(path1, item1)
                n_sub_subdirs = 0

                # Search any directories in the top level dir
                if os.path.isdir(path2):
                    path2_subdirs = os.listdir(path2)
                    for item2 in path2_subdirs:
                        path3 = os.path.join(path2, item2)

                        # Search another level (subdir/item1/item2/*)
                        if os.path.isdir(path3):
                            n_sub_subdirs += 1
                            if subdir:
                                subdirs.append(os.path.join(subdir, item1, item2))
                            else:
                                subdirs.append(item1, item2)

                if not n_sub_subdirs:
                    if subdir:
                        subdirs = [os.path.join(subdir, item1)]
                    else:
                        subdirs = [item1]

                for subdir_item in subdirs:
                    doses.extend(
                        self.get_dated_objects(dtype=dtype, subdir=subdir_item)
                    )

        # Assign dose-specific properties
        if dtype == "RtDose":
            new_doses = []
            for dose in doses:

                # Search for images with matching timestamp
                timestamp = os.path.basename(os.path.dirname(dose.path))
                if images:
                    try:
                        dose.date, dose.time = timestamp.split("_")
                        image = get_dated_obj(images, dose)
                        dose.machine = image.machine
                    except BaseException:
                        image = images[-1]
                        dose.date = image.date
                        dose.time = image.time

                    dose.timestamp = f"{dose.date}_{dose.time}"
                    dose.image = image

                dose.couch_translation, dose.couch_rotation = get_couch_shift(dose.path)
                # WARNING!
                #     Couch translation third component (y) inverted with
                #     respect to CT image
                # WARNING!
                new_doses.append(dose)
            doses = new_doses

        doses.sort()
        return doses

    def get_plan_dose(self):

        plan_dose = None
        dose_dict = {}

        # Group doses by summation type
        for dose in self.doses:
            if dose.summationType not in dose_dict:
                dose_dict[dose.summationType] = []
            dose_dict[dose.summationType].append(dose)
        for st in dose_dict:
            dose_dict[st].sort()

        # 'PLAN' summation type: just take the newest entry
        if "PLAN" in dose_dict:
            plan_dose = dose_dict["PLAN"][-1]
            plan_dose.imageStack = plan_dose.getImageStack()

        else:

            # Get fraction froup and beam sequence
            if self.plans:
                n_frac_group = self.plans[-1].nFractionGroup
                n_beam_seq = self.plans[-1].nBeamSequence
            else:
                n_frac_group = None
                n_beam_seq = None

            # Sum over fractions
            if "FRACTION" in dose_dict:
                if len(dose_dict["FRACTION"]) == n_frac_group:

                    # Single fraction
                    if n_frac_group == 1:
                        plan_dose = dose_dict["FRACTION"][0]

                    # Sum fractions
                    else:
                        plan_dose = self.sum_dose_plans(dose_dict, "FRACTION")

            # Sum over beams
            elif "BEAM" in sum_type:
                if len(dose_dict["BEAM"]) == n_beam_seq:

                    # Single fraction
                    if n_frac_group == 1:
                        plan_dose = dose_dict["BEAM"][0]

                    # Sum beams
                    else:
                        plan_dose = self.sum_dose_plans(dose_dict, "BEAM")

        return plan_dose

    def get_structure_sets(self, subdir="", images=[]):
        """Make list of StructureSet objects found within a given subdir and
        set their associated image objects."""

        # Find structure set directories associated with each image
        groups = self.get_dated_objects(dtype=skrt.core.Archive, subdir=subdir)

        # Load structure set files for each
        structure_sets = []
        for group in groups:

            # Find the matching Image for this group
            image = None
            image_dir = os.path.basename(group.path)
            image_found = False

            # Try matching on path
            for im in images:
                if image_dir == os.path.basename(im.path):
                    image = im
                    image_found = True
                    break

            # If no path match, try matching on timestamp
            if not image_found:
                for im in images:
                    if (group.date == im.date) and (group.time == im.time):
                        image = im
                        break

            # Find all structure set files inside the dir
            for file in group.files:

                # Create StructureSet
                structure_set = StructureSet(
                    file.path, 
                    image=image,
                    name=None,
                    load=False
                )

                # Add to Image
                if image is not None:
                    image.add_structure_set(structure_set)
                    structure_set.name = f'Structure set {len(image.structure_sets)}'

                # Add to list of all structure sets
                structure_sets.append(structure_set)

        return structure_sets

    def get_description(self):
        """Load a study description."""

        # Find an object from which to extract description
        obj = None
        if self.studies:
            obj = getattr(self, f"{self.image_types[0].lower()}_images")[-1]
        description = ""
        if obj:
            if obj.files:
                image_path = obj.files[-1].path
                ds = pydicom.dcmread(fp=image_path, force=True)
                if hasattr(ds, "StudyDescription"):
                    description = ds.StudyDescription

        return description

    def sum_dose_plans(self, dose_dict={}, sum_type=""):
        """Sum over doses using a given summation type."""

        plan_dose = None
        if sum_type in dose_dict:
            dose = dose_dict[sum_type].pop()
            plan_dose = RtDose()
            plan_dose.machine = dose.machine
            plan_dose.path = dose.path
            plan_dose.subdir = dose.subdir
            plan_dose.date = dose.date
            plan_dose.time = dose.time
            plan_dose.timestamp = dose.timestamp
            plan_dose.summationType = "PLAN"
            plan_dose.imagePosition = dose.imagePosition
            plan_dose.reverse = dose.reverse
            plan_dose.voxelSize = dose.voxelSize
            plan_dose.transform_ijk_to_xyz = dose.transform_ijk_to_xyz
            plan_dose.imageStack = dose.getImageStack()
            for dose in dose_dict[sum_type]:
                plan_dose.imageStack += dose.getImageStack()

        return plan_dose


class Patient(skrt.core.PathData):
    """
    Object associated with a top-level directory whose name corresponds to
    a patient ID, and whose subdirectories contain studies.
    """

    def __init__(self, path="", exclude=["logfiles"]):

        # Set path and patient ID
        if path is None:
            path = os.getcwd()
        self.path = skrt.core.fullpath(path)
        self.id = os.path.basename(self.path)

        # Find studies
        self.studies = self.get_dated_objects(dtype=Study)
        if not self.studies:
            if os.path.isdir(self.path):
                if os.access(self.path, os.R_OK):
                    subdirs = sorted(os.listdir(self.path))
                    for subdir in subdirs:
                        if subdir not in exclude:
                            self.studies.extend(
                                self.get_dated_objects(dtype=Study, subdir=subdir)
                            )

    def add_study(self, subdir='', timestamp=None, images=None, 
                  image_type="CT"):
        '''Add a new study.'''
    
        # Create empty Study object
        s = Study("")
        s.subdir = subdir
        s.timestamp = timestamp if timestamp else skrt.core.generate_timestamp()

        # Add images
        if images:
            for im in images:
                s.add_image(im, image_type)

        # Add to studies list
        self.studies.append(s)

    def combined_files(self, attr, min_date=None, max_date=None):
        """Get list of all files of a given data type <attr> associated with
        this patient, within a given date range if specified."""

        files = []
        for study in self.studies:
            objs = getattr(study, attr)
            for obj in objs:
                for file in obj.files:
                    if file.in_date_interval(min_date, max_date):
                        files.append(file)
        files.sort()
        return files

    def combined_files_by_dir(self, attr, min_date=None, max_date=None):
        """Get dict of all files of a given data type <attr> associated with
        this patient, within a given date range if specified. The dict keys
        will be the directories that the files are in."""

        files = {}
        for study in self.studies:
            objs = getattr(study, attr)
            for object in objs:
                for file in object.files:
                    if file.in_date_interval(min_date, max_date):
                        folder = os.path.dirname(skrt.core.fullpath(file.path))
                        if folder not in files:
                            files[folder] = []
                        files[folder].append(file)

        for folder in files:
            files[folder].sort()

        return files

    def combined_objs(self, attr):
        """Get list of all objects of a given attribute <attr> associated
        with this patient."""

        all_objs = []
        for study in self.studies:
            objs = getattr(study, attr)
            if objs:
                all_objs.extend(objs)
        all_objs.sort()
        return all_objs

    def load_demographics(self):
        """Load a patient's birth date, age, and sex."""

        info = {"BirthDate": None, "Age": None, "Sex": None}

        # Find an object from which to extract the info
        obj = None
        if self.studies:
            obj = getattr(
                self.studies[0], f"{self.studies[0].image_types[0].lower()}_images"
            )[-1]

        # Read demographic info from the object
        if obj and obj.files:
            ds = pydicom.dcmread(fp=obj.files[-1].path, force=True)
            for key in info:
                for prefix in ["Patient", "Patients"]:
                    attr = f"{prefix}{key[0].upper()}{key[1:]}"
                    if hasattr(ds, attr):
                        info[key] = getattr(ds, attr)
                        break

        # Ensure sex is uppercase and single character
        if info["Sex"]:
            info["Sex"] = info["Sex"][0].upper()

        # Store data
        self.age = info["Age"]
        self.sex = info["Sex"]
        self.birth_date = info["BirthDate"]

    def get_age(self):

        self.load_demographics()
        return self.age

    def get_sex(self):

        self.load_demographics()
        return self.sex

    def get_birth_date(self):

        self.load_demographics()
        return self.birth_date

    def get_subdir_studies(self, subdir=""):
        """Get list of studies within a given subdirectory."""

        subdir_studies = []
        for study in self.studies:
            if subdir == study.subdir:
                subdir_studies.append(study)

        subdir_studies.sort()

        return subdir_studies

    def last_in_interval(self, attr=None, min_date=None, max_date=None):
        """Get the last object of a given attribute <attr> in a given
        date interval."""

        files = self.combined_files(attr)
        last = None
        files.reverse()
        for file in files:
            if file.in_date_interval(min_date, max_date):
                last = file
                break
        return last

    def write(
        self,
        outdir=".",
        ext=".dcm",
        to_ignore=None,
        overwrite=True,
        structure_set="all",
        root_uid=None
    ):
        """Write files tree."""

        if not ext.startswith("."):
            ext = f".{ext}"

        patient_dir = os.path.join(os.path.expanduser(outdir), self.id)
        if not os.path.exists(patient_dir):
            os.makedirs(patient_dir)
        elif overwrite:
            shutil.rmtree(patient_dir)
            os.mkdir(patient_dir)

        if to_ignore is None:
            to_ignore = []

        for study in self.studies:

            # Make study directory
            study_dir = os.path.join(
                patient_dir, study.subdir, study.timestamp
            )
            if not os.path.exists(study_dir):
                os.makedirs(study_dir)

            # Loop through image types
            for image_type in study.image_types:

                if image_type in to_ignore:
                    continue

                image_type_dir = os.path.join(study_dir, image_type)
                if not os.path.exists(image_type_dir):
                    os.mkdir(image_type_dir)

                # Write all images of this image type
                for im in getattr(study, f"{image_type.lower()}_images"):

                    # Make directory for this image
                    if im.path:
                        im_timestamp = os.path.basename(im.path)
                    else:
                        im_timestamp = im.timestamp
                    im_dir = os.path.join(image_type_dir, im_timestamp)

                    # Write image data to nifti
                    if ext == ".dcm":
                        outname = im_dir
                    else:
                        outname = f"{im_dir}{ext}"
                    if os.path.exists(outname) and not overwrite:
                        continue
                    Image.write(im, outname, patient_id=self.id,
                                modality=image_type, root_uid=root_uid)

                    # Find structure sets to write
                    if structure_set == "all":
                        ss_to_write = im.get_structure_sets()
                    elif structure_set is None:
                        ss_to_write = []
                    elif isinstance(structure_set, int):
                        ss_to_write = [im.get_structure_sets()[structure_set]]
                    elif skrt.core.is_list(structure_set):
                        ss_to_write = [im.get_structure_sets()[i] for i in structure_set]
                    else:
                        raise TypeError(
                            "Unrecognised structure_set option " f"{structure_set}"
                        )

                    # Write structure sets for this image
                    for ss in ss_to_write:

                        # Find path to output structure directory
                        ss_path = os.path.join(
                            study_dir, 'RTSTRUCT', image_type, im_timestamp
                        )
                        filename = f'RTSTRUCT_{ss.timestamp}'
                        if ext == ".dcm":
                            ss_dir = ss_path
                        else:
                            ss_dir = os.path.join(ss_path, filename)

                        # Ensure it exists
                        if not os.path.exists(ss_path):
                            os.makedirs(ss_path)

                        # Write dicom structure set
                        if ext == ".dcm":
                            if os.path.exists(ss_path) and not overwrite:
                                continue
                            ss.write(outname=f'{filename}.dcm', outdir=ss_path)

                        # Write ROIs to individual files
                        else:
                            ss.write(outdir=ss_dir, ext=ext)

