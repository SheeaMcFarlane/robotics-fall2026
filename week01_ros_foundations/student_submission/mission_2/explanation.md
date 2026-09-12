# Mission 2

## Measurement Explanation

In the curve trail, the estimated traveled time and start to end distance described different measurements because they are measuring the distance two different ways, one is measuring the length of the actual trajectory and the other measuring the shortest line from the start point to the end point.

## Motion Comparison

The measured motion compared to my prediction isn't far off, my prediction being 0.45 and the actual measurement being 0.413. Unlike my prediction the estimated calculation compared to the actual distance traveled is perfectly accurate, 0.413 being the measurement for both. 

## Prediction Locks

{'straight': '2026-09-11T23:54:20.245583+00:00', 'rotation': '2026-09-12T00:12:05.312446+00:00', 'curve': '2026-09-12T00:18:14.985303+00:00', 'curve_modified': '2026-09-12T00:22:35.655688+00:00'}

## Predictions

{'straight': 'I predict the robot will travel 0.45m from the starting point.', 'rotation': "I predict its position will be the same while it's direction will be 1.50rad to the left of the current direction. ", 'curve': "I predict a curve because it's turning to the right 0.6m and moving forward 1.6rad ", 'curve_modified': 'This curve should be tighter, wider, or turn the other way because the turning speed is positive and the forward speed is positive.'}

## Safety Explanation

The command guard checks for and blocks unsafe or invalid speeds. The final zero command stops the robot at the end of trail. The timeout is needed if it loses connection for 0.5s. 

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}
