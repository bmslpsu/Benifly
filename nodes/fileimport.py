
import glob, os
import numpy as np
import h5py


class FileImport:
    def __init__(self):
        self.root = ''
        self.filespec = ''
        self.files = {}
        self.n_file = 0
        self.vid = []
        self.n_frame = 0

    def get_files(self, root, filespec):
        # Get all files in directory that fit filespec
        self.root = root
        self.filespec = filespec

        os.chdir(self.root)
        self.files = glob.glob(self.filespec)
        self.files.sort()
        self.n_file = len(self.files)


    def get_matdata(self,file,vidname):
        # Extract video data from .mat file
        data = h5py.File(file, 'r')  # load file
        arrays = {}
        for k, v in data.items():
            arrays[k] = np.array(v)

        self.vid = []
        try:
            self.vid = arrays[vidname]   # video matrix
            self.vid = np.squeeze(self.vid)   # get rid of singleton dimension
            self.n_frame = self.vid.shape[2]  # # of frames
        except (ValueError, Exception):
            print "No variable named " , vidname


#if __name__ == '__main__':
    #main = FileImport()

    #root = 'Q:\Box Sync'
    filespec = 'fly_1_trial_*.mat'

    #main.get_files(root,filespec)

    #path = os.path.join(main.root,main.files[0])

    #main.get_matdata(path, 'vidData')

    #print('Done')