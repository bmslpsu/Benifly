
from Benifly import MainWindow
from fileimport import FileImport
import time

# USER: set these variables
#---------------------------------------------------------------------------------------
root = 'H:\EXPERIMENTS\Experiment_SOS_v2'  # folder with MATLAB video files
filespec = 'fly_2_trial_3_SOS.mat' # files to track
targetdir = 'C:\Users/boc5244\Documents/temp\out' # where to save output data & video
vidname = 'vidData' # name of video variable in MATLAB .mat file
#---------------------------------------------------------------------------------------

Benifly = MainWindow() # create Benifly instance
VID = FileImport() # create FileImport instance
VID.get_files(root,filespec) # get all files that fit filespec in root
print(VID.files)

# Loop through and track all files
iCount = 1
for f in VID.files:
    print f
    # USER: uncomment method to use
    #---------------------------------------------------
    Benifly.loopMat(root, f, vidname)
    # Benifly.loopVid(root, f)
    # Benifly.runMat(root, f, vidname, targetdir)
    # Benifly.runVid(root, f, targetdir)
    # Benifly.loopLive()
    #----------------------------------------------------
    time.sleep(2)
    iCount+=1

print('----------DONE----------')