
import time , os
from Benifly import MainWindow
from filemanager import FileManager

root = 'H:\EXPERIMENTS\MAGNO\Experiment_SOS/registered' # folder with video files
targetdir = os.path.join(root,'tracked') # where to save output data & video
vidname = 'regvid' # name of video variable in MATLAB .mat file (does not apply to videos of other formats)
params = 'C:\Users/boc5244\PycharmProjects\RunBenifly\params_test.json' # params file location

FileSelect = FileManager() # create FileManager instance
FileSelect.Select(root) # open file selection GUI in root folder

print('Files to track:')
print('-------------------------------------')
for f in FileSelect.basename:
    print(f)
print('-------------------------------------\n')

Benifly = MainWindow(params)  # create Benifly instance

# Loop through and track all files
for f in FileSelect.files:
    print 'Tracking: ', f

    Benifly.loopMat(f, vidname) # click done when finished
    Benifly.runMat(f, vidname, targetdir) # run tracking

    time.sleep(1)

print('----------DONE----------')