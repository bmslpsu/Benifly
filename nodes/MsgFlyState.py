#!/usr/bin/env python

class MsgFlyState:
    def __init__(self):
        self.head           = []
        self.abdomen        = []
        self.left           = []
        self.right          = []
        self.aux            = []


class MsgState:
    def __init__(self):
        self.angles         = []
        self.gradients      = []
        self.radii          = []
        self.freq           = []
        self.intensity      = []

class Header:
    def __init__(self, seq, stamp, frame_id):
        self.seq            = []
        self.stamp          = []
        self.frame_id       = []

class Rosimg:
    def __init__(self, header, height, width, encoding, is_bigendian, step, data):
        self.header         = Header
        self.height         = []
        self.width          = []
        self.encoding       = []
        self.is_bigendian   = []
        self.step           = []
        self.data           = []