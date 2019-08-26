# Benifly
Offline version of Kinefly for Windows/Linux without ROS

## Introduction
[**Benifly**](https://github.com/bmslpsu/Benifly) is based on [**Kinefly**](https://github.com/ssafarik/Kinefly) software developed by [Steve Safarik](https://github.com/ssafarik), which was designed for tracking tethered insect kiematics in real time. While Kinefly is designed for ROS, which requires a Linuxed based OS, Benifly only requires [Python 2](https://www.python.org/downloads/release/python-273/), so any recent Windows OS is appropriate. Benifly maintains the majority of Kinefly's core functionality, including virtually all image processing algorithms and error handling. However, instead of taking in an image stream from a camera in real-time, Benifly reads in previously recorded video files (tested for .avi,.mp4, & MATLAB data).

## Installation
Benifly is simply a collection of Python classes and functions that can be called to perform various computer vision alogorithms, thus there are no special installion requirements. The repository should simply be cloned into a directory of your choosing, and the Python path should be set to include all modules in the Benifly directory. It is highly reccomended that users install an integrated development environment (IDE) to manage modules and packages ([Pycharm](https://www.jetbrains.com/pycharm/) & [Visual Studios](https://visualstudio.microsoft.com/) work well).

Benifly requires the following external Python packages:
* **open-cv**   (for various image processing processes)
* **numpy**     (to handle numeric data & calculations)
* **h5py**      (to load .mat files)

## Operation
It is recommended that users start by reading [Kinefly documentation](https://github.com/ssafarik/Kinefly) to understand the basic functionality of the software.

The first Python file that should be run is `BatchBenifly.py`. This will allow the user to specify which video files to feed to Benifly and where to save the output.

The user can set the following variables:
 * `root`: directory where video files are located
 * `filespec`: this can be a file name or partial file name that reads in all files with the filespec
 * `targetdir`: directory to save Benifly output
 * `vidname`: the name of the video data variable in the .mat file (necessary for MATLAB videos only)
 
 It is recommended that `root` & `targetdir` be different directories.
 
 Currently, Benifly has four main functions.
 1. #### `Benifly.runLoop`
  Will continuously track one video until stopped by the user. There is no output, This is especially useful for setting the mask before tracking and outputing sata for videos. 
  
 ##Output
 Benifly outputs two files:
 * `filename.csv`: contains the head, abdomen,left & right wing angles for all frames of the input video
 * `filename.avi`: the saved Kinefly video feed
 
 For both output files, `filename` is will be the same name as the video file fed to Benifly.