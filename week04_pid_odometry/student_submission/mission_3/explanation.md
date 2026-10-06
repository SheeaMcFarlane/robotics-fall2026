# mission_3 Submission

- Name: Sheea McFarlane
- Section: 01

## Explanations

### heading

It compares where the robot is facing to where the goal point is. The PID uses that difference to tell the robot how much it need to turn to reach it's target.


### integration

Because the robot is using incorrect position information. Even with good PID settings, bad odometry can make the robot think it is somewhere completely different from it's current position.
