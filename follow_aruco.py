#!/usr/bin/python3
"""
Start your robot at the entrance of the classroom. Guide your robot with an ArUco marker to navigate to the designated area.
1. Define a new class to include two new functions: foward_left(), and foward_right().
2. Use built-in function in OpenCV to detect the ArUco marker.
3. Move your robot based on the location of the marker in your video images.
"""
import cv2
from picamera2 import Picamera2
cv2.startWindowThread()
picam2 = Picamera2()


#### Write your code below ####
