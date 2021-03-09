#!/usr/bin/env python

import copy
import cv2
import numpy as np

from imagewindow import ImageWindow
import imageprocessing
from bodypart_motion import MotionTrackedBodypart, MotionTrackedBodypartPolar

from MsgFlyState import MsgState


###############################################################################
###############################################################################
# EdgeTrackerByIntensityProfile()
# Track radial bodypart edges using the gradient of the image intensity.
# i.e. Compute how the intensity changes with angle, and detect the locations
# of the greatest change.  Usually used for Wings.
#
class EdgeTrackerByIntensityProfileCustom(MotionTrackedBodypartPolar):
    def __init__(self, name=None, params={}, color='white', bEqualizeHist=False):
        MotionTrackedBodypartPolar.__init__(self, name, params, color, bEqualizeHist)
        
        self.name        = name
        self.state       = MsgState()
        self.windowEdges = ImageWindow(False, self.name+'Edges')
        self.windowEdges.set_enable(True)
        self.set_params(params)
    
    # set_params()
    # Set the given params dict into this object.
    #
    def set_params(self, params):
        MotionTrackedBodypartPolar.set_params(self, params)
        
        self.imgRoiBackground = None
        self.iCount = 0

        self.state.intensity = 0.0
        self.state.angles = []
        self.state.gradients = []

        # Compute the 'handedness' of the head/abdomen and wing/wing axes.  self.sense specifies the direction of positive angles.
        matAxes = np.array([[self.params['gui']['head']['hinge']['x']-self.params['gui']['abdomen']['hinge']['x'], self.params['gui']['head']['hinge']['y']-self.params['gui']['abdomen']['hinge']['y']],
                            [self.params['gui']['right']['hinge']['x']-self.params['gui']['left']['hinge']['x'], self.params['gui']['right']['hinge']['y']-self.params['gui']['left']['hinge']['y']]])
        if (self.name in ['left','right']):
            self.senseAxes = np.sign(np.linalg.det(matAxes))
            a = -1 if (self.name=='right') else 1
            self.sense = a*self.senseAxes
        else:
            self.sense = 1

        #self.detector.set_params(params[self.name]['threshold'], params['n_edges_max'], self.sense)
    
        
    # update_state()
    #
    def update_state(self):
        imgNow = self.imgRoiFgMaskedPolarCropped

        # Get the rotation & expansion between images.
        if (imgNow is not None):
            # Pixel position and strength of the edges.
            #(edges, gradients) = self.detector.detect(imgNow)

            blur = cv2.GaussianBlur(imgNow, (5, 5), 0)
            ret3, bw = cv2.threshold(imgNow, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            on_ratio = np.true_divide((bw == 255).sum(), bw.size)
            kernel  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
            bw = cv2.dilate(bw, kernel, iterations = 1)
            #self.windowEdges.set_image(bw)

            angle_hi = imageprocessing.get_angle_from_points_i(
                np.array([self.handles['hinge'].pt[0], self.handles['hinge'].pt[1]]),
                np.array([self.handles['angle_hi'].pt[0], self.handles['angle_hi'].pt[1]]))
            angle_lo = imageprocessing.get_angle_from_points_i(
                np.array([self.handles['hinge'].pt[0], self.handles['hinge'].pt[1]]),
                np.array([self.handles['angle_hi'].pt[0], self.handles['angle_lo'].pt[1]]))
            angle_hi = self.transform_angle_b_from_i(angle_hi)
            angle_lo = self.transform_angle_b_from_i(angle_lo)

            angle = on_ratio * (angle_hi - angle_lo) + angle_lo
            angle = (self.transform_angle_p_from_b(angle) + np.pi) % (2*np.pi) - np.pi
            self.windowEdges.set_image(bw)
            print(self.name+'Edges = ' + str(np.rad2deg(angle)))

            #anglePerPixel = (self.params['gui'][self.name]['angle_hi']-self.params['gui'][self.name]['angle_lo']) / float(imgNow.shape[1])

            # Convert pixel to angle units, and put angle into the wing frame.
            self.state.angles = [angle]
            self.state.gradients = []
            self.state.intensity = np.mean(imgNow)/255.0

        
    # update()
    # Update all the internals given a foreground camera image.
    #
    def update(self, dt, image, bInvertColor):
        MotionTrackedBodypartPolar.update(self, dt, image, bInvertColor)

        if (self.params['gui'][self.name]['track']):
            self.update_state()
            

    # draw()
    # Draw the outline.
    #
    def draw(self, image):
        MotionTrackedBodypartPolar.draw(self, image)
        
        if (self.params['gui'][self.name]['track']):
            # Draw the major and minor edges alternately, until the max number has been reached.
            bgra = self.bgra
            for i in range(len(self.state.angles)):
                angle_b = self.transform_angle_b_from_p(self.state.angles[i])
                angle_i = self.transform_angle_i_from_b(angle_b)

                x0 = self.ptHinge_i[0] + self.params['gui'][self.name]['radius_inner'] * np.cos(angle_i)
                y0 = self.ptHinge_i[1] + self.params['gui'][self.name]['radius_inner'] * np.sin(angle_i)
                x1 = self.ptHinge_i[0] + self.params['gui'][self.name]['radius_outer'] * np.cos(angle_i)
                y1 = self.ptHinge_i[1] + self.params['gui'][self.name]['radius_outer'] * np.sin(angle_i)
                cv2.line(image, (int(x0),int(y0)), (int(x1),int(y1)), bgra, 1)
                bgra = tuple(0.5*np.array(bgra))
                
            self.windowEdges.show()
        
# end class EdgeTrackerByIntensityProfile
