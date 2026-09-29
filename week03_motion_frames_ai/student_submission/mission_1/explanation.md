# Mission 1

## Predictions

{'straight': {'x': 0.45, 'y': 0.0, 'theta': 0.0}, 'turn_then_drive': {'x': 0.0, 'y': 0.3, 'theta': 1.57}, 'arc': {'x': 0.37, 'y': 0.39, 'theta': 1.6}}

## Model Vs Observation

The observed motion did not match the model at all. The model predicted a movement to destination but the observed motion was basically still.

## Largest Error

The sequence with the largest discrepancy is straight. The model prediction shows that the pose would be at (0.45m,0, 0.0 RAD) but the observation was still (0,0,0). The robot failed to execute its primary objective of forward translation therefore missing it destination target.

## Error Source

It seems model/ timing error is when the computer sends bad commands resulting int the robot moving wrongly, while localization error the robot does movement but it wasn't tracked/ processed by computer

## Twice Distance

If the robot drove twice as long at the same straight velocity it would produce the same error.

## Predictions Locked At

2026-09-17T16:43:12.757821+00:00
