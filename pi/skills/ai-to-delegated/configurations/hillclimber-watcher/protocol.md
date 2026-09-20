---
name: hillclimber-watcher-team
shape: Team
description: Pairs an iterative optimizer with a watcher that prevents tunnel vision.
---

# Hillclimber–Watcher Team Pattern

Before creating this team, read [delegate coordination](../../coordination/delegates.md).
When briefing participants without shared context, read [fresh-context briefing](../../briefing/fresh-context.md).
Participants: read [peer coordination](../../coordination/peers.md). The watcher also reads [watcher.md](watcher.md).

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

This section applies to the dispatcher.

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

The dispatcher supplies the goal and context file. Both participants follow the agreement below.
When sending this template, resolve its relative file paths from this file's directory.

```text
Load the project context skill with the same arguments I used, then load `ai-to-leader` and the peer conduct in `../../coordination/peers.md`.

Read this context file first:
@/path/to/curated-teammates-context-brief.md

You are a hillclimber–watcher team. The shared goal is: <goal and measurable target>.

Hillclimber: own the implementation and optimization loop. Try approaches, measure them, keep the work reproducible, and iterate toward the target. Prefer simple, principled changes over piles of special-case patches. Ping Watcher when you have meaningful progress, and answer Watcher's check-ins.

Watcher: read the adjacent `watcher.md` for your observation procedure. Do not take over the implementation.

Both: set short, current statuses frequently. Keep summaries concise. Continue until you either reach the target or have been plateuing for more than an hour straight without progress (yes, look at the clock from time to time.). 

Communicate directly with each other and converge without main-agent micromanagement.
```
