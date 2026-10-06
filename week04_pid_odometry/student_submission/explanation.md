# PID and Odometry Lab -- Full Submission

- Name: Sheea McFarlane
- Student ID: 24292168
- Section: 01

## Check-ins

### background_compare

When designing a PID controller it is important for the engineer to keep in mind gains in Ki, Kp, and Kd. These values are important because they help with shaping how the controller reacts to things like errors, accumulated drift, etc.

### background_social

In terms of a car brakes, if it is tuned too aggressively then the wheels could potentially lock up and result into a potential car flip etc. If the brakes are tuned too cautiously then the brakes might not respond when you need it to, the response might also be delayed and this can result into the car crashing into something or someone.

### pid_playground_terms

The P term reacted first because it responds to the current error. The I term eliminated the final gap by correcting the remaining error over time.

### odom_background_wheels

It turns left because dR is 6cm and dL is 0cm so dTheta is 0.50 rad which approximately 28.6 degrees.

### m1_prediction

Too little Kp would make the arm move too slowly toward the target and may not reach or hold the target well and too little Kd would make the arm less controlled, so it may overshoot the target or keep moving back and forth before settling.

### m1_arm_tuning

For the shoulder and the elbow controllers to make the arm settle cleanly i changed al three K values, each played their own role but most importantly the Ki and the Kp had the most impact on the robot arm. While it might have not been needed the Kd by adjusting the Kd slightly I was able to fix the shaking and overshooting which allowed the arm to settle more smoothly and land closer to the target.

### m2_prediction

If the forward pod scale is too large then the robot's estimated forward distance will be too high. If the strafe pod scale is too small then the robot's estimated sideways distance will be too low.

### m2_analysis

My prediction was mostly correct. The forward pod measured forward movement, and the strafe pod measured sideways movement. The sideways pod is needed because the robot can move sideways. Some drift can remain because of small measurement errors. The test passed with a maximum error of 1.76 inches, which was under 3 inches.

### m3_prediction

Increasing forward speed could increase tracking error because the robot has less time to correct its path. Using too little derivative control could also cause more overshooting and oscillation around the desired path. Both could reduce pedestrian clearance because the robot may have a harder time stopping or correcting its direction quickly near a pedestrian.

### m3_technical

My prediction was correct. The robot uses its estimated pose to compare its current heading to the direction of the next route point. The PID calculates the heading error and turns it into a steering command so the robot can adjust its direction and follow the path. If the wheel radius is inaccurate, the robot gets incorrect distance measurements and its estimated position will not match its actual position, so even a well-tuned PID can follow the wrong physical path.

### m3_human

The most dangerous failure is the robot hitting a pedestrian. I would keep a 2.5–3 foot safety distance, even if it makes the robot slower. The engineer, company, and operator are responsible for making sure the robot is safe before it is used.

### final_reflection

I learned that small changes to the PID settings, wheel size, speed, and many other settings can easily change the robots movements . While some changes can impact the robot more than others, testing is very important to maintain and guarantee proper functionality. I enjoyed testing the robot and seeing how change impacted the robots movements. I also learned that safety should be more important than speed. Making the robot faster can save time, but it can also cause more drifting or mistakes. Slowing the robot down and keeping more space around people can make it safer. Overall, this activity showed me that robotics is not just about writing code. You also have to test the robot, understand how changes affect it, and make sure it is safe for people. Overall, this activity reiterates to me that robotics is not just about writing code. You also have to test the robot, understand how changes affect it, and make sure it is safe for people.

## Mission Explanations

### mission_1

**prediction**: Too little Kp would make the arm move too slowly toward the target and may not reach or hold the target well and too little Kd would make the arm less controlled, so it may overshoot the target or keep moving back and forth before settling.

**tuning_analysis**: For the shoulder and the elbow controllers to make the arm settle cleanly i changed al three K values, each played their own role but most importantly the Ki and the Kp had the most impact on the robot arm. While it might have not been needed the Kd by adjusting the Kd slightly I was able to fix the shaking and overshooting which allowed the arm to settle more smoothly and land closer to the target.

### mission_2

**prediction**: If the forward pod scale is too large then the robot's estimated forward distance will be too high. If the strafe pod scale is too small then the robot's estimated sideways distance will be too low.

**calibration_analysis**: My prediction was mostly correct. The forward pod measured forward movement, and the strafe pod measured sideways movement. The sideways pod is needed because the robot can move sideways. Some drift can remain because of small measurement errors. The test passed with a maximum error of 1.76 inches, which was under 3 inches.

### mission_3

**technical_analysis**: My prediction was correct. The robot uses its estimated pose to compare its current heading to the direction of the next route point. The PID calculates the heading error and turns it into a steering command so the robot can adjust its direction and follow the path. If the wheel radius is inaccurate, the robot gets incorrect distance measurements and its estimated position will not match its actual position, so even a well-tuned PID can follow the wrong physical path.

**human_centered_analysis**: The most dangerous failure is the robot hitting a pedestrian. I would keep a 2.5–3 foot safety distance, even if it makes the robot slower. The engineer, company, and operator are responsible for making sure the robot is safe before it is used.
