# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Sheea McFarlane
- Email: sheea.mcfarlane68@login.cuny.edu

## final.architecture_evidence

It reacts to the current LiDar information. A hybrid system would have to add planning or memory.

## final.course_reflection

This activity made me more interested in robotics but also showed me how I need to pay close attention to details. this activity also helped me learn how ROS 2 helps different parts of the robot communicate / building off of each other.

## final.hardware_next

I would test different obstacles, sensor problems, and speeds.

## final.middleware_debugging

I would check if the nodes and the topics are connected correctly.

## final.system_synthesis

Robotics is difficult because many parts have to work together, they have to be able to work together cohesively. The robot has sensor, code, communication, and safely systems. If one part has a problem, it can affect the robot. The architecture that is used is a reactive architecture which allows robot to react to what the LiDAr sees. The robot makes a decision based on the current LiDAR reading. The advantage is that it is simple and responds quickly. However, it cannot plan ahead or remember what happened before. The front_distance() finds the closet valid distance in front of the robot and decide_velocity decides if the robot should move or stop. he benefit is that it is simple and fast. The downside is that it does not plan ahead. ROS 2 connects different part, Lidar sends information through /scan, obstacle_guard node receives the LiDAR information and uses my two functions, it then sends the speed through /student_cmd_vel. The command guard helps prevent unsafe movement. This gives the system several connected parts working together. Sensor problems can also affects dafety, if the LiDAr give no valid front measurement then the robot stops (If there is no valid measurement in front of the robot, my program returns 0.0 ) instead of assuming the path is clear which is safer. The command guard is another layer that can restrict unsafe movement. Overall, this activity showed me that robotics is not just about making a robot move. The software also needs to communicate correctly and handle problems safely.Overall, this activity showed me that robotics requires more than just writing code that works. The different software components must communicate correctly, handle unexpected situations, and include safety controls. This activity also showed me how important testing is in robotics. Even when the code works, the robot still needs to be tested in different situations to make sure it is safe. Small problems with sensors, timing, or communication can change how the robot behaves. This is why safety and testing are important parts of robotics.

## final.timing_evidence

The robot stops when the sensor gives bad or missing information.

## mission_1.command_path_explanation

A Proposed command travels on /student_cmd_vel to serve as a check before moving along to the robot. The guard node gets this message and reviews it and is then forwarded to /cmd_vel, where it can then be safely read by /ros_gz_bridge. The separation is the key to keeping it safe.

## mission_1.graph_explanation

A ROS 2 graph shows running components and their communications. One of these nodes is a subscriber node that receives messages from a publisher node.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

In the laser scan values I found the range min and max values, the min value being the the minimum distance the laser can detect and the max being the max distance I can detect. 

## mission_1.tools_explanation

Gazebo is responsible for calculating the virtual world's physics while RViz is responsible for displaying the information collected.

## mission_2.measurement_explanation

In the curve trail, the estimated traveled time and start to end distance described different measurements because they are measuring the distance two different ways, one is measuring the length of the actual trajectory and the other measuring the shortest line from the start point to the end point.

## mission_2.modified_settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## mission_2.motion_comparison

The measured motion compared to my prediction isn't far off, my prediction being 0.45 and the actual measurement being 0.413. Unlike my prediction the estimated calculation compared to the actual distance traveled is perfectly accurate, 0.413 being the measurement for both. 

## mission_2.prediction_locks

{'straight': '2026-09-11T23:54:20.245583+00:00', 'rotation': '2026-09-12T00:12:05.312446+00:00', 'curve': '2026-09-12T00:18:14.985303+00:00', 'curve_modified': '2026-09-12T00:22:35.655688+00:00'}

## mission_2.predictions

{'straight': 'I predict the robot will travel 0.45m from the starting point.', 'rotation': "I predict its position will be the same while it's direction will be 1.50rad to the left of the current direction. ", 'curve': "I predict a curve because it's turning to the right 0.6m and moving forward 1.6rad ", 'curve_modified': 'This curve should be tighter, wider, or turn the other way because the turning speed is positive and the forward speed is positive.'}

## mission_2.safety_explanation

The command guard checks for and blocks unsafe or invalid speeds. The final zero command stops the robot at the end of trail. The timeout is needed if it loses connection for 0.5s. 

## mission_3.data_to_command

The front_distance finds the closet valid LiDAR reading in front of the robot and decide_velocity() uses that distance to decide if the robot to move or stop.

## mission_3.missing_data_safety

The robot stops when there is no valid front measurement instead of treating the path as clear because we cannot know if the path is safe. It is safer to stop than risk hitting something.

## mission_3.system_layers

The LiDar gives the distance, the functions decide the speed, and the ROS node and guard help make sure the robot stops safely when needed.

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
