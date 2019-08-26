
from Benifly import MainWindow
from fileimport import FileImport

Benifly = MainWindow() # create Benifly instance
Files = FileImport() # create FIleImport instance

root = 'Q:/temp'  # folder with MATLAB video files
filespec = 'fly_1_*.mat' # files to track
targetdir = 'Q:\Box Sync' # where to save output data & video
vidname = 'vidData' # name of video variable in MATLAB .mat file

Files.get_files(root,filespec) # get all files that fit filespec in root

# Loop through and track all files
iCount = 1
for f in Files.files:
    print 'File: ' , iCount
    #Benifly.loopVid(Files.root, f, vidname)
    Benifly.runVid(root, f, vidname, targetdir)
    iCount+=1

print('DONE')