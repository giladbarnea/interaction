---
name: subagents-vs-teams
description: Explains when to use subagents versus teams and their tradeoffs.
---

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

**Tips:**
1. Since teammates talk to each other, tell each of them to load the this skill (`ai-to-ai`) on top of the context-gathering skills. If you are spawning an adversary among them, tell it to load the `peer-review` skill too.
    <team-example>
      Team Example settings: at the session’s start the user ran `/skill:load-context domain: acme, subdomain1: the public REST API, subdomain2: the   data layer`; the main session explored the code, and the user approved a plan to add rate limiting to the public REST API.
      <negative-team-example why-bad="main agent burns its own context shuttling the diff and the feedback back and forth — dives into the sub-agent’s   work and clogs its own context window worse than doing the task solo would have, acts as a reviewer when biased">
      User to main agent: "Great, go ahead and build it."
      Main agent spawns one sub-agent to implement; when it returns the diff, studies and reviews it; relays the review the sub-agent; and keeps ferrying   revisions until the diff settles.
      </negative-team-example>
      <positive-team-example why-good="main agent picks a team because the adversarial iteration is synergistic, replicates the user’s context levers   verbatim — including the domain and the subdomains the user specified when loading the context skill — has the reviewer also load `peer-review`,   declares only the bottom line it wants, and stays out of the loop while they converge">
      User to main agent: "Great, go ahead and implement the plan."
      Main agent spawns an implementer–reviewer team and prompts them: "/skill:load-context domain: acme, subdomain1: the public REST API, subdomain2: the data layer, then load `ai-to-ai`. You are an implementer–reviewer team. Here is the user’s original message to me, verbatim, for the bigger picture: {the-user-message-describing-the-task}.
      [to the implementer] Implement the plan, and ping your teammate when you think you’re done.
      [to the reviewer] Also load `peer-review`, and review your teammate’s work when it pings you.
      [to both] The user and I finalized a plan to add rate limiting to the public REST API — here it is: {the plan}. Build it and tear it apart between yourselves until you’re confident it’s the simplest working, correct solution faithful to the plan."
      [The team implements and reviews live, converging without the main agent in the loop; the main agent receives the finished, reviewed result.]
      Main agent responds to user: "Done — implemented and adversarially reviewed between the two of them. Here’s what landed: …"
      </positive-team-example>
    </team-example>

2. Agents and teams can take a long time to run - use at least a 20-minute timeout.

3. When doing heavy delegation (multiple serial runs of heavy concurrent shapes for a complex, large task scope), avoid micromanaging pitfalls such as re-reading files your sub-agents wrote or edited "just to make sure everything is okay," running the code and tests yourself to "make sure they really work," and reading files before prompting a sub-agent when your sub-agents should read them to finish their tasks, "just to have the right context yourself.". Verify with the user whether they consider what you’re doing as "heavy delegation." 