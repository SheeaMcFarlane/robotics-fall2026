# mission_3 Submission

- Name: Sheea McFarlane
- Section: 01

## Explanations

### technical_analysis

My prediction was correct. The robot uses its estimated pose to compare its current heading to the direction of the next route point. The PID calculates the heading error and turns it into a steering command so the robot can adjust its direction and follow the path. If the wheel radius is inaccurate, the robot gets incorrect distance measurements and its estimated position will not match its actual position, so even a well-tuned PID can follow the wrong physical path.

### human_centered_analysis

The most dangerous failure is the robot hitting a pedestrian. I would keep a 2.5–3 foot safety distance, even if it makes the robot slower. The engineer, company, and operator are responsible for making sure the robot is safe before it is used.