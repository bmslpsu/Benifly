
from Benifly import MainWindow
from fileimport import FileImport
import time

# USER: set these variables
#-----------------------------------------------------------------------------------------
root = 'Q:/temp'  # folder with video files
filespec = 'Fly_1_*.mat' # files to track
targetdir = 'Q:/temp\out' # where to save output data & video
vidname = 'vidData' # name of video variable in MATLAB .mat file (for .mat files only)
#-----------------------------------------------------------------------------------------

Benifly = MainWindow() # create Benifly instance
VID = FileImport() # create FileImport instance
VID.get_files(root,filespec) # get all files that fit filespec in root
print(VID.files)

# Loop through and track all files (if running a Benifly.loop function, we will stay on the first file until stopped,
# this is helpful for setting the mask before tracking & saving data)
iCount = 1
for f in VID.files:
    print f
    # USER: uncomment method to use
    #---------------------------------------------------
    # Benifly.loopLive()
    # Benifly.loopMat(root, f, vidname)
    # Benifly.loopVid(root, f)
    # Benifly.runMat(root, f, vidname, targetdir)
    # Benifly.runVid(root, f, targetdir)
    #----------------------------------------------------
    time.sleep(2)
    iCount+=1

print('----------DONE----------')