# Mission 3

## Data To Command

The front_distance finds the closet valid LiDAR reading in front of the robot and decide_velocity() uses that distance to decide if the robot to move or stop.

## Missing Data Safety

The robot stops when there is no valid front measurement instead of treating the path as clear because we cannot know if the path is safe. It is safer to stop than risk hitting something.

## System Layers

The LiDar gives the distance, the functions decide the speed, and the ROS node and guard help make sure the robot stops safely when needed.
