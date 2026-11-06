# Assignment: Build a Budget-Aware Trip Planner Agent

Monday, 9 November 2026 · Kumar Arpit

## Overview

Design an agent that plans a three-day city trip within a fixed budget, then try to build it in n8n Community Edition with a local model from Ollama. Bring your design to Session 2, in one to two weeks, where we build it together.

- **Required:** a one-page design sketch and short answers to three questions.
- **Optional, encouraged:** a first working version in n8n, even a broken one.
- **No real bookings or payments:** the agent only plans.

## The scenario

Your agent receives this request, the same one we build for in Session 2:

> “Plan me a three-day trip to Lisbon. My budget is 600 euros. I love museums and good food, and I hate early mornings.”

Use a small fixed dataset instead of live websites, so every agent can be compared fairly and runs offline. Keep it in one JSON file or an n8n Code node. The sample below is fictional; extend it as you like.

| Type | Name | Price (€) | Notes |
| --- | --- | --- | --- |
| Hotel | Hotel Azul | 110 per night | Central, Alfama |
| Hotel | Casa do Rio | 85 per night | Riverside, 20 min by tram |
| Hotel | Tejo Hostel | 40 per night | Central, shared bathroom |
| Museum | Tile Museum | 8 | Closed Mondays |
| Museum | Modern Art Centre | 12 | Opens 10:00 |
| Museum | Maritime Museum | 10 | Closed Tuesdays |
| Restaurant | Tasca da Esquina | 25 per person | Lunch and dinner |
| Restaurant | Mercado Food Hall | 15 per person | All day |
| Tour | Sunset river cruise | 45 | Daily, 18:00 |

## Requirements

Your agent must do all six. Each one is an idea from the lecture.

| # | Requirement | What it means in practice | Lecture idea |
| --- | --- | --- | --- |
| 1 | Act in a loop | Call at least one tool, for example a search over your dataset, and use the result | The agent cycle |
| 2 | Check the budget in code | A Code node adds up the total and rejects any plan over the user’s budget (600 € here) or with anything starting before 10:00; the LLM never does these checks | Hard constraints vs preferences |
| 3 | Score preferences | Prefer museums and good food; trade them off against cost | Expected utility |
| 4 | Revise, but stop | At most two revisions after the first draft; then stop and hand over to a human | Stop rules, bounded loops |
| 5 | Ask when it matters | If the budget or dates are unclear, ask instead of guessing; don’t ask questions that change nothing | Value of information |
| 6 | Keep a trace | Log each step: tool calls, totals, each revision and why the run stopped | Seeing what the agent did |

## What to bring to Session 2

1. **A one-page design sketch.** Hand-drawn is fine. Show:
   - each agent or node and its one job
   - the tools and the data they read
   - where the budget is checked
   - when the agent stops, revises or asks the user
2. **Short answers to three questions:**
   - Which decisions does the LLM make, and which does code make? Why?
   - The hotel price in your data rises after the plan is drafted. What happens?
   - How would you show that your agent is better than one well-written prompt?
3. **Optional:** your n8n workflow, exported as JSON (Workflow menu → Download). Remove any credentials first.

## Setup

About 25 minutes. Do it before Session 2 so the class time goes into building. You install **n8n Community Edition**, the free, self-hosted version of n8n: no cloud account and no trial. These are the same steps as the last two slides of Session 1.

**Part A: n8n Community Edition (about 15 minutes)**

1. **Install Docker Desktop** from [docker.com](https://www.docker.com/products/docker-desktop/) (Windows, macOS or Linux) and start it.
2. **Create a volume** so your workflows survive restarts, then **start n8n**. Leave the terminal window open:

```bash
docker volume create n8n_data

docker run -it --rm --name n8n \
  -p 5678:5678 \
  -e GENERIC_TIMEZONE="Europe/Berlin" \
  -e TZ="Europe/Berlin" \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

3. **Open http://localhost:5678** and create the owner account (an email and a password; it stays on your laptop).
4. **Optional:** accept n8n’s offer to register the Community Edition. The free licence key unlocks folders and debugging in the editor.

No Docker? With Node.js 20.19 to 24 installed, run `npx n8n` instead ([n8n docs](https://docs.n8n.io/hosting/installation/npm/)).

**Part B: Ollama and the connection (about 10 minutes)**

5. **Install Ollama** from [ollama.com/download](https://ollama.com/download). On Linux: `curl -fsSL https://ollama.com/install.sh | sh`
6. **Pull a model that can call tools** and check it is there:

```bash
ollama pull qwen2.5:7b
ollama list
```

7. **Add the Ollama credential in n8n.** Base URL when n8n runs in Docker: `http://host.docker.internal:11434`. When you used `npx`: `http://localhost:11434` ([n8n docs](https://docs.n8n.io/integrations/builtin/credentials/ollama/)).
8. **Smoke test:** build *Chat Trigger → AI Agent*, attach an *Ollama Chat Model* (qwen2.5:7b) to the agent, open the chat and say hello.

Done when the chat answers and the execution log shows the Ollama Chat Model ran.

If n8n can’t reach Ollama: check that `ollama list` answers; with `npx`, try `127.0.0.1` instead of `localhost`; with Docker on Linux, add `--add-host=host.docker.internal:host-gateway` to the `docker run` command. A 7B model needs about 8 GB of free memory; on a weaker laptop use `qwen2.5:3b` and expect less reliable tool calls.

## Hints from the lecture

- **The LLM proposes, code verifies.** Anything a computer can check exactly (sums, start times, required fields) belongs in a Code node.
- **Constraints are not preferences.** A 680 € plan is not “slightly worse”; it is invalid. Filter first, then pick the best valid plan.
- **Send feedback to whoever caused the problem.** An over-budget plan goes back to the step that chose the hotel, not to the start.
- **Start small.** One agent plus one code check beats five agents you can’t debug. Add a judge only if it earns its cost.
- **Read more:** Murphy, *Probabilistic Machine Learning: Advanced Topics* (2023): §34.1 decisions under uncertainty (pp. 1093–1098), §34.2.3 value of information (pp. 1101–1102), §34.5 Markov decision processes (pp. 1116–1119).
