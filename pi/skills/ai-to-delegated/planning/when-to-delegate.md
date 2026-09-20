---
name: when-to-delegate
description: Decide whether delegation adds value through context management, specialization, independent judgment, or parallel work.
---

# When to Delegate

Read this when deciding whether delegation is worthwhile. If delegation is already decided, continue with the unresolved choices in [choose-configuration.md](choose-configuration.md).

## Why delegate at all? Rationale

<!-- todo: this section could just as well be titled “Why it's good to let others do work too”, and framed not as main-targeted but as a rank-agnostic collaborative mindset that gets more, better work done within a set budget. -->
The leader agent (the one delegating) already holds all the context, so why not have it just do the work directly? The answer is **context management**. Delegated AI’s have their own context window. They pay tokens with their window while the leader’s stays unused. This gives the leader agent a longer runway.
A good analogy is that context windows are compute capacities, and tokens are processing cycles. 

## Different types of delegation and their tradeoffs

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

## Limited context window as a finite resource

Every agent has a context window. Every context window has a limit. Once that limit is reached, the agent is permanently offline. It can’t work nor communicate. In that sense, a context window is like a fuel tank.

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

Logically, if the task is not large or complex, do not delegate. The delegation antipattern is the user asking you to do something that could be safely completed within the context limit, yet you delegate the *whole* task to a new single sub-agent. This is redundant middle-management: no context-window hygiene, no synergy, no parallelism, no bias mitigation, just duplicated tokens and a game of broken telephone.

## Abstract delegation use case examples

> This is not an exhaustive list. Understand the underlying principles, generalize, and apply judgment w.r.t. your actual task.

These are example implementations of the different, justified types of delegation, as described earlier in this file.

- **Dirty work**: The main agent needs the result of a process, not the process itself. Examples include mapping unknown terrain to identify where to dive deeper; finding where things are or whether they exist at all; conducting research; summarizing topics the delegating agent does not need to understand deeply; implementing a well-defined spec; and so on. These tasks require the executor to consume substantial irrelevant context because the space has not yet been mapped by relevance, creating a fog-of-war situation. Someone has to burn through context and deal with the noise. It is better to assign this work to a throwaway agent and keep the main agent’s context high signal-to-noise. Moreover, due to the read-only nature of these tasks, they can potentially be fanned out and run in parallel.
- **Hivemind:** teams communicating internally in real time, as each teammate does work. Hollywood analogy: elite soldier squad or a team of spies, global channel earpieces, deployed behind enemy lines, each progresses their part, each part essential for completing the mission, global channel earpieces, consistent live updates, uncertainties surfaced to get advice, discussions to make best decisions for mission, path forward of an individual adapts in real time due to new peer finding, HQ available for teammates to surface rare issues that only HQ can or should handle.
- **De-bias:** A reviewer with a fresh context (either paired with the worker in a live team, or dispatched after the fact), informed only of the intent which birthed the work, can spot blind spots and flaws that the worker could not. Related: sometimes a hypothesis is considered true only after it is confirmed independently by multiple actors (consensus).
- **Get more done with less time**: horizontally & more of the same. Readonly tasks are often a strong candidate to fan out as such.
- **Multiple experts over jack(s) of all trades**: horizontally & orthogonal domains.
- **Big picture, smaller picture**: vertical responsibility layers. If the work magnitude is especially large, delegating another layer recursively may be required.
