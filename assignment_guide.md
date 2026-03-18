# ArUco Marker Follower

## 1. Overview
With vision, the robots no longer walk in the darkness.
Robotic vision is the cornerstone of modern autonomy, transforming passive machines into intelligent agents capable of interacting dynamically with their environment.

The robotic vision is widely used in the following industrial and technological shifts.
- Warehouse Automation & Logistics: Companies like Amazon and automated factories rely heavily on the vision systems to navigate fleets of Automated Guided Vehicles (AGVs) through complex environments safely and efficiently.
- Precision Docking & Navigation: Whether it is a Mars rover aligning with a sample tube, an autonomous underwater vehicle returning to its base, or a robotic vacuum finding its charging station, vision-based pose estimation is critical for millimeter-perfect precision.
- SLAM: extract features from 2Dor 3D images is robot's first step toward building complex maps of unknown environments.

In this assignment, we will gain hands-on experience with:
1. ArUco marker detection under the ROS 2 framework.
2. Decisions making to drive the robot approaching the marker.
3. ROS 2 Packaging. 


## 2. Get Started
1. [Connect RPi Camera Module](https://projects-static.raspberrypi.org/projects/getting-started-with-picamera/9aeb5ca06297d9c3d14d3d2d3e36bf5cd8c6466b/en/images/connect-camera.gif).
> [!WARNING]
> Please disconnect power when you (dis)connecting the camera module.
2. (Optional) [Install Software](https://linzhanguca.github.io/homer_docs/setup/rpi/) 
3. An [example](https://github.com/linzhangUCA/homer_bringup/blob/main/homer_bringup/aruco_detector.py) of ArUco marker detection. 

## 3. Requirements: 

### 3.1. (10%) Publish [`Image`](https://docs.ros2.org/foxy/api/sensor_msgs/msg/Image.html) message from camera module.
- Publish an appropriate ROS 2 topic with reasonable image resolution and publishing rate.
  Write down commands for doing this in [README](README.md).
 
### 3.2. (15%) Detect and localize ArUco marker.
- (10%) Document the ArUco marker (ID \#) and its picture in [README](README.md).
- (10%) Subscribe to the topic bears the `Image` message and detect the **interested** ArUco marker.
  Extract corner coordinates of the marker.

### 3.3. (25%) Follow ArUco Marker
- Develop an approach to guide your robot always following the marker.
  Publish appropriate `Twist` like message at a reasonable rate to guide your robot approaching the marker.


### 3.5. (40%) Demonstration
Demonstrate "chemical reactions" between you and your robot.
Use the **proposed** ArUco marker guiding your robot finish the journey described in Project 2.  

### 3.6. (10%) Package ArUco follower
Create a package to host all your executables and make sure `ros2 run <package_name> <executable_name>` command is available after the package is built.


## AI Policies
Please acknowledge AI's contributions according to the policies in the syllabus.
