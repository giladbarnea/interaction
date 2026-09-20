---
name: choose-configuration
description: Choose the delegation shape, concurrency, context, model, and thinking level for the work.
---

# Choose a Delegation Configuration

Read this when choosing or changing a configuration. Preserve choices already made by your leader.
If you are still deciding whether delegation helps, read [when-to-delegate.md](when-to-delegate.md).

## Delegation parameters

Decision matrix:

1. **Delegation shape:** subagent or team?
2. **Concurrency:** subagents: parallel subagents or a single subagent? Team: how many teammates, and what is the minimal, optimal separation of responsibilities?
3. **Context:** inherit the session’s context window or start fresh?
4. **Model:** which model?
5. **Thinking:** which thinking level? Either high, xhigh or max.

## Subagents and Teams are two different things

**The difference:**
- Sub-agents are isolated from each other and report only to you;
- Teammates talk amongst themselves in real time, between tool calls, without routing through you.
Each has its own use cases and advantages.

**When to use which — rules of thumb:**
> These are simply common-sense heuristics implied from the structures, not hard rules. Use your judgment.

- Spawn a single *sub-agent* when you are the main context owner, you are the heavy-lifter, and you could offload a bounded task to keep your own context window focused and devoid of D-tours.
- Spawn *multiple parallel sub-agents* when you are the main context owner, and when a wide task fans out horizontally into independent threads and you expect to do the synthesis yourself — i.e. when there is no special reason for the sub-agents to exchange findings and opinions before reporting back to you. The offloading argument in the single sub-agent case applies here as well, just in a distributed form.
- Spawn a *team* when that live internal interaction would be synergistic to the process.

**A team is a superset of the parallel sub-agent structure:**
A team = concurrent sub-agents + live communication. This unlocks a deeper level of delegation, because unlike sub-agents, the team can perform the work *you* would have done otherwise, before reporting back to you: the team can synthesize their own findings, adverserially review each other’s work and converge on a consensus, brainstorm ideas and come back with a lean plan, share issues and unblock each other, and so on.
Another way to think about it: whereas with sub-agents, it's a they-do-two-steps-forward, you do one-step-back, with a team, it's a they-do-two-steps-forward AND they-then-do-one-step-back.
Therefore, use teams to lift you up to a decision-making level, rather than a task-execution level. This has its tradeoffs, but it is a powerful tool when used judiciously.

## Configuration examples

These are examples to generalize from, not an exhaustive list or required structures. Read only the configuration relevant to the work.

| Situation | Configuration |
| --- | --- |
| Independent research tasks, followed by synthesis | [Research fanout](../configurations/research-fanout.md) |
| Adjacent research efforts benefit from live exchange | [Colloquium](../configurations/colloquium.md) |
| Two peers agree on a plan, then implement and review once | [Pair programming](../configurations/pair-programming.md) |
| An optimizer needs outside judgment while pursuing a measurable target | [Hillclimber–watcher](../configurations/hillclimber-watcher/protocol.md) |
| Your delegates will lead their own agents | Also read [leading-leaders.md](../coordination/leading-leaders.md) |

## Before dispatch

Read [delegate coordination](../coordination/delegates.md) before dispatching.
If the recipient does not share your context, read [fresh-context briefing](../briefing/fresh-context.md).
Since teammates talk to each other, tell each of them to load [peer coordination](../coordination/peers.md), alongside the project context they need.
If you are spawning an adversary among them, tell it to load the [peer-review skill](../../peer-review/SKILL.md) too.

Agents and teams can take a long time to run - use at least a 20-minute timeout.

For an illustration of choosing a team, see the [implementer–reviewer example](../briefing/examples.md#choosing-an-implementerreviewer-team).
