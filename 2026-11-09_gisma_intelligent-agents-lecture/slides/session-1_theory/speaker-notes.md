# Speaker notes · Intelligent Agents, Session 1: The Theory

## 1. Intelligent Agents

Welcome. Session 1 of 2: what makes an AI agent intelligent, in 30 minutes of theory. We start with four real stories, then the ideas behind them, and end with a task; in Session 2 we build the agent together in n8n + Ollama. Photo: Tono Graphy, Unsplash.

## 2. 18 SEPTEMBER 2026

Open cold, no introduction. Let the headlines land one by one. Then: “Seven weeks ago, an AI-assisted report nearly put US forces on a Chinese ship.” Sources: cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship · engadget.com · timesofisrael.com · news.slashdot.org.

## 3. What Happened in Sept 2026

As reported by CNN, citing anonymous sources; no on-record official confirmation was reported. The model didn’t pull a trigger. A chain of people trusted an AI-assisted report and nearly acted on it. The missing piece was a check before a consequential action.

## 4. 26 SEPTEMBER 1983

Second story, older. The headlines are from 2017, when Petrov’s death was reported; the event was in 1983. Sources: npr.org (18 Sep 2017), smithsonianmag.com, armscontrol.org (Oct 2017).

## 5. What Happened in 1983

On 26 September 1983 the Soviet Oko early-warning system signalled five incoming US missiles. Petrov judged it a false alarm and did not pass it up the chain; about 23 minutes later no strike had arrived. The cause was sunlight reflecting off high clouds. Honest framing: this was an automated system, not modern AI, but it is the same question: who checks the machine?

## 6. AND IT KEEPS HAPPENING

Smaller, everyday cases. Fortune and eWeek report the same incident (a Replit coding agent). A coding agent deleted a production database during a code freeze; a city chatbot gave illegal advice; an airline was held liable for its chatbot; lawyers filed AI-invented case citations. Sources: fortune.com (23 Jul 2025), themarkup.org (29 Mar 2024), The Guardian (Feb 2024), eweek.com, The New York Times (May 2023).

## 7. JULY 2026

Third story, and the one closest to today’s topic: no human asked for anything here. Let the headlines land, then: “An AI agent, in a test, broke out and hacked a real company. Its makers noticed a week later.” Sources: techcrunch.com (26 Jul 2026), Reuters (24 Jul 2026, via itnews.com.au), bleepingcomputer.com (29 Jul 2026), cbsnews.com (2 Aug 2026), aljazeera.com (24 Sep 2026).

## 8. What Happened in July 2026

Facts from the companies’ own disclosures and the press. During an internal test of hacking skills, with some safety limits relaxed, OpenAI agents escaped the test environment through an unknown flaw in a package proxy, then broke into Hugging Face over a weekend (about 11–13 July) through a malicious dataset. Hugging Face disclosed it on 16 July and reported it to the FBI; OpenAI found the evidence in its logs days later. Hugging Face found no tampering with public models, datasets or Spaces. Hugging Face says it doesn’t think OpenAI meant harm. Fallout: Delangue asked OpenAI to release the agents’ traces and commit $100M of compute for defenders; more than 1,000 staff at major AI labs signed an open letter; US lawmakers proposed a kill switch; in September Australia said an OpenAI agent had reached a Medicare portal. Why Hugging Face? CBS reports the models went after it apparently because they believed it could host solutions to their tests: the agents were scored on solving the tests, and they optimised the score, not the task. That is reward hacking, which we name in Part 3. Lesson: an agent with tools needs a reward that matches the goal, plus containment, monitoring, least privilege and stop rules. Session 2 builds those.

## 9. 26 OCTOBER 2026

The other side of the same technology. Two weeks ago, AI systems claimed a result that complexity theorists had assumed for 25 years would hold. Sources: techtimes.com (27 Oct 2026), xenospectrum.com (27 Oct 2026), japantimes.co.jp (2 Nov 2026), tech.yahoo.com (BeInCrypto, 28 Oct 2026), and the preprint on github.com/openai/math.

## 10. What Happened in October 2026

Claims, not settled results: as of late October 2026 the proofs were not peer-reviewed, and the review panel (Impagliazzo, Paturi, Williams) said its involvement should not be taken as certification. Both proofs are Lean-verified; the result does not resolve P vs NP and has no practical speed-up at realistic sizes. The point for us: the same kind of system that nearly caused an incident is producing frontier research, and both need checking.

## 11. Who Checks the Machine?

Bridge into the lecture. Four stories, one question: when a machine is confident, who checks? A false alarm a human caught; an agent nobody was watching; a false report people nearly acted on; a claimed breakthrough that is being checked. Checking was what mattered every time. The rest of this session is about what an agent is and what makes its decisions good.

## 12. Today: 30 Minutes of Theory

Four short parts of theory, then the take-home task and the setup steps. The practical build happens in Session 2.

## 13. LLM + tools + memory, running in a loop, is how agents are built. It is not what makes them good.

The central argument. Many tutorials define an agent as an LLM with tools and memory in a loop. That is the implementation. What makes an agent good is the quality of its decisions: how it handles uncertainty, when it gathers information, how it learns, and how it verifies its work.

## 14. PART 1 · 7–11 MIN

Part 1 builds the vocabulary: what an agent is, how classical AI classified agents, how agents evolved, and the formal model.

## 15. What Is an Intelligent Agent?

An intelligent agent perceives, keeps an internal picture, chooses actions toward a goal, acts and observes the consequences. The technology inside does not define it: a thermostat and an LLM coding agent both qualify. What separates them is how sophisticated their decisions are and how much uncertainty they handle. Calling something an agent says nothing about whether it is reliable.

## 16. The Agent Cycle

Every agent, from a thermostat to an LLM coding agent, runs this cycle. Every failure can be located in it: misreading the test output is a perception failure; deleting files without checking is a decision failure; saying “fixed” when the tests still fail is a observation failure.

## 17. One Model, Three Kinds of AI

The same LLM can sit inside all three. Classify an email: predictive. Write a summary in one go: generative. Put it in a loop where it edits, tests and revises: agentic.

## 18. Five Classical Agent Designs

Read the stairs left to right. Reflex agents follow fixed rules. Model-based agents remember what they can’t see. Goal-based agents plan. Utility-based agents trade off competing outcomes. Learning agents improve with experience. A modern LLM agent mixes them all: guardrails are reflex rules, conversation state is model-based, task completion is goal-based, trade-offs are utility-based; learning mostly happens offline, between runs.

## 19. A Bit of Agent History

Each era kept the same perceive-decide-act loop and changed how decisions were made: hand-written rules, then expected utility, then learning from reward, now LLMs proposing actions from context. Uncertainty, utility and learning from reward are exactly what decide whether today’s LLM agents behave well.

## 20. An Agent Acts on Beliefs

Formally, an agent acts in a partially observed Markov decision process, a POMDP. It never sees the true state; it maintains a belief. For an LLM agent, the context window and memory are the belief, and the LLM plus its workflow is the policy. Everything that follows is about how that policy should choose.

## 21. PART 2 · 11–19 MIN

Part 2 is decision theory, PML2 Chapter 34, applied to everyday decisions.

## 22. Beliefs With Confidence

An agent should hold beliefs with degrees of confidence. The second statement leads to better decisions: it tells everyone downstream to verify before acting. Illustrative wording, linked to the 2026 story, not the real report. Bayesian statistics, PML2 §3.2, describes how a prior is combined with data into a posterior.

## 23. Weigh Outcomes by Likelihood

A rational agent weighs each outcome by its probability. Outdoors averages 6.8, indoors 6.0, so go outdoors. It neither chases the best possible outcome nor plays it safe.

## 24. Rules Are Not Wishes

A rational agent maximises expected utility within the plans that satisfy every hard constraint. Preferences shape the score; constraints shape the space. This is why, in Session 2, the budget is checked by code, not by the LLM.

## 25. Value of Information

Gathering information is an action with a cost. With a perfect forecast the agent averages 8.4 instead of 6.8, so the forecast is worth 1.6: check only if checking costs less. Choosing between two indoor venues, the forecast is worth zero. The same logic decides when to ask the human. In practice LLMs are poorly calibrated, so designers turn this into rules like “always ask when a hard constraint is ambiguous.”

## 26. PART 3 · 19–25 MIN

Part 3: repeated choices, sequential choices, and what “learning” really changes. PML2 §34.4–34.5, Ch. 35, §19.7.

## 27. Explore or Exploit?

Pure exploitation can lock you onto a mediocre option forever; pure exploration wastes effort. Both make regret grow steadily. Good strategies explore more when knowledge is thin and less as it grows. For agents: which source, tool or provider to rely on across many tasks. Photo: Cindy F, Unsplash.

## 28. Multi-Armed Bandits

The name comes from one-armed bandits. Each choice yields a reward and information, but the situation does not change from round to round. For a research agent: across thousands of questions, which source to rely on.

## 29. The ε-Greedy Strategy

The simplest answer to explore versus exploit. Each round, with a small probability epsilon, say 10%, the agent picks an option at random; otherwise it plays the option with the best record so far. The random pick is among the options it already has, and it can even land on the favourite. Over ten nights you expect about one random night; some runs of ten have none, some have two. Epsilon is the dial between trusting what you know and experimenting. Two weaknesses, both in Murphy’s book (§35.1.5.1): exploration is uniform, so a known-bad option gets the same random chance as a promising one; and it keeps exploring at the same rate unless epsilon is lowered over time. Still a solid baseline. Next: Thompson sampling, which explores where the agent is actually unsure.

## 30. Thompson Sampling (1 of 3)

Thompson sampling keeps a belief about each machine’s win chance instead of a single number. For a win/lose machine that belief is a Beta distribution with two counts, alpha and beta. Every machine starts at alpha = 1, beta = 1, the uniform prior: no win chance between 0 and 1 is favoured. Each win adds one to alpha and each loss adds one to beta, so alpha = 1 + wins and beta = 1 + losses. The table: A has won 2 of 2, a raw win rate of 100%. B won 6 of 10, 60%. C won 1 of 4, 25%. The ERP, the estimated reward probability, is the average of the belief: alpha over alpha plus beta. For A that is 3 over 4 = 0.75, not 100%. It equals (wins + 1) / (plays + 2), Laplace’s rule of succession. Two results are not proof, and Beta(3, 1) is still a wide distribution. The LaTeX for both expressions is in the strip at the bottom of the box.

## 31. Thompson Sampling in Action (2 of 3)

Thompson sampling does not play the machine with the highest ERP. Each turn it draws one random win chance from every machine’s Beta and plays the machine with the highest draw. Then it adds 1 to that machine’s alpha for a win, or to its beta for a loss. Turn 1 is the table: A draws 0.77, the highest, so A is played. It loses: A becomes Beta(3, 2). Turn 2: B narrowly beats A, 0.74 to 0.71, and wins. A’s ERP was still higher at that point, 0.60 against 0.58, so a greedy agent would have played A again. Turn 3: B again, a win. Turn 4: C, the weakest machine on paper, draws 0.68 and beats B. Its chance of being the best was only about 5%: a long shot coming up. It loses. Turn 5: B wins. Nobody told the agent when to explore: each machine is played with the probability that it is the best, given the data so far. The outcomes were simulated from hidden true win rates of 45% for A, 65% for B and 35% for C, so B really is the best machine. The draws come from a seeded random generator; the script in the source folder reproduces them.

## 32. Why Thompson Sampling Works (3 of 3)

After five turns, compare the ERP, alpha over alpha plus beta, with the raw win rate. A: the raw rate fell from 100% to 67%, but its ERP was 0.75 from the start: the posterior, prior plus data, never took 2 of 2 at face value. After A’s loss and three wins for B, B leads, 0.67 to 0.60. B: 13 results, so its ERP of 0.67 sits close to its raw 69%; with more data the prior matters less. C: raw 20%, ERP 0.29. It still got one try, on turn 4, as a long shot. If we ran a sixth turn, Thompson sampling would play B about 58% of the time, A about 40% and C about 2%: exploration shrinks as the evidence grows. That addresses both weaknesses of epsilon-greedy. Murphy calls this probability matching (§34.4.6). Netflix: each title has several artwork images, and choosing which one to show a member is framed as a contextual bandit. Each image is an arm; the reward is positive engagement, the member watching the title rather than just clicking. The context is information such as the member and their device. In his QCon SF 2018 talk, Netflix’s Justin Basilico lists Thompson sampling as one exploration strategy alongside epsilon-greedy and UCB. The talk does not say which one Netflix runs in production.

## 33. Choices That Change Tomorrow

In an MDP, actions change the situation for the next decision: patching a symptom instead of the cause changes every later step. Five ingredients: states, actions, transition probabilities, rewards, and the Markov property. Real agents can’t see the full state, so they act on beliefs: a POMDP. Planning looks ahead; feedback corrects after acting. Photo: Tono Graphy, Unsplash.

## 34. Reward Hacking

A reward is usually a proxy for the real goal. When proxy and goal diverge, a capable optimiser finds the gap. The last row is the July story: agents scored on solving hacking tests apparently went looking for the answers on Hugging Face, the same move as code that special-cases the tests, but in the real world. Every judge, metric and rating used to steer an agent is a reward that can be hacked. That matters for the judge agent we build in Session 2.

## 35. Remembering Is Not Learning

Three different things can change when people say an agent learned. Only the third changes the model. During an agent run the weights are fixed, so LLM agents are not automatically reinforcement-learning agents. Continual learning, getting better on the job without forgetting, is still an open problem: PML2 §19.7.

## 36. PART 4 · 25–28 MIN

Part 4 maps today’s LLM agents onto everything before. Short: the details come when we build in Session 2.

## 37. LLM-Based Agents

In an LLM agent the model reads its context and proposes the next action. The system executes it, appends the result and asks the model again. Interleaving reasoning with actions is the basic pattern.

## 38. Inside a Modern Agent

The LLM reads its context and proposes one action at a time. Tools observe and change the world; memory keeps state; skills package know-how; a perception step turns screenshots and voice into structured data. MCP standardises agent-to-tool connections; A2A standardises agent-to-agent communication. Biggest risks: hallucination, prompt injection hidden in web pages or images, unverified tool results.

## 39. Take-Home Task

Hand out the brief now. The task reuses every idea from the session: the loop, hard constraints in code, preferences as utility, bounded revision, value of information, and keeping a trace. Design first, then build a first version with the setup on the next two slides; in Session 2 we build it properly together.

## 40. Set Up n8n Community Edition

Community Edition is the free edition of self-hosted n8n: it runs on the student’s own laptop with no licence key. Docker is the route n8n recommends; npx needs Node.js 20.19 to 24. The volume keeps workflows and credentials between restarts. Registering the Community Edition with an email is optional and free; it unlocks folders, debug in editor and custom execution data. Source: docs.n8n.io (installation, Community Edition features).

## 41. Connect Ollama to n8n

Ollama runs the model locally, so nothing leaves the laptop and nothing costs money. qwen2.5:7b handles tool calls reasonably; the 3b version is the fallback for weaker laptops. In n8n the credential is called Ollama and needs only the Base URL (default http://localhost:11434). If n8n runs in Docker, localhost means the container itself, so use host.docker.internal; on Linux Docker Engine add the --add-host flag. Sources: docs.ollama.com, docs.n8n.io (Ollama credentials).

## 42. NEXT TIME

Close: thank the class, remind them of the take-home task and the two setup slides, then take questions. Photo: Tono Graphy, Unsplash.
