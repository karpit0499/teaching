# Intelligent Agents: From Decision Theory to Modern Agentic AI

**Class date:** Monday, 9 November 2026
**Where:** Gisma University of Applied Sciences, Berlin
**Lecturer:** Kumar Arpit
**Format:** 45-minute lecture with a live look at an n8n + Ollama multi-agent workspace
**Core text:** Kevin P. Murphy, *Probabilistic Machine Learning: Advanced Topics* (MIT Press, 2023 print edition), cited in the slides as "Murphy 2023" / PML2

## The idea in one line

An LLM plus tools plus memory, running in a loop, is how agents are *built*. It is not what makes them *good*. The loop is the body; the decisions made inside it are the intelligence.

Running example throughout: *"Plan me a three-day trip to Lisbon. My budget is 600 euros. I love museums and good food, I hate early mornings, and here's a hotel I liked."*

## Session plan

| Time | Part | Topics | PML2 |
|---|---|---|---|
| 0–3 min | Opening | Running example, central argument | |
| 3–9 min | 1. What is an agent? | Definition, agent cycle, three kinds of AI, classical architectures, history, POMDP | §34.5.2 |
| 9–16 min | 2. Deciding under uncertainty | Beliefs, expected utility, constraints, value of information, explore vs exploit, regret, fairness, test and roll, Empirical Bayes | §3.2, §3.7, §34.1–34.4 |
| 16–21 min | 3. Learning to decide | Bandits, UCB, Thompson sampling, contextual bandits, MDPs, return, planning, active learning | §34.4–34.7 |
| 21–26 min | 4. Learning from feedback | RL families, reward design and hacking, RLHF, continual learning, memory vs learning, hallucination | §19.7, §22.4.1, Ch. 35 |
| 26–30 min | 5. Modern agentic architectures | Reasoning loops, tools, skills, memory, multimodal, multi-agent, MCP and A2A, failure modes | §22.4, §34.5.2 |
| 30–40 min | 6. Building reliable agents | When to use an agent, supervisor–worker, judges and bounded loops, code checks, guardrails, escalation, then the live n8n + Ollama workspace | §19.3, §34.1 |
| 40–43 min | 7. Evaluation and impact | Two causal questions, demos vs evidence, randomised trials, applications, risks, case study | Ch. 36 |
| 43–45 min | 8. Future of AI | Long-horizon tasks, verifiable rewards, continual learning, world models, discussion | §19.7, §34.7, §35.4 |

## What's in this folder

```
2026-11-09_gisma_intelligent-agents-lecture/
├── README.md                ← this file
├── slides/
│   ├── Intelligent_Agents_Lecture_2026-11-09.pdf   ← the 76-slide deck as presented
│   ├── speaker-notes.md     ← notes for every slide, in order
│   └── source/              ← slide source (deck.json + one HTML file per slide)
└── n8n-workspace/           ← reserved for the n8n + Ollama travel-planner workflow export
```

The slides were built in the Gisma lecture style (white logo panel, cyan title bar, reference and page box). The `source/` files are the editable slide definitions; images in them point to hosted assets, so the PDF is the version to read.

## Photo credits

All photos from Unsplash: Timur Seyfelmlyukov, Daniel van den Berg, Cindy F, Tono Graphy, Annamaria Kupo.

## Notes on accuracy

- Page and section numbers refer to the 2023 print edition of PML2.
- Numbers marked "illustrative" in the slides (regret bars, fairness bars, forgetting bars, trace snippets) are teaching examples, not data.
- The case study (slide 71) is based on a CNN report of 18 September 2026 citing anonymous sources; no on-record official confirmation was reported.
