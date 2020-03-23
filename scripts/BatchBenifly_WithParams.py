
import time , os
from Benifly import MainWindow
from filemanager import FileManager
import imp


# USER: set these variables
#---------------------------------------------------------------------------------------
root = 'E:\Experiment_SOS_v1/registered'  # folder with video files
targetdir = os.path.join(root,'tracked_headwing') # where to save output data & video
maskdir =  os.path.join(root,'mask') # where to save masks
vidname = 'regvid' # name of video variable in MATLAB .mat file (does not apply to videos of other formats)
#---------------------------------------------------------------------------------------

FileSelect = FileManager() # create FileManager instance
FileSelect.Select(root) # open file selection GUI in root folder


# Loop through and track all files

for f in FileSelect.basename:
    print 'Tracking: ', f
    params = os.path.join(maskdir, f)  # parameter file location
    Benifly = MainWindow(params)  # create Benifly instance
    g = f[0:-5] + '.mat' # Create Matlab file name
    Benifly.runMat(os.path.join(root, g ), vidname, targetdir) # run tracking

    time.sleep(1)

print('----------DONE----------')