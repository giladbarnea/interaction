---
name: self-peer-review
description: Dispatch a subagent to review your own committed work
arguments: work_to_review
loads: references/peer-review-instructions.md
---

First, commit your work to have a commit reference. Then dispatch a large subagent (thinking=xhigh if project is medium-sized, thinking=max if large) with the following prompt:

---

The user has given me this task:
<original-user-task>  # Quote verbatim.
{ original user task that resulted in work_to_review }
</original-user-task>

I have attempted to complete it. It’s committed to { commit_sha }.

@references/peer-review-instructions.md <work_to_review> <research_targets="Blast radius of {commit_sha}".>

{ if original user task references skills }
    Load the referenced skills yourself for complete understanding:
    - `skill-1`: `path/to/skill-1/`
    - ...
{ end if }
