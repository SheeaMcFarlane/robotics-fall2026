# Mission 1

## bias

0.010

## bias_vs_variance

My predication was correct for the most part. The stats show that the bias is as low as +0.010 m, with a mean of 2.010 which is close to the target 2.00m.  This shows that the sensor does not consistently measure too high or  too low. The variance of 0.0367 m^2 shows that the readings have some noise and are not always consistent. The bias measure how far the average reading is from the target, while variance measures how spread out the readings are. So a sensor can have low bias but still have noisy readings.

## dropouts

3

## mean

2.010

## median

1.990

## more_samples

More samples would not remove the sensor's main problem because the readings are noisy and inconsistent. Although more samples could make the average more reliable , more samples would not eliminate the variance, outliers, or dropouts. In order for it to produces more consistent and reliable measurements the sensor would need improvements. 

## outliers

4

## prediction

For biased sensor, the readings will be tightly grouped together but progressively shift away from the target. This would result in a high bias, a mean that is significantly different from 2.00 m, and a low variance. However for a noisy sensor the readings will be scattered and unstable, fluctuating randomly both above and below the target. This will result in low bias, a mean that's really close to 2.00m and high variance.

## prediction_draft

For biased sensor, the readings will be tightly grouped together but progressively shift away from the target. This would result in a high bias, a mean that is significantly different from 2.00 m, and a low variance. However for a noisy sensor the readings will be scattered and unstable, fluctuating randomly both above and below the target. This will result in low bias, a mean that's really close to 2.00m and high variance.


## profile

noisy

## robot_consequence

One robot decision this imperfection could change is how close the robot gets to a pedestrian. Noisy readings or outliers could make the robot misjudge the distance and can cause to get too close to the person. This could put the pedestrian at risk of being hit and because the robot needs to move safely it needs a more reliable sensor.

## variance

0.0367
