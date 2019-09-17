
import time
from Benifly import MainWindow
from filemanager import FileManager

# USER: set these variables
#---------------------------------------------------------------------------------------
root = 'E:\Walking_Experiments\SOS\mat'  # folder with video files
targetdir = 'E:\Walking_Experiments\SOS\mat\Retrack' # where to save output data & video
vidname = 'rawVid' # name of video variable in MATLAB .mat file (does not apply to video other formats)
fps = 60 # output frame rate in Hz (not required)
#---------------------------------------------------------------------------------------

FileSelect = FileManager() # create FileManager instance
FileSelect.Select(root) # open file selection GUI in root folder

Benifly = MainWindow() # create Benifly instance

print('Files to track:')
print('-------------------------------------')
for f in FileSelect.basename:
    print(f)
print('-------------------------------------\n')

# Loop through and track all files
for f in FileSelect.files:
    print 'Tracking: ' , f

    # USER: uncomment method to use
    #---------------------------------------------------
    Benifly.loopMat(f, vidname)
    # Benifly.loopVid(f)
    # Benifly.runMat(f, vidname, targetdir, fps)
    # Benifly.runVid(f, targetdir, fps)
    # Benifly.loopLive()
    #----------------------------------------------------

    time.sleep(1)

print('----------DONE----------')