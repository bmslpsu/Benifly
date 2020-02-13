
import time , os , sys
from Benifly import MainWindow
from filemanager import FileManager
import shutil
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

Benifly = MainWindow() # create Benifly instance

nodename = MainWindow.__module__
mainroot = os.path.dirname(os.path.dirname(imp.find_module(nodename)[1]))

print('Files to track:')
print('-------------------------------------')
for f in FileSelect.basename:
    print(f)
print('-------------os.path.join------------------------\n')


# Loop through and track all files
n = 0
for f in FileSelect.files:
    print 'Tracking: ' , f
    # Loop files to set auto-zero ===> press "w" when done with file
    Benifly.loopMat(FileSelect.files[n], vidname)
    shutil.copy2(os.path.join(mainroot,'params.json'), os.path.join(maskdir, FileSelect.fname[n] + '.json'))
    n = n + 1

    time.sleep(1)

print('----------MASKS DONE----------')
