# xnat_import
Collection of python scripts to import public imaging datasets into XNAT

To get started:
1) Familiarize yourself with neuroimaging data   
   http://miykael.github.io/nipype-beginner-s-guide/neuroimaging.html

2) Install FSL (http://fsl.fmrib.ox.ac.uk/fsldownloads/fsldownloadmain.html)
   FSL is a popular brain imaging analysis software that includes useful command line tools such as 
   a) fslview           image viewer 
   b) fslreorient2std   reorient images to a standard orientation (so that images all face the same way when viewed
   c) slicer            create 2D images of 3D volumes to view in web browser for QC etc.
   Plus much more. 
   
3) Familiarize yourseful a bit with XNAT
   a) https://www.xnat.org/about/             Short introduction to XNAT
   
4) Install Python and pyxnat. pyxnat is a pythonic wrapper around the XNAT REST API and is useful interface to XNAT. It can be used to      import data and metdata into XNAT. Some useful links for getting acquainted with pyxnat are:
  a) https://pythonhosted.org/pyxnat/starters_tutorial.html              Useful beginner's tutorial and guide
     http://xnat.bigr.nl/index.php/Xnat:Pyxnat                           Example for uploading data to XNAT
     https://wiki.xnat.org/display/XNAT16/XNAT+REST+XML+Path+Shortcuts   Useful to set common attributes (metadata) in XNAT
     https://pythonhosted.org/pyxnat/features/files.html                 Useful for transfering files

Short challenge: After reading through the above documentation (4a and maybe some additional googling) use pyxnat to connect to https://central.xnat.org/ (you may need to sign up for a guest account) and select and print out all the subject_ids included in the  CENTRAL_OASIS_CS project
