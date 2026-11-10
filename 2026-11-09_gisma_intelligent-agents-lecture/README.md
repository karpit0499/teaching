# Intelligent Agents: From Decision Theory to Modern Agentic AI

**First session:** Monday, 9 November 2026 (Session 2 follows one to two weeks later)
**Where:** Gisma University of Applied Sciences, Berlin
**Lecturer:** Kumar Arpit
**Format:** two 30-minute sessions: theory with a take-home task, then a live build in n8n Community Edition + Ollama
**Core text:** Kevin P. Murphy, *Probabilistic Machine Learning: Advanced Topics* (MIT Press, 2023 print edition), cited in the slides as "Murphy 2023" / PML2

## The idea in one line

An LLM plus tools plus memory, running in a loop, is how agents are *built*. It is not what makes them *good*. The loop is the body; the decisions made inside it are the intelligence.

## Session 1: The Theory (42 slides)

| Time | Part | Topics | PML2 |
|---|---|---|---|
| 0–7 min | Opening | Four real stories as news clippings: the US–China AI near-miss (Sep 2026), Petrov (1983), OpenAI test agents hacking Hugging Face (Jul 2026), the AI disproof claim for the Exponential Time Hypothesis (Oct 2026). One question: who checks the machine? | |
| 7–11 min | 1. What is an agent? | Definition, agent cycle, three kinds of AI, classical designs, history, POMDP | §34.5.2 |
| 11–19 min | 2. Deciding under uncertainty | Beliefs, expected utility, hard constraints, value of information | §3.2, §34.1–34.2 |
| 19–25 min | 3. Learning to decide | Explore vs exploit, bandits, ε-greedy, Thompson sampling (worked example with three slot machines; Netflix artwork), MDPs, reward hacking (with the Hugging Face case), memory vs learning | §34.4–34.6, §19.7 |
| 25–28 min | 4. Modern architectures | The LLM as policy, tools, memory, skills, MCP and A2A | |
| 28–30 min | Take-home task | Design a budget-aware trip-planning agent; step-by-step setup for n8n Community Edition and Ollama | |

Session 1 deliberately has no Lisbon examples; it uses coding agents and a class party instead.

## Session 2: Build It (22 slides)

| Time | Part | Topics |
|---|---|---|
| 0–8 min | 1. Building reliable agents | When to use an agent, supervisor–worker, judges and bounded loops, code checks and guardrails |
| 8–26 min | 2. Build it together | Seven steps in n8n + Ollama, each with a checkpoint: planner, tool, structured output, budget check in code, routing, LLM judge, feedback with a revision cap and hand-over to a human |
| 26–30 min | 3. Does it work? | Test cases, why a demo is not evidence, where agents are heading |

Running request: *3 days in Lisbon, 600 € budget, nothing before 10:00.*

## What's in this folder

```
2026-11-09_gisma_intelligent-agents-lecture/
├── README.md
├── slides/
│   ├── session-1_theory/
│   │   ├── Session1_Intelligent_Agents_Theory.pptx   ← present this (animations and transitions included)
│   │   ├── Session1_Intelligent_Agents_Theory.pdf    ← read-only copy
│   │   ├── speaker-notes.md
│   │   └── source/                                   ← deck.json, one HTML file per slide, Thompson sampling script
│   └── session-2_build/
│       ├── Session2_Build_It_n8n_Ollama.pptx
│       ├── Session2_Build_It_n8n_Ollama.pdf
│       ├── speaker-notes.md
│       └── source/
├── handouts/
│   ├── assignment-brief_session-1.md   ← take-home task + n8n Community Edition and Ollama setup
│   └── build-sheet_session-2.md        ← the seven build steps with code and checkpoints
├── n8n-workspace/                      ← reserved for the n8n workflow export
└── archive/first-draft_76-slides/      ← the original single 45-minute deck, kept for reference
```

The PowerPoint files embed their fonts (Lato, IBM Plex Mono, Libre Baskerville), so they look the same on any computer running PowerPoint. Keynote and Google Slides ignore embedded fonts.

## Sources for the opening stories

- CNN, 18 Sep 2026 (anonymous sources); Engadget, The Times of Israel, Slashdot
- NPR, 18 Sep 2017; Smithsonian Magazine; Arms Control Association (Petrov)
- [TechCrunch, 26 Jul 2026](https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/); [CBS News, 2 Aug 2026](https://www.cbsnews.com/news/hugging-face-hack-openai-rogue-model/); Reuters, 24 Jul 2026; BleepingComputer, 29 Jul 2026; Al Jazeera, 24 Sep 2026 (Hugging Face)
- Tech Times, XenoSpectrum, The Japan Times, BeInCrypto via Yahoo Tech; the preprint at github.com/openai/math (Exponential Time Hypothesis)

## Photo credits

All photos from Unsplash: Tono Graphy, Cindy F (Session 1); Annamaria Kupo, Timur Seyfelmlyukov (Session 2).

## Notes on accuracy

- Page and section numbers refer to the 2023 print edition of PML2.
- Numbers marked "illustrative" in the slides (traces, the 300 € run) are teaching examples, not data.
- The Thompson sampling draws on Session 1 slides 30–32 come from a seeded random generator; `source/thompson_sampling_example.py` reproduces them.
- Netflix: the artwork bandit and its exploration strategies (ε-greedy, Thompson sampling, UCB) come from Justin Basilico's QCon SF 2018 talk "Artwork Personalization at Netflix". The slides do not claim which algorithm Netflix runs in production.
- The US–China story rests on CNN's anonymous sources; the ETH result was a claim under expert review, not a certified result, as of early November 2026.
