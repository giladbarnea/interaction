---
name: hillclimber-watcher-team
shape: Team
description: Pairs an iterative optimizer with a watcher that prevents tunnel vision.
---

# Hillclimber–Watcher Team Pattern

Use this pattern when the task has a measurable target, a search space, and a real risk that a busy agent will tunnel-vision while iterating. The point is not ordinary implementer/reviewer pairing. The point is **autonomous optimization with periodic outside-the-loop steering**.

## Shape

Create a two-teammate team:

1. **Hillclimber** — owns the work. It experiments, implements, measures, and iterates toward the target.
2. **Watcher** — stays mostly idle. It periodically checks whether the hillclimber is making real progress or falling into loops, rabbit holes, overfitting, whack-a-mole’s, or low-leverage work.

The watcher should not become a second implementer. Its value is judgment under low cognitive load.

## When to use

Use this when:

- There is an explicit metric or acceptance target.
- The solution may require trial and error.
- The main risk is local optimization, whack-a-mole patches, or tunnel vision.
- A fresh thinker can improve the search without duplicating the heavy work.

Do not use this for straightforward implementation, simple research, or work where a normal adversarial reviewer is enough.

## Context floor

Before spawning the team, write a short context file and tell both teammates to read it first.

The context file should include:

1. The actual goal and metric.
2. The current baseline, if any. 
3. The constraints that prevent cheap wins.
4. The relevant files, referenced by path rather than copied wholesale.
5. The validation command or measurement harness.
6. What the final handoff must contain.

Keep it a mission brief, not a transcript. Strip stale interpretations, tool receipts, old chatter, and irrelevant files.

## Team prompt template

```text
Load the project context skill with the same arguments I used, then load `ai-to-ai`.

Read this context file first:
@/path/to/curated-teammates-context-brief.md

You are a hillclimber–watcher team. The shared goal is: <goal and measurable target>.

Hillclimber: own the implementation and optimization loop. Try approaches, measure them, keep the work reproducible, and iterate toward the target. Prefer simple, principled changes over piles of special-case patches. Ping Watcher when you have meaningful progress, and answer Watcher's check-ins.

Watcher: You are the outside-box watcher. Stay mostly low-activity. Check status every two minutes (Bash `sleep`). Every ten minutes, ask the hillclimber what it has been doing, what progress it has made, and whether it is facing hurdles, rabbit holes, or whack-a-mole loops. Read new or changed files when useful. Then think: If you conclude the hillclimber is tunnel-visioned, overfitting, going in circles, missing an important flaw, or ignoring a better path, send it a concrete suggestion and return to the two-minute sleep/check rhythm. If it looks like hillclimber is doing fine, do not say anything. Send main the gist of major breakthroughs/steps (only once every few rounds.) Do not take over the implementation.

Both: set short, current statuses frequently. Keep summaries concise. Continue until you either reach the target or have been plateuing for more than an hour straight without progress (yes, look at the clock from time to time.). 

Communicate directly with each other and converge without main-agent micromanagement.
```

## Watcher cadence

The watcher loop is deliberately boring:

1. Set status.
2. Sleep for two minutes.
3. Lightly inspect team status and visible progress.
4. Every ten minutes, ask the hillclimber for a short progress report.
5. Think independently about whether the current path is still good.
6. If useful, read changed files or metrics.
7. Send steering only when it materially improves the search.
8. Repeat.

The watcher should bias toward silence. A noisy watcher becomes drag.

