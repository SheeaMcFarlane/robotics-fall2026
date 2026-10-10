# Week 5: Sensors, Noise, and Uncertainty

- course_id: CSCI 39536 01
- email: sheea.mcfarlane68@login.cuny.edu
- name: Sheea McFarlane

## concepts.observation

The changes that occurs when there was an increase in versus bias are increases in variance, decrease in standard_deviation, and a decrease in outliers. 

## final.course_reflection

Connecting technical work with human values ensures that technology helps people instead of harming them. When developers focus only on code, they can accidentally create systems that spread bias, leak data, or leave people out. Building technology with ethics in mind creates safer, fairer tools that people can actually trust.

## final.synthesis

Our three experimental missions demonstrate how raw sensor measurements, algorithmic estimation choices, and deployment contexts must be carefully engineered together. In Mission 1, we established that Sensor A provides fast but noisy, outlier-prone updates, whereas Sensor B is steady but heavily biased and structurally delayed, sampling only every fourth time step. To handle these distinct measurement properties, Mission 2 evaluated estimation choices. We calculated that a tight window of three valid readings bounds the response delay, while a median filter mathematically isolates extreme outliers while a moving average fails by incorporating the noise. Furthermore, our experiments proved that a balanced fusion weight of 0.25 on Sensor A minimizes total system error. It leverages Sensor A to dynamically fill in Sensor B's slow timing gaps while relying on Sensor B's stability to suppress Sensor A’s rapid fluctuations. Finally, Mission 3 proved that these algorithmic choices must adapt to the deployment context. In a tight industrial warehouse, the goal is productivity/ flow rate. The baseline policy utilized a 0.75 m threshold with a tight 0.10 m caution margin to keep traffic moving efficiently, tolerating a small 0.05 s delay while using a reading confirmation of 2 to eliminate false stops from factory noise. Conversely, an assistive wheelchair deployment prioritizes human passenger safety above all else.

## mission_1.bias

0.010

## mission_1.bias_vs_variance

My predication was correct for the most part. The stats show that the bias is as low as +0.010 m, with a mean of 2.010 which is close to the target 2.00m.  This shows that the sensor does not consistently measure too high or  too low. The variance of 0.0367 m^2 shows that the readings have some noise and are not always consistent. The bias measure how far the average reading is from the target, while variance measures how spread out the readings are. So a sensor can have low bias but still have noisy readings.

## mission_1.dropouts

3

## mission_1.mean

2.010

## mission_1.median

1.990

## mission_1.more_samples

More samples would not remove the sensor's main problem because the readings are noisy and inconsistent. Although more samples could make the average more reliable , more samples would not eliminate the variance, outliers, or dropouts. In order for it to produces more consistent and reliable measurements the sensor would need improvements. 

## mission_1.outliers

4

## mission_1.prediction

For biased sensor, the readings will be tightly grouped together but progressively shift away from the target. This would result in a high bias, a mean that is significantly different from 2.00 m, and a low variance. However for a noisy sensor the readings will be scattered and unstable, fluctuating randomly both above and below the target. This will result in low bias, a mean that's really close to 2.00m and high variance.

## mission_1.prediction_draft

For biased sensor, the readings will be tightly grouped together but progressively shift away from the target. This would result in a high bias, a mean that is significantly different from 2.00 m, and a low variance. However for a noisy sensor the readings will be scattered and unstable, fluctuating randomly both above and below the target. This will result in low bias, a mean that's really close to 2.00m and high variance.


## mission_1.profile

noisy

## mission_1.robot_consequence

One robot decision this imperfection could change is how close the robot gets to a pedestrian. Noisy readings or outliers could make the robot misjudge the distance and can cause to get too close to the person. This could put the pedestrian at risk of being hit and because the robot needs to move safely it needs a more reliable sensor.

## mission_1.variance

0.0367

## mission_2.comparison

Increasing the moving average window size from 3 to 7 and then 11 actually causes the MAE to drop slightly from 0.0668 to 0.0644 then going up to 0.0650, while the response delay slightly increases from 1.25 to 1.3 steps. A matched pair of a window 3 moving average against a window 3 median filter at a fixed 0.25 weight, the median filter provides a lower RMSE of 0.1330 compared to the moving average's 0.13303, this shows it handles extreme deviations a little better. However, this outlier protection comes with a give and take, as the median filter increases the response delay to 1.55 steps, making it slower than the moving average's 1.25 steps.

## mission_2.fusion_choice

Increasing the weight on Sensor A from 0.25 to 0.75 steadily raises the MAE from 0.0646 to 0.0851, proving that the 0.25 weight is the best choice. This setup keeps errors at their lowest point because it heavily relies on the steadier Sensor B to suppress Sensor A's extreme noise. At the same time, it uses just enough of Sensor A to fill in the gaps between Sensor B's slow updates, keeping the overall response delay at a manageable 1.55 steps.

## mission_2.manual_average

4.17

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

Window 3 with Weight A = 0.75 reacts the fastest to true changes but suffers from the most noise and spike leakage because it relies heavily on Sensor A.

## mission_2.responsiveness

Heavy smoothing cuts down noise but creates a response delay, such as the peak lag of 1.55 steps seen in the median filter. For a person nearby, this means a robotic arm or automated vehicle becomes temporarily blind to their sudden movements. Because the machine continues to move based on old data, this tracking lag creates a high risk of a dangerous physical collision.

## mission_2.selected

0

## mission_3.Assistive.prediction_draft

This setup will be challenged by crowded spaces, causing frequent unnecessary stops while keeping reaction delay at zero. Because it triggers a stop on just 1 bad reading, it halts instantly at the very first sign of danger to maximize pedestrian safety. Compared to a long, slow moving average policy, this setup completely eliminates lag but will cause the wheelchair to frequently stutter or freeze when trying to pass close to people.

## mission_3.Warehouse.prediction_draft

This setup will be challenged by Sensor A's sudden noise spikes, causing frequent unnecessary stops while keeping reaction delay at zero. Because it triggers a stop on just 1 bad reading, any single unfiltered spike that slips past the filter causes a false alarm. Compared to a heavily smoothed policy, this completely eliminates tracking lag but will cause the machinery to freeze or stutter unnecessarily in noisy factory settings.

## mission_3.context_comparison

The two final policies differ by changing the safety margins and confirmation steps to fit their environments. The warehouse uses a tight 0.10 m margin and requires 2 readings to prevent false stops in cramped aisles. The assistive robot policy scales up to a wide 0.40 m margin and an instant reading(1) trigger. This difference means the robot prioritizes human life over smooth movement, instantly halting the machine at the first sign of danger to drop detection delay to 0.0 s so it or it's beneficiary never hits an obstacle.

## mission_3.error_costs

In the warehouse, the business owner bears the financial cost of unnecessary stops from stalled operations, while workers bear the injury costs of false-safes. In the assistive setting, the beneficiary bears the minor annoyance of an unnecessary stop, while nearby pedestrians bear the severe injury costs of a false-safe collision. Upgrading the warehouse policy cut dangerous commands from 2 to 0 while keeping unnecessary stops at 0% and delay at 0.15 s. Upgrading the assistive policy dropped dangerous commands from 2 to 0 and cut reaction lag from a slow 0.35 s down to an instant 0.0 s.

## mission_3.limitations

These seven tests establish that the system handles single sensor noise spikes, sudden data drops, and completely missing signals safely. They do not establish how the hardware will perform during continuous real-world issues like physical lens smudges, blinding sunlight, or thick dust clouds that cause long-term sensor blockages. Before deployment, you should consult a Safety Engineer and run an additional high-velocity braking test to ensure the physical machine can actually stop in time when a person appears suddenly at max speed.
