
import glob, os
import numpy as np
import h5py


class FileImport:
    def __init__(self):
        pass

    def get_files(self, root, filespec):
        # Get all files in directory that fit filespec
        self.root = root
        self.filespec = filespec

        os.chdir(self.root)
        self.files = glob.glob(self.filespec)
        self.files.sort()
        self.n_file = len(self.files)

    def get_filedata(self, fullfile):
        # Get file data
        self.file = fullfile
        self.path, self.basename = os.path.split(self.file)
        self.fname , self.ext = os.path.splitext(self.basename)
        self.targetfile = os.path.join(self.path,self.fname)

    def get_matdata(self, fullfile, vidname):
        # Get file data & .mat data
        self.file = fullfile
        self.path, self.basename = os.path.split(self.file)
        self.fname , self.ext = os.path.splitext(self.basename)
        self.targetfile = os.path.join(self.path,self.fname)

        # Extract video data from .mat file
        # print('Loading data ...')
        data = h5py.File(self.file, 'r')  # load file
        arrays = {}
        for k, v in data.items():
            try:
                arrays[k] = np.array(v)
            except:
                #print('Can not load in variable')
                pass
        # print('done')

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