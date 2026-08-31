---
name: roles
description: The classifier every agent runs first — three questions that decide which interaction skills to load.
---

# Roles: Who Are You in the Structure?

Instructions attach to edges, not to agents. An agent has no role; its edges do.

Definitions:

- **Your leader**: whoever gave you your mission and receives your results. Every agent has exactly one — the human, or the agent that dispatched you.
- **Your delegates**: AI’s you dispatched. Zero or more.
- **Your peers**: teammates working alongside you under the same leader. Zero or more.

Hierarchy depth never matters. Every agent’s neighborhood looks the same: one edge up, optional edges down and sideways. Classify by your adjacent edges only.

## The classifier

| question | if yes, load |
| --- | --- |
| — (always) | [`theory-of-mind.md`](./theory-of-mind.md) + [`ai-to-leader`](../skills/ai-to-leader/SKILL.md) |
| Is your leader a human? | [`ai-to-leader/references/human.md`](../skills/ai-to-leader/references/human.md) |
| Do you dispatch subagents or teams? | [`ai-to-delegated`](../skills/ai-to-delegated/SKILL.md) |
| Do you have teammates? | [`ai-to-delegated/references/peers.md`](../skills/ai-to-delegated/references/peers.md) |

Notes:

- “Both” is not a special state. A mid-chain agent holds an upward edge and downward edges. It loads both skills and applies each to its own edge. The two spaces never conflict, because they govern different edges.
- Narrow, in-and-out delegation still flips the dispatch bit. Whatever you delegated is not yours until it returns, regardless of how much of the work stays in your hands.
