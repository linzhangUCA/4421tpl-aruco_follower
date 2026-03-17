# ArUco Marker Follower

## 1. Overview
Robotic vision is the cornerstone of modern autonomy, transforming passive machines into intelligent agents capable of interacting dynamically with their environment.
With vision, the robot will not walk in the darkness.

The robotic vision is widely used in the following industrial and technological shifts.
1. Warehouse Automation & Logistics: Companies like Amazon and automated factories rely heavily on the vision systems to navigate fleets of Automated Guided Vehicles (AGVs) through complex environments safely and efficiently.
2. Precision Docking & Navigation: Whether it is a Mars rover aligning with a sample tube, an autonomous underwater vehicle returning to its base, or a robotic vacuum finding its charging station, vision-based pose estimation is critical for millimeter-perfect precision.
3. Advanced SLAM: ArUco markers act as perfect "ground truth" landmarks. Understanding how to extract a marker's pose (position and orientation) from a 2D image is your first step toward building complex 3D maps of unknown environments.

In this assignment, we will gain hands-on experience with:
1. ArUco marker detection under the ROS 2 framework.
2. Decisions making to drive the robot approaching the marker.
3. ROS 2 Packaging. 


## 2. Get Started
To simulate a physical robot's movement, we can measure the velocity of the robot using on-board sensors (e.g. encoders).
Then feed the measured velocity as the target/reference velocity command for the differential drive turtle from the `turtlesim_node`.

### 2.1. Reference Workflow
1. Open a terminal and start `turtlesim_node`.
```console
ros2 run turtlesim turtlesim_node
```
2. Start transform broadcasting node in another terminal.
```console
ros2 run <homer8_package> <tf_bc_node> 
```
3. (Optional) Start robot driving node in the third terminal.
```console
ros2 run <homer8_package> <driver_node> 
```

> [!NOTE]
> The commands wrapped in `<>` are customizable.

### 2.2 Preparation
- Have HomeR or your favorite ground robot [assembled](https://linzhanguca.github.io/homer_docs/mechanical/assembly/).
- Let the [Pico Messenger](https://github.com/linzhanguca/homer_pico) running at the background on Pico.
So that HomeR's linear and angular velocity can be set and measured from a Raspberry Pi.
- If `turtlesim_node` is running on a different computer other than Raspberry Pi, make sure `ROS_DOMAIN_ID` on these computers are the same.
Attach `export ROS_DOMAIN_ID=<numer>` to the end of `~/.bashrc` file **on both computers**, then `source ~/.bashrc`.
- Review the trajectory calculation from robotics 1's [slides](https://linzhanguca.github.io/_docs/robotics1-2025/1014/kinematics.pdf).
If you are running out of time, HomeR's [hardware interface node](https://github.com/linzhangUCA/homer_bringup/blob/main/homer_bringup/homer_interface.py) is the goto.


## 3. Requirements: 

### 3.1. (50%) Broadcast transform
- (20%) Listen to Pico for measured linear and angular velocity of the robot.
Whenever the Raspberry Pi received the measured velocities, publish them to the proper topic to drive the simulated turtle.
- (15%) Subscribe to a `Twist` message topic (e.g. `/cmd_vel` from the driver node or `teleop_twist_keyboard`).
send `linear.x` and `angular.z` data as the robot's reference velocity command to Pico.
- (10%) Compute `base_link` frame's position and orientation relative to the `odom` frame.
Broadcast the tansform of the frames at the frequency of 20 Hz.
- (5%) Illustrate the relationship between `odom` frame and `base_link` frame in a transform tree graph.
Upload the graph to the repository and display it in [README](README.md)

> [!TIP]
> - You can add "TF" in `rviz2` to visualize the transform.
> - You can test tf broadcasting by driving the robot using the keyboard or gamepad.
 
### 3.2. (30%) Drive HomeR in Figure 8s.
- (10%) Create a publisher running at 20 Hz, publish `Twist` message to the right topic to drive the robot making the Figure 8 pattern.
- (20%) The robot needs to traverse two circles at opposite directions, but maintain its angular speed at $\pi/4$ rad/s.
  - The ideal smaller circle is with radius of 0.5 m.  
  - The ideal bottom circle is with radius of 1 m, and the robot should be travelling in opposite direction on it.

> [!TIP]
> - Refer to [Assignment 2](https://classroom.github.com/a/a4Gqehwo).
> - You can either stuff the figure 8 driving to the transform broadcasting node, or create a separate node for it.

### 3.3. (20%) Construct package
- Create a package to host all your executables and make sure `ros2 run <package_name> <executable_name>` command is available after the package is built.
- (10% Bonus) Use one `ros2 launch <package_name> <launch_file_name>` command to launch everything  

### 3.4. (50% BONUS) Ground Demonstration
You can request a live demo to showoff your robot "painting" 8️⃣ figures on the ground.


## AI Policies
Please acknowledge AI's contributions according to the policies in the syllabus.
