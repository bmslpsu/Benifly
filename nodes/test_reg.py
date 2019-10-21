
from __future__ import print_function
import cv2
import numpy as np
import os

from fileimport import FileImport

class IMregister(object):
    def __init__(self, vidpath, vidname):
        self.vidpath = vidpath
        self.vidname = vidname
        self.filedata = FileImport()
        self.filedata.get_filedata(self.vidpath)
        self.vid = np.array(0)
        self.max_features = 500
        self.good_match_percent = 0.15
        self.frame_height = 0
        self.frame_width = 0
        self.frame_count = 0
        self.fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self.vidout = []
        self.fs = 60
        self.regvidpath = []

        print("Video loading..."),
        if (self.filedata.ext.lower() == ".mat"):
            self.filedata.get_matdata(self.vidpath, self.vidname)
            self.vid = self.filedata.vid
            self.frame_height = self.filedata.height
            self.frame_width = self.filedata.width
            self.frame_count = self.filedata.n_frame
        elif (self.filedata.ext.lower() == ".avi") or (self.filedata.ext.lower() == ".mp4") or (self.filedata.ext.lower() == ".mov"):
            self.ReadVid()
        print("Video loaded")
        self.regvid = np.empty((self.frame_count, self.frame_width, self.frame_height), np.dtype('uint8'))
        self.h = np.empty((self.frame_count,3,3), np.dtype('int8'))

        self.alignVid()
        self.displayVid()

    def saveVid(self,path,fs):
        self.regvidpath = os.path.join(path,self.filedata.fname + ".avi")
        self.fs = fs
        self.vidout = cv2.VideoWriter(self.regvidpath, self.fourcc, fs, (self.frame_width,  self.frame_height))
        print("Saving ",self.frame_count," frames...")
        for frame in range(self.frame_count):
                self.vidout.write(self.regvid[frame,:,:])
        self. vidout.release()
        print("Registered video saved: " + self.regvidpath)

    def displayVid(self):
        cv2.namedWindow('Montage', cv2.WINDOW_NORMAL)
        for frame in range(self.frame_count):
            display = np.hstack((self.vid[frame,:,:], self.regvid[frame,:,:],))
            cv2.imshow('Montage', display)
            cv2.waitKey(2)
            if cv2.waitKey(2) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

    def alignVid(self):
        print("Registering",self.frame_count," frames...")
        for frame in range(self.frame_count):
            imReg, h = self.alignImages(self.vid[frame,:,:],self.vid[1,:,:])
            self.regvid[frame,:,:] = imReg
            self.h[frame,:,:] = h

            print(frame)

    def alignImages(self,im1,im2):
        # Convert images to grayscale
        #im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        #im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
        im1Gray = im1
        im2Gray = im2

        # Detect ORB features and compute descriptors.
        orb = cv2.ORB_create(self.max_features)
        keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
        keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

        # Match features.
        matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
        matches = matcher.match(descriptors1, descriptors2, None)

        # Sort matches by score
        matches.sort(key=lambda x: x.distance, reverse=False)

        # Remove not so good matches
        numGoodMatches = int(len(matches) * self.good_match_percent)
        matches = matches[:numGoodMatches]

        # Draw top matches
        imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
        # cv2.imwrite("matches.jpg", imMatches)

        # Extract location of good matches
        points1 = np.zeros((len(matches), 2), dtype=np.float32)
        points2 = np.zeros((len(matches), 2), dtype=np.float32)

        for i, match in enumerate(matches):
            points1[i, :] = keypoints1[match.queryIdx].pt
            points2[i, :] = keypoints2[match.trainIdx].pt

        # Find homography
        h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

        # Use homography
        height, width = im2.shape
        im1Reg = cv2.warpPerspective(im1, h, (width, height))

        return im1Reg, h

    def ReadVid(self):
        cap = cv2.VideoCapture(self.vidpath)
        #frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        self.vid = np.empty((self.frame_count, self.frame_height, self.frame_width), np.dtype('uint8'))
        idx = 0
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                self.vid[idx,:,:] = gray
            else:
                break
            idx += 1
            # cv2.imshow('frame', gray)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    from filemanager import FileManager

    vidname_1 = "viddata"
    root = "Q:\Box Sync"
    FileSelect = FileManager()  # create FileManager instance
    FileSelect.Select(root)  # open file selection GUI in root folder

    test = IMregister(FileSelect.files[0],vidname_1)

    savepath = "Q:\Box Sync\Research"
    fs_1 = 60
    test.saveVid(savepath,fs_1)

    print('DONE')