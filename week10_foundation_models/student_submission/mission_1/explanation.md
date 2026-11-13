# mission_1 explanations

## case_analysis

For spill_cleanup plan, the first invalid assumption happens at step 2, this is where the model assumes the robot has a vacuum action. It isn’t in the robot’s capability list, and a vacuum is also the wrong tool for a liquid spill. The downstream consequence is that the plan can’t run past step 2. Because report_complete() has no check before it, a naive executor could report the spill cleaned when nothing was done. For medication plan, the first invalid assumption is at step 1. The plan picks up pill_bottle_a without moving to the tray, and it assumes the pills on the tray are pill_bottle_a without ever verifying that. The downstream consequence is that the robot may fail to pick anything up, or may pick the wrong item. Step 3 then calls administer_medication, which doesn’t exist. If the system substituted a similar action, the robot could give Jordan unverified medication, which is a safety problem.

## executable_vs_reasonable

Syntactically executable, grounded, reasonable and safe are different claims because a plan is syntactically executable when every action is a valid command the robot can parse and run, which says nothing about the world; it is grounded when the objects, places, and people it names exist in the known world and match the request (ambiguous_cup is executable but ungrounded, since “the cup” became red_cup with nothing to justify that choice), it is reasonable when its steps make sense in order and would achieve the goal (a grounded plan can still pick before moving or skip a needed check), and it is safe when running it won’t cause harm, which can fail even for a plan that passes the other three, such as handing medication to the wrong person, so safety needs explicit constraints and often a human authorization step.

## better_interface

For world state the model needs the objects present and where they are (which cups, what’s on the tray, what’s in the supply room), plus which doors are locked and which hallways are blocked. For capabilities it needs an explicit list of what the robot can actually do, so the model can’t invent unlock, vacuum or administer_medication. Where a needed capability is missing, it should say so rather than make one up. And lastly for clarification interface it needs a way to ask “which cup?” or “who authorizes this medication?” instead of guessing. It should also refuse or escalate for tasks like medication that need human approval.
