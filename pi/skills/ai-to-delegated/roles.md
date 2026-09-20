---
name: roles
description: Map an agent's relationships to the interaction guidance that applies.
---

# Roles: Who Are You in the Structure?

Instructions attach to edges, not to agents. An agent has no role; its edges do.

Definitions:

- **Your leader**: whoever gave you your mission and receives your results. Every agent has exactly one — the human, or the agent that dispatched you.
- **Your delegates**: AI’s you dispatched. Zero or more.
- **Your peers**: teammates working alongside you under the same leader. Zero or more.

Hierarchy depth never matters. Every agent’s neighborhood looks the same: one edge up, optional edges down and sideways. Classify by your adjacent edges only.

## The classifier

Read every matching route, once while its contents remain in context. Reconsider the routes when your relationships change.

| question | if yes, load |
| --- | --- |
| — (always) | [`theory-of-mind`](../theory-of-mind/SKILL.md) + [`ai-to-leader`](../ai-to-leader/SKILL.md) |
| Is your leader a human? | [`ai-to-leader/references/human.md`](../ai-to-leader/references/human.md) |
| Do you dispatch or supervise delegates? | [Delegate coordination](coordination/delegates.md) |
| Do your delegates lead their own agents? | Also [leading leaders](coordination/leading-leaders.md) |
| Do you have teammates? | [Peer coordination](coordination/peers.md) |

Notes:

- “Both” is not a special state. A mid-chain agent holds an upward edge and downward edges. It loads both skills and applies each to its own edge. The two spaces never conflict, because they govern different edges.
- Narrow, in-and-out delegation still flips the dispatch bit. Whatever you delegated is not yours until it returns, regardless of how much of the work stays in your hands.

For delegation planning, briefing, or named configurations, use the matching routes in [ai-to-delegated](SKILL.md).
