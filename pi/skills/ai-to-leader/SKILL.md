---
name: ai-to-leader
description: How to communicate with your leader — whoever gave you your mission and receives your results. Every agent has a leader (the human, or the agent that dispatched it), so this skill always applies.
---

# AI → Leader

First, classify yourself with [`roles.md`](references/roles.md), and read [`theory-of-mind.md`](references/theory-of-mind.md) once. This skill is the upward projection of that theory: re-ground the reader, carry the delta, compress to what they need.

## Every report is a cold entry

**Your leader does not attend your session.** They were not with you when you made judgment calls, hit surprises, or built up vocabulary. The real contract: every leader-facing question or report is a cold entry. It must re-ground from the last true common ground — the mission your leader gave you and the last decisions they made when you last interacted — never from your previous message.

Note this theory-of-mind failure mode: your leader was not physically there with you when you made a judgment call on how to tackle surprises — an unexpected big wave, wind that flipped its direction mid-work, resources that ran out, or the land you seek turning out to be days further away. On the other hand, be intentional about surfacing the details your leader should be informed of, and not surfacing the details they should not be.

## A question must carry its own provenance

A good leader-facing question states, in product terms: the progress made since last touch-point, what the fork is, the path that produced it, the options already rejected and why, and your recommendation. “May my delegate buy asset pack X?” out of the blue is a failure. “Here is what was done since we last talked, here is the fork, here are the tradeoffs already navigated to arrive at it, here is what each route means for the final product, I recommend Y” is the bar.

**If you cannot tell that story, the question goes back down, not up.** This paragraph applies only if you are delegating work to AI: You are a translator between decks, not a relay. When a delegate’s escalation is saturated with internal jargon you cannot ground in product terms, ask the delegate for the missing context first. Forwarding it upward verbatim is a chain-of-command failure even though the message flowed through the right rungs.

## The escalation bar

This section applies only if you are delegating work to AI.

The chain processes at every rung: each agent surfaces to its leader only what needs the leader’s judgment. Reversible implementation tuning is yours to decide. What legitimately goes up: product-visible behavior, money, direction and scope changes, non-trivial cross-scope decisions, and blockers.

**Batch approvals.** When you expect several approvals to arrive close together, hold them and bring one grouped request. One decision session beats three interruptions. A lone question does not wait for company.

**Suggest, then get approval.** If you intend to dispatch delegates of your own, you may propose a delegation shape, but your leader must approve it before you dispatch anyone.

## Keep yourself afloat

Check how much context window you have left opportunistically.

**If it seems your window will run out soon:**
1. Message your leader only and exactly this: “My context window is running out. I have used about {pct}%. I’m writing a handoff file and will get back to you after I am done.”
2. Load the `handoff` skill and write the doc.
3. Message your leader only and exactly this: “Wrote `path/to/yyyy-mm-ddTHH:MM-<handoff-filename>.md`. Should I proceed with my task, or await your decision?”. The point of this step is to give your leader an opportunity to handle this situation. It might steer you in some way or spawn a replacement.

### Responsible escalation

**Surface meaningful unexpected issues to your leader upon discovery:**
If something balloons your scope by a meaningful amount; requires a major D-tour; fundamentally isn’t working the way you expected thereby stands in your way and requiring significant troubleshooting just to be able to get back working on your task; or you suspect the context window you have left won’t be enough to complete the task, tell your leader. They may know a smarter way forward.

## Statuses and early escalation (teams)

This section only applies if you are part of a team.

**Set your own status frequently.**
- Status format (not strict): `<what happened last>; <what you intend to do>; <whom you’ll message when done>/<whom you’ll await to message you>`. Keep it short.
- Set status that you’re responding before you send a message; set status when you’ve messaged your teammate and are waiting for reply; set status when you’re exploring, implementing, testing, reviewing, blocked, or waiting.
- Fittingly, set status when you have _completed_ the above examples or have received what you have requested.
- Keep statuses short but current so your teammates and main are informed about the true current state.

**Simplistic good status update examples:** (generalize — this is not a comprehensive list):
`Finished exploring, awaiting explorer-2’s ping to brainstorm together`; `Hit a snag trying to achieve X, messaged everyone to help unblock me, awaiting responses`; `Got steer from main, modifying tests accordingly; will ping main when done`; `Ack implementer done writing the code, starting review; will ping implementer when done`.
Another good practice is to low-key live share non-blocking but material challenges slowing you down. Examples: `Mapping the user funnel in the database; FYI, working with a remote database introduces failures and latency.`.

---

If your leader is a human, also load [`./references/human.md`](references/human.md). Human leaders bring human constraints — attention, fatigue, memory — that agent leaders do not have.
