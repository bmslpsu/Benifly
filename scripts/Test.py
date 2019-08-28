
from Benifly import MainWindow
from fileimport import FileImport
import time

# USER: set these variables
#---------------------------------------------------------------------------------------
mainroot = "C:\Users/boc5244\PycharmProjects\Benifly" # location of Benifly root
#---------------------------------------------------------------------------------------
root = 'H:\EXPERIMENTS\Experiment_Chirp_Walking\mat'  # folder with MATLAB video files
filespec = 'fly_1_trial_2_Amp_7.5.mat' # files to track
targetdir = 'C:\Users/boc5244\Documents/temp\out' # where to save output data & video
vidname = 'Vid' # name of video variable in MATLAB .mat file
#---------------------------------------------------------------------------------------

Benifly = MainWindow(mainroot) # create Benifly instance
VID = FileImport() # create FileImport instance
VID.get_files(root,filespec) # get all files that fit filespec in root
print(VID.files)

# Loop through and track all files
iCount = 1
for f in VID.files:
    print f
    # USER: uncomment method to use
    #---------------------------------------------------
    # Benifly.loopMat(root, f, vidname)
    # Benifly.loopVid(root, f)
    # Benifly.runMat(root, f, vidname, targetdir)
    # Benifly.runVid(root, f, targetdir)
    # Benifly.loopLive()
    #----------------------------------------------------
    time.sleep(2)
    iCount+=1

print('----------DONE----------')