
import glob, os
import numpy as np
import h5py


class FileImport:
    def __init__(self):
        self.root = ''
        self.file = ''
        self.filename = ''
        self.targetdir = ''
        self.targetpath = ''
        self.vid = []
        self.n_frame = 0
        self.width = 0
        self.height = 0

    def get_matdata(self, root, file, vidname, targetdir):
        # Get all files in directory that fit filespec
        self.root = root
        self.file = file
        self.targetdir = targetdir
        self.filename = os.path.splitext(self.file)[0]
        self.targetpath = self.targetdir + '/' + self.filename + '.txt'

        os.chdir(self.root)

        # Extract video data from .mat file
        data = h5py.File(file, 'r')  # load file
        arrays = {}
        for k, v in data.items():
            arrays[k] = np.array(v)

        self.vid = []
        try:
            self.vid = arrays[vidname]          # video matrix
            self.vid = np.squeeze(self.vid)     # get rid of singleton dimension
            self.n_frame = self.vid.shape[0]    # # of frames
            self.width = self.vid.shape[1]      # frame width
            self.height = self.vid.shape[2]     # frame height
        except (ValueError, Exception):
            print "No variable named " , vidname


#if __name__ == '__main__':
    #main = FileImport()