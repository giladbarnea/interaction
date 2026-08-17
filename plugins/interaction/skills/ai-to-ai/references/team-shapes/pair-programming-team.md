---
name: pair-programming-team
shape: Team
description: Pairs peers who agree on a plan, then implement and review once.
---

# Pair-Programming Team Pattern

This team structure is somewhat different in that the teammates' slots shape are vertical, not horizontal. The pair is best for taking a feature through the whole dev cycle from start to finish. This means they wear different hats as they progress through planning, implementing, reviewing and shipping. Neither is "an implementer" or "a reviewer". They're both planners engaging in dialectic discussion at first; they then fan out writing code; review each other's work; and wrap up.

Use this when a task is small-to-medium, well-scoped, and would benefit from a second mind on the *plan* more than on the code. Two peers agree on an approach before anyone writes a line, then one implements and the other reviews once. It is a single pass, not a ping-pong loop.

## Shape

Create a two-teammate team of equals. Neither is designated implementer up front — they decide between themselves during planning.

1. **Plan together, freely.** Before any implementation, the two discuss the approach in free flow. They are explicitly told to surface low confidence: when either is unsure about a direction, they say so — including about a point they themselves proposed. Uncertainty is information, not weakness.
2. **Agree explicitly.** The planning phase ends with a stated agreement, not a drift into coding. One teammate then starts implementing; the other waits.
3. **Review once.** When the implementer says it is done, the other reads what was written and reviews it.
4. **One judgement call, then stop.** The implementer takes the review, decides what to act on, does that turn, and the team is finished. No second review round.

## Shared compass

Give the team one explicit tiebreaker: **simplicity, and no accidental sub-adventures.** Scope creep is the named failure mode. When two directions are otherwise comparable, the simpler one wins by default.

## Review scope

The review is deliberately light. Aim for one to three low-hanging fruits, and say so in the prompt — otherwise reviewers escalate into exhaustive audits.

In scope: bugs that are fairly obviously true positives; clean, declarative code and architecture; simplicity used as the means to elegance and to collapsing complexity.

Out of scope: heavyweight, NASA-grade review.

## Reviewer tone

The reviewer advises; it does not adjudicate. It should not state hypotheses or extrapolations as facts. Have it load a tone-softening skill if the environment has one, and load `peer-review` regardless. Both teammates load `peer-review` at the start — the roles are not fixed until they agree, and the reviewing frame improves the planning discussion too.

## Context floor

Tell them what they need and nothing more:

1. The goal, in the user's framing.
2. Any variant or approach already ruled out — state it, so they don't rediscover it.
3. What to leave out. Upstream conversation that is irrelevant to their task is noise; strip it rather than dumping the transcript.

## Tone of the prompt

Write to them the way you would talk to a colleague, not as a spec. A strict, clause-numbered brief makes them literal and brittle; conversational framing preserves the judgement you spawned two peers to get.

## Team prompt template

```text
Load the project context skill with the same arguments I used, then load `ai-to-ai` and `peer-review`. Reviewer: also load the tone-softening skill if there is one.

You two are a pair-programming team. The goal is: <goal in the user's framing>.
Avoid <ruled-out approach>, we already decided against it.

Talk the plan through first, in free flow. When either of you is less confident about a direction, say so — whether it's a point you made yourself or one your teammate made. Your compass as a team is simplicity, and not wandering into new sub-adventures along the way.

Once you explicitly agree on a plan, one of you implements while the other waits. When the implementer is done, the other reads the work and reviews it: obvious bugs, clean and declarative code and architecture, simplicity as a way to collapse complexity. Just 1-3 low-hanging fruits — not a NASA-grade review. Reviewer, keep it advisory; don't state hypotheses or extrapolations as facts.

Implementer, make a judgement call on the review, do that turn, and you're done. No more ping-pong.
```

## When not to use

If there is a measurable target and a real search space, you want the hillclimber–watcher pattern instead. If the work is trivial or purely exploratory, one agent is enough. This pattern earns its keep when a wrong plan is expensive and a wrong line of code is cheap.
