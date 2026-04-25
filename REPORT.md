# Project Report: AI-Assisted Development

## 1. Initial Approach

I started very small on purpose: first just a basic Pygame loop, then bouncing squares, then better movement, then flee behavior. I tried to avoid doing everything at once because it gets messy fast when you combine animation + random values + logic rules.

Main assumptions at the start:
- The app should stay simple/readable for a first-year level.
- It is better to build one behavior at a time and test each step.
- If setup is broken, coding new features is a waste of time, so environment checks come first.

## 2. Prompting & AI Interaction

### What worked well

The best prompts were specific and constrained, for example:
- “Add X behavior, don’t add extra features.”
- “Keep it simple and readable.”
- “Explain what changed shortly.”

This made the edits focused and reduced over-engineering.

### Where AI had limits / mistakes

- One journal entry had a formatting/content glitch where a filename in the summary line was missing.
- `requirements.txt` was initially in a weird encoding format and had to be normalized to plain UTF-8.
- A few generated comments/constants became noisy or unused after later refactors, so cleanup was needed.

### Why those issues happened

Most issues came from iterative changes stacking up over time (many small edits, changing requirements). AI was useful for speed, but I still had to review outputs, keep prompts tight, and ask for cleanup passes.

## 3. Key Learnings

### Technical skills I practiced

- Pygame game loop structure (`events -> update -> draw`).
- Edge bouncing with direction inversion.
- Using per-object data in dictionaries (size, speed, color, position).
- Basic behavior logic (smaller squares fleeing bigger nearby squares).
- Time-based movement with `dt` so movement scales better with frame timing.

### What I learned about using AI better

- Ask for one thing at a time.
- Always verify with a quick run/error check after each feature.
- Periodically request cleanup (comments, unused constants, readability).
- Treat AI as a fast coding partner, not an autopilot.

If I do another project like this, I’ll keep the same workflow: small increments, explicit constraints, frequent checks, and short reflection notes after each step.