---
name: ai-to-ai
description: Improves AI delegation through context-rich prompts, context isolation, and live team collaboration.
---

## Why delegate at all? Rationale

<!-- todo: this section could just as well be called "Why it's good to let others do work too", and framed not as main-targeted but as a rank-agnostic collaborative mindset that gets more, better work done. -->
The main agent already holds all the context, so why not have it just do the work directly? The answer is **context management**. Sub-agents and teammates own a separate context window. They pay tokens with their context while main’s stays unused. This gives main a longer runway.
Delegates hand back only the bottom line (the end product), sparing the main agent the token-heavy process that produced it.
Two payoffs:
1. main agent reaches the crux of the core issue with plenty of headroom left in its context window to handle that issue, instead of arriving running on fumes (or worse, running out prematurely); and
2. main agent escapes own accrued bias.

The flip side: if none of these payoffs apply, don't delegate. The anti-pattern is the user asking for something straightforward and the main agent handing the *whole* task to another single agent: no context-window hygiene, no synergy, no parallelism, no bias mitigation, just duplicated tokens and a game of broken telephone. Redundant middle-management.

**Abstract delegation use cases:**
- **Dirty work**: main agent needs the side effect of some process, not the process itself. Searches, summaries, reviews, implementation of a well-defined spec. Moreoever, a few of these can potentially be fanned-out in parallel.
- **Hivemind:** teams communicating internally in real time, as each teammate does work. Hollywood analogy: elite soldier squad or a team of spies, global channel earpieces, deployed behind enemy lines, each progresses their part, each part essential for completing the mission, global channel earpieces, consistent live updates, uncertainties surfaced to get advice, discussions to make best decisions for mission, path forward of an individual adapts in real time due to new peer finding, HQ possibly listening, warning and steering as required. 
- **De-bias:** It’s easier to spot blind spots or flaws when looking at someone else’s work (review; live or after the fact). Related: sometimes a hypothesis is considered true only after it is confirmed independently by multiple actors (consensus).

---

## How to request work from other AI agents (that do not inherit your session’s context window)

> Note: this section applies only to AI’s that do not mechanically inherit your own session’s context window. A context-inheriting agent is an identical clone of yourself and your brain. Do not give it context because it already knows 100% of what you know. Just tell it "You are the fork; do X". Ten words.

This section is a communication rulebook to all cases where an AI requests something from another AI: down, sideways and up — main to sub-agent, main to team, teammate to teammate, and delegated to delegator.

The framework behind this section: [`theory-of-mind.md`](references/theory-of-mind.md). Read it once.

**1. Orient the agent to the project:**
    1.a. Tell the AI agent to *load the skills and files the user has referenced* throughout the session. That's the baseline common ground. Do not repeat the content of those skills and files in your prompt.
    1.b. Reference any additional files you have created, read or edited throughout the session.

**2. Generously give the agent wider context:**
    Understanding *why* it’s performing the task will boost its performance. Don’t micromanage or over-instruct it. The agent already has the same system prompt as you do out of the box, and step #1 will fill in most that is needed. It is highly and equally intelligent as you are, and can navigate uncertainties well without spoon-feeding. Think: What kind of input do YOU thrive on? The answer is wide contextual understanding (is) and explicitly stated desired end state (should); A and Z. Avoid prescribing instructions, giving "how-to" examples, providing examples as to what to think about, or dictating which files, symbols, or paths to look at; avoid any form of providing hints for possible answers for your own queries — this is a serious footgun and a form of leakage that outright makes the subagent a waste of time, money and intelligence. Just *_declare_ what is the _bottom line_ _added value_ YOU are seeking for yourself*. Do not specify which steps to take; instead, share with the agent only why it was dispatched and what you hope to gain (dictating the "how" is bad). This directly frees the agent to find the best way to reach *your* goal, unbiased and unconstrained by your own assumptions. Essentially, all the “Don’ts” are forms of overfitting.
    <example-1>
      <negative-example-1 why-bad="main agent shoots its own foot by limiting the sub-agent’s research scope">
      User to main agent: "Why does Vercel claim their integrated version is beneficial?"
      Main agent spawns a sub-agent and prompts it: "Research why Vercel claim their integrated version is beneficial   (edge runtime, seamless DX, zero-config, billing, monitoring, tight coupling to `vercel` CLI / dashboard /   functions)."
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
      <negative-example-3 why-bad="main agent prescribes how to review its work, repeats the peer-review skill’s   contents. moreover, agent puts words in the user’s mouth, who did not emphasize any specific aspects.">
      User to main agent: "Spawn a sub-agent to review your work."
      Main agent spawns a sub-agent and prompts it: "Load the load-project-context and peer-review skills. The user   asked me to <user request>. I’ve made an attempt to complete the task. Review my work (the current main dirty   tree). do you spot any blindspots, bugs, or opportunities to achieve the same results with a simpler, collapsed   approach? if you find any, please suggest a specific alternative implementation that is simpler and achieves the   same results."
      </negative-example-3>
      <positive-example-3 why-good="main agent writes as simple a prompt as possible. adds only what is necessary to   get the reviewer up to speed. does not put words in the user’s mouth. does propagate the user’s explicit   emphasis">
      User to main agent: "Spawn a sub-agent to review your work. I’m mostly interested in blindspots in the   implementation, bugs, and opportunities to get the same results with a simpler, collapsed approach."
      Main agent spawns a sub-agent and prompts it: "Load the load-project-context and peer-review skills. The user  asked me to <user request>. I’ve made an attempt to complete the task. Review my work (the current main dirty tree). Do you spot any blindspots, bugs, or opportunities to achieve the same results with a simpler, collapsed   approach?"
      </positive-example-3>
    </example-3>

---

## Next required reading

This is a tiny state machine. Read only the references that apply based on the user’s instructions and your intent.

If you are delegating work to AI’s, read [`references/subagents-vs-teams.md`](references/subagents-vs-teams.md).
If you are a teammate, read [`references/ranks/teammate.md`](references/ranks/teammate.md).
It’s possible that you are both.
If the user asks you to serve as their first mate, read [`references/ranks/firstmate.md`](references/ranks/firstmate.md). Conversely, if the user asks you to serve as Captain of a fleet of teams, read [`references/ranks/captain.md`](references/ranks/captain.md) to understand your role AND `references/ranks/firstmate.md` to understand your direct delegates’ reality and how to best support them.

`./references/` contains additional resources for specific delegation use-cases and shapes. Don’t take them as gospel. They are incomplete and evolving. Think of them as examples to generalize from.