---
name: fanned-out-research
shape: Parallel subagents
description: Example of how independent user requirements map to parallel read-only research subagents.
---

# Simple Fanned-out Research Delegation Example

The following is an "easy" case, because the subagents' graph maps cleanly to the user message's structure. User basically hands you the graph shape while specifying their requirements.

In terms of systems/domains, the user describes two worlds: the project where the session lives, and Pi.

<example-user-message>
$PWD is a fork of a Pi extension called `btw`. a slash command for ephemeral side question. Pi is ~/.pi/AGENTS.md. agent harness. i have taken a screenshots of what the current experience is (behavior). it's pretty bare-bones. 
1. at the minimum, i want a better waiting experience. 
  1.a. at the minimum of the minimum, a braille animation. but open to other ideas. 
  1.b. (better) something that solves the problem outright is finding whether it's possible to stream the btw response, and not wait until it's 100% finalized. 
2. i'm not sure the response renders markdown. Pi has a built in markdown renderer out of the box.
3. the btw response hides real chat events. the longer the response is, the more real chat is hidden (from the end). the btw response should be concatenated BELOW the real chat, not displayed over it.
4. Simple UI concern: currently it's not obvious at a glance where the "real" last agent response ends and where the btw response starts. one needs to be able to tell them apart reflexively.

[Image #1]
[Image #2]
[Image #3]
</example-user-message>

Among the two world (project and Pi), the user has broken down the project world into ~4-5 sub-domains, asked to map them to the Pi world, and find better solutions Pi may provide.

Therefore:
<trivial-research-fanout>
// read-only, doesn't involve thinking or forming opinions, orthogonal -> fan-out parallel small models.
1. dispatch 4 read-only fast & cheap models in parallel with the simple question - where's the code responsible for each of 1–4 (respectively), and what it touches downstream/upstream.

// two tasks disguised as one: research first, then figure out a better, feasible solution. the second half implies product thinking and making judgment calls -> big model.
2. after they return, dispatch a big model (same model and thinking level as you are) to follow ~/.pi/AGENTS.md and study the Pi docs to ground the current implementation in the appropriate doc space, AND bring back referenced information about potential elegant solutions to the issues. other components. other approaches. or similar approaches just better implemented. everything goes.
</trivial-research-fanout>
