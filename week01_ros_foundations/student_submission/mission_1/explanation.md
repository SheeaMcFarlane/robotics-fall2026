# Mission 1

## Command Path Explanation

A Proposed command travels on /student_cmd_vel to serve as a check before moving along to the robot. The guard node gets this message and reviews it and is then forwarded to /cmd_vel, where it can then be safely read by /ros_gz_bridge. The separation is the key to keeping it safe.

## Graph Explanation

A ROS 2 graph shows running components and their communications. One of these nodes is a subscriber node that receives messages from a publisher node.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

In the laser scan values I found the range min and max values, the min value being the the minimum distance the laser can detect and the max being the max distance I can detect. 

## Tools Explanation

Gazebo is responsible for calculating the virtual world's physics while RViz is responsible for displaying the information collected.
