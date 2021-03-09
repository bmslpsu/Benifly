
import time , os
from Benifly import MainWindow
from filemanager import FileManager


root = r'E:\EXPERIMENTS\RIGID\Experiment_Asymmetry_Control_Verification\HighContrast\30\Vid\wing_filt_60'
targetdir = os.path.join(root,'tracked_head_wing') # where to save output data & video
vidname = 'regvid' # name of video variable in MATLAB .mat file (does not apply to videos of other formats)

params = 'C:\Users\BC\PycharmProjects\Run_Benifly\params_magno.json' # location of parameter file

# Paramselect = FileManager() # create FileManager instance
# Paramselect.Select(targetdir) # open file selection GUI in root folder
# params = Paramselect.files[0]

FileSelect = FileManager() # create FileManager instance
FileSelect.Select(root) # open file selection GUI in root folder

print('Files to track:')
print('-------------------------------------')
for f in FileSelect.basename:
    print(f)
print('-------------------------------------\n')

Benifly = MainWindow(params)  # create Benifly instance

# print('Looping...')
# loop = [0]
# for f in loop:
#     Benifly.loopMat(FileSelect.files[f], vidname)

# Loop through and track all files
for f in FileSelect.files:
    # print 'Tracking: ', f

    # Benifly.runMat(f, vidname, targetdir)
    Benifly.loopMat(f, vidname, targetdir)

    time.sleep(1)

print('----------DONE----------')