# Mission 3

## Deployment Limit

In my ambiguous trial, the filter settled at about 13 seconds with a low covariance of 0.11, even though the cylinders look alike from many spots. In RViz the cloud didn't stay tight it expanded largely. A low number can look confident while being wrong, and my files don’t hold the true pose, so I can’t prove it was right. I could catch this by checking whether the scan lines up with the walls, watching for sudden pose jumps, or comparing with a second sensor. The fallback would be to stop and re-localize by turning in place or driving toward a distinctive feature. If localization is wrong, people near the robot, anyone relying on its deliveries or inspections, and staff who trust its position could be affected.

## Knowing Where

I would trust the robot’s position when several signs agree. The pose stays steady and moves smoothly as the robot drives. The particles bunch into one tight cluster, and the covariance is low. In my good run, it ended at 0.08, and the robot’s position stayed steady at the end. The red scan points also sit on the map walls, and the robot behaves as expected, with no sudden jumps. Covariance alone is not proof, because it is only the filter’s own belief.

## Recovery

In the good trial, the filter settled at about 17 seconds and ended with a low covariance of 0.08. In the incorrect trial, it took much longer to settle, about 92 seconds, and ended higher at 0.21. So it did recover, but slowly. In RViz, the cloud started spread out and the scan was off the walls, then the cloud tightened and the scan lined up slightly. Driving slowly toward the walls and corners helped because those views fit only one place on the map. Starting far off and driving fast would make recovery harder.

## Sensor Effect

The degraded run kept about 51% of the scan points. Its covariance ended at 0.23, almost three times the normal run’s 0.08, so the filter was less sure of itself with less data. It still settled at about 15 seconds, close to the normal run’s 17. Covariance is only the filter’s own estimate, not a guarantee of the true error. The robot could be more or less wrong than the number suggests, so I also check whether the scan lines up with the walls.
