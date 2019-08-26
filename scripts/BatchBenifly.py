
from Benifly import MainWindow
from fileimport import FileImport

# USER: set these variables
#-------------------------------------------------------------------------
mainroot = "C:\Users\BC\PycharmProjects\Benifly"
root = 'Q:/temp'  # folder with MATLAB video files
filespec = 'fly_1_*.mat' # files to track
targetdir = 'Q:/temp/out' # where to save output data & video
vidname = 'vidData' # name of video variable in MATLAB .mat file
#-------------------------------------------------------------------------

Benifly = MainWindow(mainroot) # create Benifly instance
VID = FileImport() # create FileImport instance
VID.get_files(root,filespec) # get all files that fit filespec in root

# Loop through and track all files
iCount = 1
for f in VID.files:
    print 'File: ' , iCount

    # USER: Uncomment Method to use
    #---------------------------------------------------
    # Benifly.loopLive()
    # Benifly.loopMat(root, f, vidname)
    # Benifly.loopVid(root, f, vidname)
    # Benifly.runMat(root, f, vidname, targetdir)
    # Benifly.runVid(root, f, vidname, targetdir)
    #----------------------------------------------------

    iCount+=1

print('----------DONE----------')