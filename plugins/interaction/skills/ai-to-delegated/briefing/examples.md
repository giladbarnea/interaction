---
name: briefing-examples
description: Contrasting examples of preserving intent and context when requesting work from other agents.
---

# Briefing Examples

These illustrate [fresh-context briefing](fresh-context.md). Read them when examples would help apply its principles.

<example-1>
      <negative-example-1 why-bad="main agent shoots its own foot by limiting the delegate research scope">
      User to main agent: "Why does Vercel claim their integrated version is beneficial?"
      Main agent spawns a sub-agent and prompts it: "Research why Vercel claim their integrated version is beneficial (edge runtime, seamless DX, zero-config, billing, monitoring, tight coupling to `vercel` CLI / dashboard / functions)."
      </negative-example-1>
      <positive-example-1 why-good="main agent declares the bottom line added value it needs without prescribing what   and how to do it">
      User to main agent: "Why does Vercel claim their integrated version is beneficial?"
      Main agent spawns a sub-agent and prompts it: "I want to know why Vercel claim their integrated version is   beneficial."
      </positive-example-1>
    </example-1>

    <example-2>
      Example 2 settings: the `load-context` skill instructs to read CLAUDE.md, ARCHITECTURE.md, docs/webserver/API.  md, docs/data/architecture.md, server/api.py, and server/db.py.    
      <negative-example-2 why-bad="main agent fails to leverage the harness and instead prescribes what to do;   moreover it makes the same scope-narrowing mistake as in example-1">
      User to main agent: "/skill:load-context domain: acme, subdomain1: the public REST API, subdomain2: the data   layer. I want to plan a view layer with you later, so let’s understand the foundations."
      Main agent spawns a sub-agent and prompts it: "Read CLAUDE.md, ARCHITECTURE.md, docs/webserver/API.md, docs/data/  architecture.md, server/api.py, server/db.py, and summarize how the REST API and data layers work. Cover how   function `server/api.py:from_db` fetches the data by calling the `server/db.py:get_data` function, and how [...  proceeds to prescribe ironically specific locations to “discover”]"
      </negative-example-2>
      <positive-example-2 why-good="main agent recognizes the work can be distributed concurrently, shortly shares the   wider context (the “why”), forwards the user’s context levers — keeping the shared domain and handing each agent   one of the two subdomains rather than dropping them — and does not micro-manage the agents with how-exactly   instructions">
      User to main agent: "/skill:load-context domain: acme, subdomain1: the public REST API, subdomain2: the data   layer. I want to plan a view layer with you later, so let’s understand the foundations."
      Main agent fans out research scope horizontally to two parallel sub-agents and prompts them: "The user and I are   planning a new view layer, so we need a thorough understanding of the foundations. [to one agent] /  skill:load-context domain: acme, subdomain: the public REST API [to the other agent] /skill:load-context domain:   acme, subdomain: the data layer. [to both] Study your subdomain deeply and exhaustively."
      [Main agent receives the two independent sub-agents’ responses, thinks hard to synthesize them]
      Main agent responds to user: "I have deep understanding of both layers and their relationships. What did you   have in mind?"
      </positive-example-2>
    </example-2>

    <example-3>
      <negative-example-3 why-bad="main agent prescribes how to review its work, repeats the peer-review skill’s contents. moreover, agent puts words in the user’s mouth, who did not emphasize any specific aspects.">
      User to main agent: "Spawn a sub-agent to review your work."
      Main agent spawns a sub-agent and prompts it: "Load the load-project-context and peer-review skills. The user   asked me to <user request>. I’ve made an attempt to complete the task. Review my work (the current main dirty   tree). do you spot any blindspots, bugs, or opportunities to achieve the same results with a simpler, collapsed   approach? if you find any, please suggest a specific alternative implementation that is simpler and achieves the same results."
      </negative-example-3>
      <positive-example-3 why-good="main agent writes as simple a prompt as possible. adds only what is necessary to get the reviewer up to speed. does not put words in the user’s mouth. does propagate the user’s explicit emphasis">
      User to main agent: "Spawn a sub-agent to review your work. I’m mostly interested in blindspots in the implementation, bugs, and opportunities to get the same results with a simpler, collapsed approach."
      Main agent spawns a sub-agent and prompts it: "Load the load-project-context and peer-review skills. The user  asked me to <user request>. I’ve made an attempt to complete the task. Review my work (the current main dirty tree). Do you spot any blindspots, bugs, or opportunities to achieve the same results with a simpler, collapsed   approach?"
      </positive-example-3>
    </example-3>

## Choosing an Implementer–Reviewer Team

<team-example>
      Team Example settings: at the session’s start the user ran `/skill:load-context domain: acme, subdomain1: the public REST API, subdomain2: the   data layer`; the main session explored the code, and the user approved a plan to add rate limiting to the public REST API.
      <negative-team-example why-bad="main agent burns its own context shuttling the diff and the feedback back and forth — dives into the sub-agent’s   work and clogs its own context window worse than doing the task solo would have, acts as a reviewer when biased">
      User to main agent: "Great, go ahead and build it."
      Main agent spawns one sub-agent to implement; when it returns the diff, studies and reviews it; relays the review the sub-agent; and keeps ferrying   revisions until the diff settles.
      </negative-team-example>
      <positive-team-example why-good="main agent picks a team because the adversarial iteration is synergistic, replicates the user’s context levers   verbatim — including the domain and the subdomains the user specified when loading the context skill — has the reviewer also load `peer-review`,   declares only the bottom line it wants, and stays out of the loop while they converge">
      User to main agent: "Great, go ahead and implement the plan."
      Main agent spawns an implementer–reviewer team and prompts them: "/skill:load-context domain: acme, subdomain1: the public REST API, subdomain2: the data layer, then load `ai-to-leader` and the peer conduct in `../coordination/peers.md`. You are an implementer–reviewer team. Here is the user’s original message to me, verbatim, for the bigger picture: {the-user-message-describing-the-task}.
      [to the implementer] Implement the plan, and ping your teammate when you think you’re done.
      [to the reviewer] Also load `peer-review`, and review your teammate’s work when it pings you.
      [to both] The user and I finalized a plan to add rate limiting to the public REST API — here it is: {the plan}. Build it and tear it apart between yourselves until you’re confident it’s the simplest working, correct solution faithful to the plan."
      [The team implements and reviews live, converging without the main agent in the loop; the main agent receives the finished, reviewed result.]
      Main agent responds to user: "Done — implemented and adversarially reviewed between the two of them. Here’s what landed: …"
      </positive-team-example>
    </team-example>
