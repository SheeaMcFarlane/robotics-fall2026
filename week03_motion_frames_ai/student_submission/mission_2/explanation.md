# Mission 2

## Diagnostics

{'stale': 'Transform unavailable at the requested time', 'typo': 'Unknown frame name', 'wrong_source': 'Point interpreted in the wrong source frame'}

## Fixed Meaning

The odom is fixed to odometry estimates that are based on the movements the robot make over time, base_link is fixed to the current positions and movements, and base_scan is fixed to the sensor .

## Map Absent

The reason why no map frame might exist in this lab because there is no movement actually occurring. Since there is no movement code being executed it can not collet any real time data necessary for generating a map frame. 

## Moving Coordinates

When the robot moves the coordinates or the base_link changes increasing or decreasing based on the robot's movements in the base_link frame.

## Point Answers

{'sensor_point_in_base': {'x': 0.97, 'y': 0.0}, 'sensor_point_in_odom': {'x': 0.97, 'y': 0.0}}

## Relationships

{'base_to_sensor': 'base_link → base_scan', 'map_role': 'Global frame corrected by localization or SLAM', 'odom_to_base': 'odom → base_link'}

## Sensor Offset

Software must know the sensor's mounting transform in order for it to properly interpret the data and provide the most accurate localization.
