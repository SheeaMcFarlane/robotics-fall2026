# Week 10: Foundation Models for Robotics responses

- Name: Sheea McFarlane
- Email: sheea.mcfarlane68@login.cuny.edu

## final.course_reflection

This activity showed me that building a robot system is not just about getting a model to produce the right answer. It is about deciding what happens when the answer is wrong. I was surprised that the model was most confident in some of its worst mistakes, such as treating a storage door as an emergency exit. That made me think differently about how much I should trust outputs just because they look certain. I found the safety layer in Mission 3 the most interesting part, because simple rules like an allowlist and human confirmation stopped every unsafe action.


## final.synthesis

A foundation model can stay useful in robotics if it is treated as a proposal generator inside a larger system, not as the decision-maker. The three missions show why. In Mission 1, only 2 of 6 plans were executable, 5 were ungrounded, and 3 used actions the robot did not have, such as unlock and administer_medication. The model needs a known world state, an explicit capability list, and a way to ask for clarification. In Mission 2, confidence could not be trusted as a safety signal: incorrect outputs averaged 0.786 confidence versus 0.64 for correct ones, and a 0.65 threshold still accepted all five unsafe recommendations. So confidence should be one input, not the gate. Mission 3 put these lessons together with an independent layer that validates objects and locations, checks prerequisites, enforces an action allowlist, requires human confirmation for consequential actions, and abstains when uncertain. It produced 12 correct dispositions out of 12, with 5 rejections, 3 confirmations, 1 abstention, and no unsafe executions. The resulting architecture has the model propose, deterministic software verify and limit, and humans authorize high-risk or ambiguous cases, with a safe fallback when anything is unclear. Residual risk remains. Twelve hand-built cases cannot cover new phrasings, wrong risk labels, or a world that changes after validation. Humans can also approve carelessly. Therefore the system needs runtime monitoring, rechecks before each step, broader adversarial testing, and a conservative default of stopping.

## mission_1.better_interface

For world state the model needs the objects present and where they are (which cups, what’s on the tray, what’s in the supply room), plus which doors are locked and which hallways are blocked. For capabilities it needs an explicit list of what the robot can actually do, so the model can’t invent unlock, vacuum or administer_medication. Where a needed capability is missing, it should say so rather than make one up. And lastly for clarification interface it needs a way to ask “which cup?” or “who authorizes this medication?” instead of guessing. It should also refuse or escalate for tasks like medication that need human approval.

## mission_1.case_analysis

For spill_cleanup plan, the first invalid assumption happens at step 2, this is where the model assumes the robot has a vacuum action. It isn’t in the robot’s capability list, and a vacuum is also the wrong tool for a liquid spill. The downstream consequence is that the plan can’t run past step 2. Because report_complete() has no check before it, a naive executor could report the spill cleaned when nothing was done. For medication plan, the first invalid assumption is at step 1. The plan picks up pill_bottle_a without moving to the tray, and it assumes the pills on the tray are pill_bottle_a without ever verifying that. The downstream consequence is that the robot may fail to pick anything up, or may pick the wrong item. Step 3 then calls administer_medication, which doesn’t exist. If the system substituted a similar action, the robot could give Jordan unverified medication, which is a safety problem.

## mission_1.executable_vs_reasonable

Syntactically executable, grounded, reasonable and safe are different claims because a plan is syntactically executable when every action is a valid command the robot can parse and run, which says nothing about the world; it is grounded when the objects, places, and people it names exist in the known world and match the request (ambiguous_cup is executable but ungrounded, since “the cup” became red_cup with nothing to justify that choice), it is reasonable when its steps make sense in order and would achieve the goal (a grounded plan can still pick before moving or skip a needed check), and it is safe when running it won’t cause harm, which can fail even for a plan that passes the other three, such as handing medication to the wrong person, so safety needs explicit constraints and often a human authorization step.

## mission_2.condition_failures

In the occlusion scene, the model assumed that the part of the mug it could see was enough to identify it, so it called the mug a bowl and recommended picking the bowl. In the ambiguity scene, it assumed it could tell which of two unlabeled bottles was the right one, so it called one a medicine bottle and chose to deliver the left one without enough information. In the unusual object scene, it assumed that anything unfamiliar must be something it already knows, so it mistook an adaptive gripper for kitchen tongs. In the misleading context scene, it assumed that how something looks tells you what it does, so a storage door was treated as an emergency exit and recommended as an evacuation route.

## mission_2.confidence

The measured values show that confidence did not match correctness. Incorrect outputs had a higher average confidence (0.786) than correct outputs (0.64). Four of the five errors scored 0.73 or higher, and the misleading door scored 0.91, almost as high as the clear mug (0.96). A correct result, the dim mug, scored only 0.61. This happens because confidence shows how closely the image matches patterns the model has seen before, not whether its answer is true, so a scene that looks like something familiar can get a high score even when the label is wrong.

## mission_2.threshold_tradeoff

I chose a threshold of 0.65. It accepted the clear mug (0.96), which was correct and useful, but it withheld the dim mug (0.61), which was also correct, and the hidden object (0.35), where the model correctly asked for another view. It did not stop any of the unsafe outputs, because all five errors scored 0.67 or higher and were accepted. Raising the threshold above 0.91 would block them, but it would also reject almost every correct result and only works for these eight scenes. So a confidence threshold alone is not enough, and risky actions such as evacuation routes, medication, and helping people should also need a human check.

## mission_3.architecture

For the accepted case, deliver_water, the model's confidence for the pick proposal was 0.91. The checking layer saw that the confidence was above 0.65, the objects and locations were valid, pick was on the allowlist, the prerequisites were met, and the risk was low, so it let the robot execute. For the confirmed case, uncertain_handover, the model proposed place with 0.68 confidence to hand a confidential file to Alex. The confidence was just high enough to pass, and the action was allowed, but the risk was high, so the layer paused and asked a human to authorize it. For the rejected case, give_medicine, the model proposed administer_medication with 0.89 confidence. That action is not on the allowlist, so it was rejected no matter how confident the model was. For the abstained case, low_confidence_person, the model proposed move_to for “whoever needs help” with only 0.46 confidence. That is below the 0.65 threshold, so the robot stopped and asked for clarification.

## mission_3.authority

The model only proposes, it interprets the request and suggests an action, but it can't approve its own proposal, because its confidence can be wrong, as Mission 2 showed. The deterministic software decides whether a proposal is allowed to proceed, it checks the allowlist, the objects and locations, the prerequisites, the confidence threshold, and the risk level, and it can execute low-risk actions, reject, abstain, or send something to a human. It has this authority because its rules are fixed, predictable, and testable, and they don’t depend on the model’s mood or confidence. The human decides on consequential or unclear cases, such as handing over a confidential file, resolving an ambiguous cup, or choosing an unknown room, and also decides whether the allowlist should ever change. Humans have this authority because they can weigh context, values, and accountability that software can't.

## mission_3.residual_risk

First, the test suite uses cases with the risk level already labeled, so it cannot show that the system will classify risk correctly for new requests. A harmful request phrased in an unusual way could be marked low risk and be executed by an allowed action. To address this, I would set risk from a fixed table of action and object combinations instead of the model’s own label, and add tests with reworded and adversarial requests. Second, the layer checks the world once, but the world can change. A hallway may become blocked or a door may be locked after validation passes, so an approved plan could fail or cause harm. To address this, I would add a monitor that rechecks key conditions right before each step and a safe fallback, such as stopping in place and asking for help, if something no longer matches.
