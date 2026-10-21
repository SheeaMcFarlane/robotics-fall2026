# Mission 2

## Comparison

Your prediction was fully supported because Strategy 2 drastically improved the circular shape of the top cylinders by scanning them from multiple directions, while simultaneously causing the predicted double-walls and severe boundary smearing on the right side due to postponed outer wall tracking and high odometric drift. You can also see that that is less unknown space inside than before.

## Loop Closure

I cannot claim a successful loop closure occurred in Strategy 2 because the clear presence of ghosting, parallel double-walls, and elongated cylinders on the lower half of the map proves that the SLAM algorithm failed to correct the accumulated coordinate drift when the robot returned to its initial frame. To distinguish a true loop closure from ordinary map growth, look for a sudden, dramatic "snap" where previously misaligned or blurry map sections instantly realign and sharpen, accompanied by a sharp jump in the map -> odom transform log rather than continuous, incremental pixel additions.

## Strategy Prediction

Strategy 1 focuses on the perimeter first, creating smooth outer walls and allowing early loop closure to fix sensor drift, though it leaves interior cylinders ragged and shadowed due to limited viewing angles. In contrast, Strategy 2 uses interior lane sweeps to weave between the cylinders first, which drastically improves internal coverage and creates crisp, complete cylinder shapes by scanning them from multiple directions. However, by postponing the outer wall mapping and delayed return to the starting point, Strategy 2 risks higher accumulation of odometric drift before SLAM can execute a loop closure.
