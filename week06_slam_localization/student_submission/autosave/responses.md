# Week 6: SLAM and Localization

- name: Sheea McFarlane
- email: sheea.mcfarlane68@login.cuny.edu
- course_id: CSCI39536

## concepts.prediction

In a SLAM system, poor odometry can lead to the robot drifting its actual trajectory, resulting in inaccurate position estimates. This can be monitored using odom in ROS to visualize and plot pose changes over time, and comparisons with the robot's path can highlight discrepancies. Weak scan geometry shows as unstable localization due to unclear environment features, which can be assessed by examining the scan for noise and lack of detail in liDAR data and checking occupancy grid map for insufficient presentation.  

## final.course_reflection

This activity showed me that a robot’s position is a guess, and checking that guess is a big part of the work. I liked watching the particles and scan in RViz, because they made a hidden idea easy to see. It was also frustrating. Things failed to launch, and the checker kept saying “not yet.” I learned to read errors carefully and to ask what a system really measures. That made me want to keep working on robotics and software, because solving those problems felt good. I also see why technical work should connect to people. If a robot is wrong about where it is, people nearby or people who depend on it could get hurt. Engineers should test for failures, be honest about uncertainty, and add backups. What stood out most was that the best-looking score was not always the best choice. My second map scored higher but was worse for this job.

## final.synthesis

For this robot, knowing where it is means that many signs agree. Seeing an arrow on the screen is not enough. First, the robot needs a good map, because it can only match what the map shows. I tried two ways of mapping: walls first, and room by room. The room-by-room map scored higher (94.6 vs 82), but it had double walls, and the drift was never fixed when the robot came back to the start. That means there was no clear loop closure. So I used my first map, which had one clean outer wall. The starting pose also matters. In my good run, the robot settled in about 17 seconds and the covariance ended low, at 0.08. In my incorrect run, it took about 92 seconds to settle and ended at 0.21, so it recovered, but slowly. Sensor quality matters too. With half the scan points removed, the covariance rose from 0.08 to 0.23, so the robot was less sure. In the ambiguous area, the covariance was low (0.11) even though the cylinders look alike. A low number can still be wrong, because covariance is only the robot’s own belief, not the real error. So I trust the robot only when the pose is steady, the particles are tight, the scan lines up with the walls, and it acts as expected.

## mission_1.limitations

The cylinders in the lower part of the map were not mapped well. Their outlines are jagged and incomplete, with stray cells. The lidar only scans along a single flat plane, so each cylinder blocks the beam and leaves a hidden area behind it. I never circled them. I only passed them from two sides, so part of each cylinder was never seen directly. Also, when the laser hits a curved surface at a shallow angle, only a few noisy points come back, which gives rough edges instead of a clean circle.

## mission_1.map_interpretation

About 73% of the map was known (known fraction 0.73). The unknown 27% is mostly the empty corners of the map box outside the arena, which the lidar could never see. The speckle fraction was low (0.05), so the map has little noise, which suggests scan matching worked well. But there were 49 separate occupied pieces and the largest was only 179 cells, so the walls and obstacles are broken up instead of forming clean shapes. Border contact was 0.12, so some known space touches the edge of the map and the area may not be fully enclosed. The quality score of 82 is decent. I trust the high known fraction and low speckle most. I’m less sure about wall continuity and the edges, and the score alone doesn’t show where the problems are.

## mission_1.system_observation

At the start, the map was completely unknown. As I drove, /scan showed the laser hitting nearby walls and obstacles, and SLAM used those points to fill in free cells in white and occupied cells in black cells, so the map only grew where the robot could see. Odometry tracked the robot’s movement smoothly but slowly drifts. TF links the frames together, odometry moves odom -> base and SLAM adjusts map -> odom to correct the drift. One thing I saw while driving was that the walls got sharper when I passed them again. In RViz, the outer wall appeared as a thin, crisp black line with red scan points along it, while the cylinders in the middle looked rough and uneven.

## mission_2.comparison

Your prediction was fully supported because Strategy 2 drastically improved the circular shape of the top cylinders by scanning them from multiple directions, while simultaneously causing the predicted double-walls and severe boundary smearing on the right side due to postponed outer wall tracking and high odometric drift. You can also see that that is less unknown space inside than before.

## mission_2.loop_closure

I cannot claim a successful loop closure occurred in Strategy 2 because the clear presence of ghosting, parallel double-walls, and elongated cylinders on the lower half of the map proves that the SLAM algorithm failed to correct the accumulated coordinate drift when the robot returned to its initial frame. To distinguish a true loop closure from ordinary map growth, look for a sudden, dramatic "snap" where previously misaligned or blurry map sections instantly realign and sharpen, accompanied by a sharp jump in the map -> odom transform log rather than continuous, incremental pixel additions.

## mission_2.strategy_prediction

Strategy 1 focuses on the perimeter first, creating smooth outer walls and allowing early loop closure to fix sensor drift, though it leaves interior cylinders ragged and shadowed due to limited viewing angles. In contrast, Strategy 2 uses interior lane sweeps to weave between the cylinders first, which drastically improves internal coverage and creates crisp, complete cylinder shapes by scanning them from multiple directions. However, by postponing the outer wall mapping and delayed return to the starting point, Strategy 2 risks higher accumulation of odometric drift before SLAM can execute a loop closure.

## mission_3.deployment_limit

In my ambiguous trial, the filter settled at about 13 seconds with a low covariance of 0.11, even though the cylinders look alike from many spots. In RViz the cloud didn't stay tight it expanded largely. A low number can look confident while being wrong, and my files don’t hold the true pose, so I can’t prove it was right. I could catch this by checking whether the scan lines up with the walls, watching for sudden pose jumps, or comparing with a second sensor. The fallback would be to stop and re-localize by turning in place or driving toward a distinctive feature. If localization is wrong, people near the robot, anyone relying on its deliveries or inspections, and staff who trust its position could be affected.

## mission_3.knowing_where

I would trust the robot’s position when several signs agree. The pose stays steady and moves smoothly as the robot drives. The particles bunch into one tight cluster, and the covariance is low. In my good run, it ended at 0.08, and the robot’s position stayed steady at the end. The red scan points also sit on the map walls, and the robot behaves as expected, with no sudden jumps. Covariance alone is not proof, because it is only the filter’s own belief.

## mission_3.recovery

In the good trial, the filter settled at about 17 seconds and ended with a low covariance of 0.08. In the incorrect trial, it took much longer to settle, about 92 seconds, and ended higher at 0.21. So it did recover, but slowly. In RViz, the cloud started spread out and the scan was off the walls, then the cloud tightened and the scan lined up slightly. Driving slowly toward the walls and corners helped because those views fit only one place on the map. Starting far off and driving fast would make recovery harder.

## mission_3.sensor_effect

The degraded run kept about 51% of the scan points. Its covariance ended at 0.23, almost three times the normal run’s 0.08, so the filter was less sure of itself with less data. It still settled at about 15 seconds, close to the normal run’s 17. Covariance is only the filter’s own estimate, not a guarantee of the true error. The robot could be more or less wrong than the number suggests, so I also check whether the scan lines up with the walls.
