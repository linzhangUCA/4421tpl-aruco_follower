# ArUco Marker Follower
Guide your robot with an ArUco marker. Navigate the robot from the entrance of LSCA 105 to the blue marker next to the south wall of the classroom. 


## Instructions: 
Complete `follow_aruco.py`.
1. (20%) Retrieve video frames using RPi camera.
2. (30%) Detect and localize ArUco marker in every video frame.
3. (30%) Use appropriate navigation strategies (e.g. move "forward left" if marker shown on left half of the video frame; stop if robot cannot detect any marker).  
4. (20%) Upload a video to show the whole navigation process.

#### Hints
- You may need [picamera2](https://github.com/raspberrypi/picamera2) library to capture video.
- An inspiring [example](https://github.com/raspberrypi/picamera2/blob/main/examples/opencv_face_detect.py), but face detection.
- ArUco marker detection [example](https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/)
- A [video streaming server](https://github.com/raspberrypi/picamera2/blob/main/examples/mjpeg_server.py) can be useful for debugging.
- You may want to tweek the motor speed to get a more comfortable driving experience. 


## Helpful Resources
- Getting started with RPi camera [tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2).
- Waveshare Motor Driver Board [Wiki Page](https://www.waveshare.com/wiki/RPi_Motor_Driver_Board).
- [gpiozero API](https://gpiozero.readthedocs.io/en/stable/). 
- [picamera2 manual](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)
- [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
