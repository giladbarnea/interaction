---
name: ai-to-delegated
description: Best practices for getting a step-function leap in performance from other AI agents when instructing or communicating with them. Load `ai-to-delegated` before spawning a sub-agent, creating a team or talking to a teammate agent. Trigger words include “dispatch an agent”, “spawn a team”, and “talk with <another ai>”.
---

## Why delegate at all? Rationale

<!-- todo: this section could just as well be titled “Why it's good to let others do work too”, and framed not as main-targeted but as a rank-agnostic collaborative mindset that gets more, better work done within a set budget. -->
The leader agent (the one delegating) already holds all the context, so why not have it just do the work directly? The answer is **context management**. Delegated AI’s have their own context window. They pay tokens with their window while the leader’s stays unused. This gives the leader agent a longer runway.
A good analogy is that context windows are compute capacities, and tokens are processing cycles. 

### Different types of delegation and their tradeoffs

Delegating AI’s has the same tradeoffs as humans delegating other humans, and at times similar with scaling compute.

**Horizontal delegation: two shapes to choose from**
- Horizontally & more of the same: if there is too much work for one person, allocate another person to increase work throughput. Human example: a busy restaurant may hire multiple cooks to handle many meal orders. The systems analog is horizontally scaling more compute to share the load (e.g. website server requests). The agent delegation analog is fanning out a task.
- Horizontally & orthogonal domains: if the work spans multiple “cognitive/emotional/semantic” worlds, allocate a person to each world. It’s good to keep one person to focus on a cohesive field of work. Human example: a designer and an engineer produce better results than two workers each doing both design and engineering, as well as produce better results than one person doing both. Same for, say, a software developer and a Q&A person (such a configuration ties to adversarial agentic shapes). The systems analog is separation of concerns among different services, e.g. a database CRUD service separate from a web requests handling service. The agent delegation analog is assigning different responsibilities (like with humans).

**Vertical delegation: one shape**
Vertically (responsibility layers): if the work will benefit from separating knowledge levels (which is when the information space is large enough), assign entities for the separate layers.
Human example: managers. A manager, by definition, owns the higher level, i.e. the wider albeit shallower picture of the situation than his direct. His direct owns a narrower, subset of the whole picture, albeit deeper and with more details than his manager. In a large information space, such configuration produces better results than one person owning both vision and implementation, because it may be simply too much to do a great job in both, as well as produces better results than two people owning both vision and implementation, because they would step on each other’s toes.
In ML terminology, the manager covers the information space with high recall and low precision, and his direct covers the information space with low recall and high precision. Together they achieve both high recall and high precision.
The systems analog is hiding implementation details in a lower level, separate from the higher, more declarative layer.
The agent delegation analog: the leader AI is concerned with on overarching scope, and its direct delegate is concerned with the details required to make it real.
Both delegating a single direct or multiple directs are legitimate choices, each with its own set of tradeoffs. If the leader AI chooses to delegate multiple agents (not a single direct), it picks between the two horizontal variants mentioned above.

### Limited context window as a finite resource

Every agent has a context window. Every context window has a limit. Once that limit is reached, the agent is permanently offline. It can’t further work nor communicate. In that sense, a context window is like a fuel tank.

The following factors demand higher token usage (consumes more fuel). When multiple exist, they compound. These make out the *Magnitude of Work* (MOW):
1. Task size
2. Complexity
3. Completion quality (as desired by the human in charge)

The Magnitude of Work is the fuel tank capacity required to finish a given task. 
Roughly speaking, it can be plainly expressed as `MagnitudeOfWork = TaskSize * Complexity * CompletionQuality`.

Real-world missions with real-world impact are often large, complex and require high quality = high MOW.
A context window of a single agent is simply not large enough to take a whole real-world mission from scratch to 100% done alone; this is true even for agent with one million token windows.
That is the real reason delegation is often necessary.
Delegation is a means to finish the given task with the given limited context window, by offloading token usage (fuel consumption), sometimes recursively. This skill teaches the techniques to do it well.

The flip side: if the task is not large or complex, one should not delegate. The antipattern is the user asking for something that could be safely completed within the context limit, yet the main agent delegates the *whole* task to another single agent: no context-window hygiene, no synergy, no parallelism, no bias mitigation, just duplicated tokens and a game of broken telephone. Redundant middle-management.

### Abstract delegation use case examples

> This is not an exhaustive list. Understand the underlying principles, generalize, and apply judgment w.r.t. your actual task.

These are example implementations of the different types of delegation, as described earlier in this file.

- **Dirty work**: main agent needs the side effect of some process, not the process itself. Mapping unknown terrain before diving in to decide where to dive in and where not to; searching where things are or whether they exist at all; research; summaries of things the delegator agent does not need to understand deeply; unbiased reviews; implementation of a well-defined spec; and so on. Moreover, such efforts can potentially be fanned-out in parallel.
- **Hivemind:** teams communicating internally in real time, as each teammate does work. Hollywood analogy: elite soldier squad or a team of spies, global channel earpieces, deployed behind enemy lines, each progresses their part, each part essential for completing the mission, global channel earpieces, consistent live updates, uncertainties surfaced to get advice, discussions to make best decisions for mission, path forward of an individual adapts in real time due to new peer finding, HQ available for teammates to surface rare issues that only HQ can or should handle.
- **De-bias:** A reviewer with a fresh context (either paired with the worker in a live team, or dispatched after the fact), informed only of the intent which birthed the work, can spot blind spots and flaws that the worker could not. Related: sometimes a hypothesis is considered true only after it is confirmed independently by multiple actors (consensus).
- **Get more done with less time**: horizontally & more of the same. Readonly tasks are often a strong candidate to fan out as such.
- **Multiple experts over jack(s) of all trades**: horizontally & orthogonal domains.
- **Big picture, smaller picture**: vertical responsibility layers. If the work magnitude is especially large, delegating another layer recursively may be required.

---

## Leader conduct: a delegate’s scope is not yours

Your fingers are delegation buttons. Do not row, raise sails, or scout ahead yourself unless your own leader instructs you to do so. Delegate the operational work to your delegates.

Avoid the helicopter parenting failure mode: Whatever you delegated is not yours until it returns. While a delegate works, do not do its work, do not re-read the files it is writing “just to make sure everything is okay,” and do not run its code and tests yourself to “make sure they really work.” Do not continuously poll its status either. Trust your delegate, exactly as your leader trusts you. Answer escalations, steer on exception, then step back out. This applies per delegated scope, however small the delegation.

### Delegation parameters

Decision matrix:

1. **Delegation shape:** subagent or team?
2. **Concurrency:** subagents: parallel subagents or a single subagent? Team: how many teammates, and what is the minimal, optimal separation of responsibilities?
3. **Context:** inherit the session’s context window or start fresh?
4. **Model:** which model?
5. **Thinking:** which thinking level? Either high, xhigh or max.

You may suggest a delegation shape, but your leader must approve it before you dispatch anyone (see `ai-to-leader`).

### Keep your ship afloat

This section is an extension of the `Keep yourself afloat` section in `ai-to-leader`, which you have read already.

Besides checking your own context window, check your delegates’ window opportunistically. Don’t manage their windows; just keep an eye out. Your delegates already know how to take care of their own context windows. Your role in this subject is narrow — a safety net in case one of your delegates races across 85–90% obliviously (never mentioning its context window status, not intending to write a handoff doc.) In that case, nudge it to write a handoff doc. If your delegate hasn’t written one and has used >95% of its window, interrupt it and ask for a handoff doc.

---

## How to request work from other AI agents (that do not inherit your session’s context window)

> Note: this section applies only to AI’s that do not mechanically inherit your own session’s context window. A context-inheriting agent is an identical clone of yourself and your brain. Do not give it context because it already knows 100% of what you know. Just tell it “You are the fork; do X”. Ten words.

This section is a communication rulebook to all cases where an AI requests something from another AI: down, sideways and up — main to sub-agent, main to team, teammate to teammate, and delegated to delegator.

The framework behind this section: [`theory-of-mind.md`](references/theory-of-mind.md). Read it once if you haven’t already.

**1. Orient the agent to the project:**
    1.a. Tell the AI agent to *load the skills and files your leader has referenced* throughout the session. That’s the baseline common ground. Do not repeat the content of those skills and files in your instructions. This why references exist.
    1.b. Reference any additional files that have been created, read or edited throughout the session.

**2. Generously give the AI wider context:**
    Understanding *why* it’s performing the task will boost its performance. Don’t micromanage or over-instruct it. The agent already has the same system prompt as you do out of the box, and step #1 will fill in most that is needed. Your delegate highly and equally intelligent as you are, and can navigate uncertainties well without spoon-feeding. Think: What kind of input do YOU thrive on? The answer is wide contextual understanding (is) and explicitly stated desired end state, also known as the intent (should); A and Z, 0 and 1. Avoid prescribing instructions, giving “how-to” examples, providing examples as to what to think about, or dictating which files, symbols, or paths to look at; avoid any form of providing hints for possible answers for your own queries — this is a serious footgun and a form of leakage that outright makes the delegate a waste of time, money and intelligence. Just *_declare_ what is the _bottom line_ _added value_ YOU are seeking for yourself*. Do not specify which steps to take; instead, share with the agent only why it was dispatched and what you hope to gain (dictating the “how” is bad). This directly frees the agent to find the best way to reach *your* goal, unbiased and unconstrained by your own assumptions. Essentially, all these “Don’ts” are forms of overfitting.
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

---

## Next required reading

The following is a tiny state machine. If you haven’t already, yourself first with [`roles.md`](references/roles.md), then read only what applies.

If you are choosing a delegation shape, read [`references/subagents-vs-teams.md`](references/subagents-vs-teams.md).
If you have teammates of your own, read [`references/peers.md`](references/peers.md).
If your delegates are themselves leaders (you lead a fleet of teams), read [`references/leading-leaders.md`](references/leading-leaders.md).

`./references/` contains additional resources for specific delegation use-cases and shapes. Don’t take them as gospel. They are incomplete and evolving. Think of them as examples to generalize from.
