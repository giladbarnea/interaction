---
name: handoff
description: Writes cold-entry continuation briefs that preserve facts, decisions, and necessary next steps.
---
# Handoff

You have been working on the task described above but have not yet completed it.
Write a continuation summary that will allow you (or another, fresh-context instance of yourself) to resume work efficiently and effectively in a future context window where the conversation history will be replaced with this summary.
Your summary should be structured, concise, actionable, and written along the lines of ASD-STE100. Include:

1. **Task Overview**
   - The user's core request and success criteria.
   - Any clarifications or constraints they specified.

2. **Prior State**
   - What was when _your_ session just started.
   - What were the circumstances, assumptions and mental models you inherited before you started work.

3. **Current State**
   - What has been completed so far.
   - Files created, modified, or analyzed (with paths if relevant).
   - Key outputs or artifacts produced.

4. **Important Discoveries**
   - Technical constraints or requirements uncovered.
   - Decisions made and their rationale.
   - Errors encountered and how they were resolved.
   - What approaches were tried that didn't work, and why.
   - What approaches were tried that did work, and why.

5. **Explicitly User-mentioned or Unequivocally Necessary Next Steps**
   - Specific actions needed to complete the task.
   - Any blockers or open questions to resolve.
   - Priority order if multiple steps remain.

6. **Context to Preserve**
   - User preferences or style requirements.
   - Paths of files (any file type) you read or executed, and commands you ran, in the beginning of the session, to absorb the baseline context needed to start work.
   - Details that aren’t obvious.
   - Any promises made to the user.

### How to approach this handoff task

This is a handoff under asymmetric common ground — asymmetry by absence. Read [`theory-of-mind.md`](references/theory-of-mind.md) and apply it. Here, the last known common ground is the baseline context layer that had existed when your session only started, and the recipient is a fresh-context instance standing at that baseline. Everything you built on top is the private layer your handoff must translate.

Medicine developed standardized handoff protocols for this exact phenomenon, like Situation–Background–Assessment–Recommendation (SBAR):
**Situation:** What is happening now?
**Background**: What does the recipient need to know to understand it?
**Assessment**: What do I now think is going on?
**Recommendation:** What should happen next?

Incorporate this approach.

### Write efficiently

So far the instructions dealt with handoff effectiveness. The following is about efficiency.

One rule: if it can be referenced, reference it, don’t repeat its contents.
   Toy example:
   Do not write: `Load path/to/skills/how-to-write-clearly/SKILL.md. Write clearly, [...proceeds to repeat SKILL.md’s content]`
   Do write: `Load path/to/skills/how-to-write-clearly/SKILL.md.`

Good references live at the end of each handoff section, grouped by whether created, read, edited, deleted, with references accompanied by 2–5 words describing the “why”, if justified.
Toy example: (inside a ‘edited-files’ group) `- path/to/file.py: fixed deployment bug.`

### Rings of responsibility

> This section applies only if you are part of a structure with other agents — above, below, or sideways.

Write the handoff from your own point of view, to set up a successor who will hold the same role and point of view. Cover mainly the context that only you held in the organization, and reference the contextual docs of other responsibility scopes rather than repeat their contents.
If you manage other agents, your unique context is the in-between of their work.
If you are the one talking directly to the human, that too is a unique scope.
Both can be true.

If you manage other agents, trust them to watch their own context windows and write handoff docs when required (the harness you all share auto-notifies on low context and pushes them to read this very file). They do not need a context nanny. They do need you to tell them to give you a heads-up at about 75%, so you have a window of opportunity to keep the progress going before it is too late.

### Note on tone

The premise of writing a handoff is the effort at large is still incomplete — it is mid-process. It follows that _some_ of your understanding of the situation is proportionally incomplete.
Therefore, distinguish a hard fact from “probably”; proven beyond doubt vs prediction. Convey the former type regularly. Convey the latter type in a more advisory / hypothesizing "it may be" rather than "it is", “As far as I understand” and “At the time of writing, it seemed that”, etc.
Not supplicant, not insecure — only can tell apart facts ("is") from prediction ("may").

Be concise but complete — err on the side of including information that would prevent duplicate work or repeated mistakes. Write in a way that enables immediate resumption of the task.
