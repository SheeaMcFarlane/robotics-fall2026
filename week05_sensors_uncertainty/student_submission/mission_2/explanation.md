# Mission 2

## comparison

Increasing the moving average window size from 3 to 7 and then 11 actually causes the MAE to drop slightly from 0.0668 to 0.0644 then going up to 0.0650, while the response delay slightly increases from 1.25 to 1.3 steps. A matched pair of a window 3 moving average against a window 3 median filter at a fixed 0.25 weight, the median filter provides a lower RMSE of 0.1330 compared to the moving average's 0.13303, this shows it handles extreme deviations a little better. However, this outlier protection comes with a give and take, as the median filter increases the response delay to 1.55 steps, making it slower than the moving average's 1.25 steps.

## fusion_choice

Increasing the weight on Sensor A from 0.25 to 0.75 steadily raises the MAE from 0.0646 to 0.0851, proving that the 0.25 weight is the best choice. This setup keeps errors at their lowest point because it heavily relies on the steadier Sensor B to suppress Sensor A's extreme noise. At the same time, it uses just enough of Sensor A to fill in the gaps between Sensor B's slow updates, keeping the overall response delay at a manageable 1.55 steps.

## manual_average

4.17

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

Window 3 with Weight A = 0.75 reacts the fastest to true changes but suffers from the most noise and spike leakage because it relies heavily on Sensor A.

## responsiveness

Heavy smoothing cuts down noise but creates a response delay, such as the peak lag of 1.55 steps seen in the median filter. For a person nearby, this means a robotic arm or automated vehicle becomes temporarily blind to their sudden movements. Because the machine continues to move based on old data, this tracking lag creates a high risk of a dangerous physical collision.

## selected

0
