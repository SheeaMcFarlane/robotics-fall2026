# Mission 3

## Assistive.prediction_draft

This setup will be challenged by crowded spaces, causing frequent unnecessary stops while keeping reaction delay at zero. Because it triggers a stop on just 1 bad reading, it halts instantly at the very first sign of danger to maximize pedestrian safety. Compared to a long, slow moving average policy, this setup completely eliminates lag but will cause the wheelchair to frequently stutter or freeze when trying to pass close to people.

## Warehouse.prediction_draft

This setup will be challenged by Sensor A's sudden noise spikes, causing frequent unnecessary stops while keeping reaction delay at zero. Because it triggers a stop on just 1 bad reading, any single unfiltered spike that slips past the filter causes a false alarm. Compared to a heavily smoothed policy, this completely eliminates tracking lag but will cause the machinery to freeze or stutter unnecessarily in noisy factory settings.

## context_comparison

The two final policies differ by changing the safety margins and confirmation steps to fit their environments. The warehouse uses a tight 0.10 m margin and requires 2 readings to prevent false stops in cramped aisles. The assistive robot policy scales up to a wide 0.40 m margin and an instant reading(1) trigger. This difference means the robot prioritizes human life over smooth movement, instantly halting the machine at the first sign of danger to drop detection delay to 0.0 s so it or it's beneficiary never hits an obstacle.

## error_costs

In the warehouse, the business owner bears the financial cost of unnecessary stops from stalled operations, while workers bear the injury costs of false-safes. In the assistive setting, the beneficiary bears the minor annoyance of an unnecessary stop, while nearby pedestrians bear the severe injury costs of a false-safe collision. Upgrading the warehouse policy cut dangerous commands from 2 to 0 while keeping unnecessary stops at 0% and delay at 0.15 s. Upgrading the assistive policy dropped dangerous commands from 2 to 0 and cut reaction lag from a slow 0.35 s down to an instant 0.0 s.

## limitations

These seven tests establish that the system handles single sensor noise spikes, sudden data drops, and completely missing signals safely. They do not establish how the hardware will perform during continuous real-world issues like physical lens smudges, blinding sunlight, or thick dust clouds that cause long-term sensor blockages. Before deployment, you should consult a Safety Engineer and run an additional high-velocity braking test to ensure the physical machine can actually stop in time when a person appears suddenly at max speed.
