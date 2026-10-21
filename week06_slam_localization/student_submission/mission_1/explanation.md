# Mission 1

## Limitations

The cylinders in the lower part of the map were not mapped well. Their outlines are jagged and incomplete, with stray cells. The lidar only scans along a single flat plane, so each cylinder blocks the beam and leaves a hidden area behind it. I never circled them. I only passed them from two sides, so part of each cylinder was never seen directly. Also, when the laser hits a curved surface at a shallow angle, only a few noisy points come back, which gives rough edges instead of a clean circle.

## Map Interpretation

About 73% of the map was known (known fraction 0.73). The unknown 27% is mostly the empty corners of the map box outside the arena, which the lidar could never see. The speckle fraction was low (0.05), so the map has little noise, which suggests scan matching worked well. But there were 49 separate occupied pieces and the largest was only 179 cells, so the walls and obstacles are broken up instead of forming clean shapes. Border contact was 0.12, so some known space touches the edge of the map and the area may not be fully enclosed. The quality score of 82 is decent. I trust the high known fraction and low speckle most. I’m less sure about wall continuity and the edges, and the score alone doesn’t show where the problems are.

## System Observation

At the start, the map was completely unknown. As I drove, /scan showed the laser hitting nearby walls and obstacles, and SLAM used those points to fill in free cells in white and occupied cells in black cells, so the map only grew where the robot could see. Odometry tracked the robot’s movement smoothly but slowly drifts. TF links the frames together, odometry moves odom -> base and SLAM adjusts map -> odom to correct the drift. One thing I saw while driving was that the walls got sharper when I passed them again. In RViz, the outer wall appeared as a thin, crisp black line with red scan points along it, while the cylinders in the middle looked rough and uneven.
