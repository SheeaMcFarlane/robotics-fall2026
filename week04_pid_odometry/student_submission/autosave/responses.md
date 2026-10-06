# Autosaved responses

- Name: (not provided)
- Student ID: (not provided)
- Section: (not provided)

## Check-in answers

### m2_drift

The forward pod scale changed how far the robot estimated it moved forward and the strafe pod scale changed how the robot estimated it moved sideways.

### m2_turning

A holonomic robot needs a sideways odometry pod because it can move sideways and the pod will be measuring that sideways movement so the robot can keep track of its position accurately.

## Mission explanations

### mission_2

**calibration**: After watching the original estimated I noticed the forward pod's estimate was further than where the robot stopped and the strafe pod estimate was earlier than where the robot stopped. To find the right estimate i slowly decreased the forward in/tick and slowly increased the  strafe in/tick and tested it with each increase and decrease.

**drift**: Odometry can still drift even after calibration because of wheel slipping, measurement errors even if it's a really small error, uneven floors, or changes in the robot’s movement. These small errors can add up over time and make the estimated position different from the robot’s actual position.
