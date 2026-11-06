# Speaker notes

Intelligent Agents: From Decision Theory to Modern Agentic AI · Gisma · 9 November 2026

## 1. Intelligent Agents

Welcome. Today: what makes an AI agent intelligent, from decision theory to the agents you can build today. One running example, a trip to Lisbon, carries every concept. 45 minutes, including a live showcase of a multi-agent system built with n8n and Ollama. Photo: Annamaria Kupo, Unsplash.

## 2. The Next 45 Minutes

Eight parts, read top to bottom, left to right. Minutes are shown on the right of each part. Part 6 ends with a live look at my n8n + Ollama workspace.

## 3. Our Running Example

This is our running example: text, a budget, preferences, an image. Every concept today answers one question: what would this travel agent need in order to handle this request well? Photo: Daniel van den Berg, Unsplash.

## 4. The loop is the body.

The central argument. Many tutorials define an agent as an LLM with tools and memory in a loop. That is the implementation. What makes an agent good is the quality of its decisions: how it handles uncertainty, when it gathers information, how it learns, and how it verifies its work.

## 5. What Is an Agent?

Part 1 builds the vocabulary: what an agent is, how classical AI classified agents, how agents evolved, and the formal model we use for the rest of the lecture.

## 6. What Is an Intelligent Agent?

An intelligent agent perceives, keeps an internal picture, chooses actions toward a goal, acts and observes the consequences. The technology inside does not define it: a thermostat and an LLM travel planner both qualify. What separates them is how sophisticated their decisions are and how much uncertainty they handle. Calling something an agent says nothing about whether it is reliable.

## 7. The Agent Cycle

Every agent, from a thermostat to an LLM travel planner, runs this cycle. Every failure can be located in it: misreading the screenshot is a perception failure; booking without checking is a decision failure; saying “booked” when nothing was booked is a feedback failure.

## 8. From Chatbot to Agent

The same model can be either. Give the chatbot the ability to search hotels, check the total against the budget, notice the overrun and revise, and it becomes an agent: it acts, observes the result of its action and changes what it does next.

## 9. Same Model, Three Kinds of System

The same LLM can sit inside all three. Classify a review: predictive. Write an itinerary in one go: generative. Put it in a loop where it searches, checks and revises: agentic.

## 10. Classical Agent Architectures

Classical AI describes a ladder of agent designs; each step adds one capability. Reflex agents only react. Model-based agents keep state. Goal-based agents plan toward an explicit goal. PML2 does not cover this taxonomy; its formal model of agents is §34.5.

## 11. Classical Agent Architectures

Utility-based agents can trade off competing objectives because they score outcomes. Learning agents contain a critic and a learning element. Today’s LLM agents combine all five designs in one system.

## 12. Five Classical Agent Designs

Read the stairs left to right. Reflex agents follow fixed rules. Model-based agents remember what they can’t see. Goal-based agents plan. Utility-based agents trade off competing outcomes. Learning agents improve with experience. A modern LLM agent mixes them all: guardrails are reflex rules, conversation state is model-based, task completion is goal-based, trade-offs are utility-based.

## 13. A Bit of Agent History

Each era kept the same perceive-decide-act loop and changed how decisions were made: hand-written rules, then expected utility, then learning from reward, now LLMs proposing actions from context. Uncertainty, utility and learning from reward are exactly what decide whether today’s LLM agents behave well.

## 14. A Bit of Agent History

Era 1 decided with hand-written rules and logical planning: Shakey and STRIPS, expert systems such as MYCIN. Transparent but brittle when the world differs from the rules. Era 2 reframed AI as designing rational agents that maximise expected outcome given beliefs; BDI architectures modelled beliefs, desires and intentions.

## 15. A Bit of Agent History

Era 3: agents learned policies from reward: TD-Gammon, DQN on Atari, AlphaGo. Superhuman when reward is clear and practice is cheap. Era 4: an LLM proposes the next action from its context; ReAct, tool calling, MCP for tools, A2A between agents. The new era needs the old ideas: uncertainty, utility and learning from reward decide whether LLM agents behave well.

## 16. An Agent Acts on Beliefs

Formally, an agent acts in a partially observed Markov decision process, a POMDP. It never sees the true state; it maintains a belief. For an LLM agent, the context window and memory are the belief, and the LLM plus its workflow is the policy. Everything that follows is about how that policy should choose.

## 17. Deciding Under Uncertainty

Part 2 is decision theory, PML2 Chapter 34. Every idea is applied to the Lisbon trip.

## 18. Beliefs With Confidence

An agent should hold beliefs with degrees of confidence. The second statement leads to better decisions: it tells the agent that checking the current price may be worthwhile and warns the user. Bayesian statistics, PML2 §3.2, describes how a prior is combined with data into a posterior.

## 19. Utility and Rational Choice

A utility is a number expressing how good an outcome is for the person served. A rational agent chooses the action whose outcomes, weighted by probability, are best on average: maximising expected utility. Next slide: the worked example.

## 20. Weigh Outcomes by Likelihood

A rational agent weighs each outcome by its probability. The hike averages 6.8, the museum 6.0, so pick the hike. It neither chases the best possible outcome nor plays it safe.

## 21. Rules Are Not Wishes

A rational agent maximises expected utility within the plans that satisfy every hard constraint. Preferences shape the score; constraints shape the space. This is why, in the demo, the budget is checked by code, not by the LLM.

## 22. Value of Information

Information is valuable only to the extent that it could change your decision. With a perfect forecast the agent picks the hike on sunny days and the museum on rainy days, averaging 8.4. Next slide: the value of that information.

## 23. Value of Information

Gathering information is an action with a cost. With a perfect forecast the agent averages 8.4 instead of 6.8, so the forecast is worth 1.6: check only if checking costs less. Choosing between two indoor museums, the forecast is worth zero. The same logic decides when to ask the human. In practice LLMs are poorly calibrated, so designers turn this into rules like “always ask when a hard constraint is ambiguous.”

## 24. When Should an Agent Ask?

A good human travel agent asks whether 600 € is a hard limit, because the answer could change the plan, and never asks your shoe size. In theory an agent could compute this exactly; in practice LLM confidence is poorly calibrated, so designers write rules.

## 25. Explore or Exploit?

Pure exploitation can lock you onto a mediocre option forever; pure exploration wastes effort. Both make regret grow steadily. Good strategies explore more when knowledge is thin and less as it grows. For agents: which source, tool or provider to rely on across many tasks. Photo: Cindy F, Unsplash.

## 26. Regret: Measuring Decision Quality

Regret is the gap between what the agent achieved and what it would have achieved knowing the best option from the start. It is the natural yardstick for exploration strategies. PML2 also uses it in §34.3.1.

## 27. Fairness in Decision-Making

If the agent maximises average satisfaction, it may consistently serve a minority badly. PML2 describes fairness definitions as decision-theoretic constraints; several reasonable definitions exist and often cannot all be satisfied at once.

## 28. Optimal Sample Size: Test and Roll

Testing on more users gives more certainty, but every test user who gets the worse version pays a cost, and could have had the better one if the decision were made earlier. PML2 shows an optimal sample size that balances these costs.

## 29. Test and Roll: A Worked Example

Worked example with a prior spread of about 5 percentage points. If a difference is too small to detect cheaply, it is probably too small to matter much: pick the apparent winner and move on. The question is which testing plan maximises total benefit to all users.

## 30. Empirical Bayes: Borrowing Strength

Empirical Bayes estimates the prior from the whole population of similar cases, then combines it with each case’s own data. Cases with little data are pulled strongly towards the average: shrinkage. Here the prior counts like ten typical reviews. PML2’s A/B example (§34.3.2) estimates its prior from about 2,000 past experiments.

## 31. Recap: Three Tools From the Book

Fairness: the objective decides who is served well; equal opportunity and equalised odds can’t always both hold. Sample size, worked example: 10,000 future requests, about 60% baseline success, prior spread of 5 percentage points. Test-and-roll gives about 423 requests per version; a classical power analysis (80% power, 5-point difference) asks for about 1,500. Empirical Bayes: if the prior counts like ten typical reviews, (2×5 + 10×4.0) ÷ 12 ≈ 4.17.

## 32. Learning to Decide

Part 3 moves from one-off choices to repeated choices (bandits) and choices that change the future (MDPs). PML2 §34.4–34.7.

## 33. Multi-Armed Bandits

The name comes from one-armed bandits. Each choice yields a reward and information, but the situation does not change from round to round. For the travel agent: across thousands of requests, which information source to rely on.

## 34. Two Bandit Strategies

UCB adds an uncertainty bonus: options tried rarely have wide ranges and a high plausible best, so they get explored; options tried often and doing poorly drop out. Thompson sampling samples from the posterior and picks the winner of the sample. In the chart, bars are plausible ranges and the dark line is the current average.

## 35. Two Smart Ways to Explore

Bandits: repeated choices where your choice doesn’t change the situation. UCB adds an uncertainty bonus to rarely tried options. Thompson sampling chooses each option with the probability that it is the best. The chart is illustrative: agents that never or always explore keep accumulating regret; Thompson sampling’s regret grows more and more slowly.

## 36. Contextual Bandits

In a contextual bandit the agent sees the context, then chooses. This is the model behind most recommendation systems and online advertising. Each decision is still made fresh: the choice does not change future situations.

## 37. Choices That Change Tomorrow

In an MDP, actions change the situation for the next decision: booking a hotel in Belém changes travel times for every later activity. Five ingredients: states, actions, transition probabilities, rewards, and the Markov property. Real agents can’t see the full state, so they act on beliefs: a POMDP. Planning looks ahead; feedback corrects after acting. Photo: Tono Graphy, Unsplash.

## 38. Markov Decision Processes

An MDP has states, actions, transition probabilities and rewards, plus the Markov property: you need only the current state, not the full history, to decide what to do next.

## 39. Short-Term vs Long-Term Reward

In an MDP the agent cares about the return: the total, often discounted, reward over time. A greedy agent books the cheap 6 a.m. flight; an agent that considers the return does not. A value function estimates how good it is to be in a state considering everything that can follow.

## 40. Planning and Feedback Loops

Planning looks ahead with the agent’s current model; value iteration repeatedly asks “what is the best I can do from here, given my current guesses for the next states?” until the guesses stop changing. Feedback corrects after acting. Good agents combine both.

## 41. Active Learning

Active learning chooses which labels to request next, focusing on the most uncertain examples. It is value of information applied to learning, and the idea behind AI that chooses the next experiment. Human-in-the-loop: humans correct, approve and label at selected points.

## 42. Learning From Feedback

Part 4 separates the different meanings of “learning” and shows what changes in each. PML2 Chapter 35, §22.4.1 and §19.7.

## 43. Reinforcement Learning

Reinforcement learning learns a policy from rewards obtained by acting. The agent is not told the correct action; it discovers which actions lead to high reward over time, facing the exploration–exploitation trade-off in its sequential form.

## 44. Three Families of RL Methods

Value-based methods learn action values (Q-learning, DQN). Policy-based methods adjust the policy directly; PPO is in §35.3.4. Model-based methods learn a model of the world and plan with it. Imitation learning learns from demonstrations instead of rewards.

## 45. Reward Design

In RL the agent optimises what it is rewarded for. When the reward is an imperfect proxy, the agent can score highly without doing what was intended: reward hacking, or misspecified objectives. Next slide: examples.

## 46. Reward Hacking

A reward is usually a proxy for the real goal. When proxy and goal diverge, a capable optimiser finds the gap. Every judge, metric and rating used to steer an agent is a reward that can be hacked. That matters for the judge agent you’ll see in the demo.

## 47. How Assistants Learn What We Prefer

Most assistant models are aligned this way. People compare more reliably than they score, so the reward model learns from comparisons: preference learning. Then the language model is fine-tuned with RL, for example PPO, to score well while staying close to its original behaviour. PML2 §22.4.1, pp. 815–816; §35.3.4, pp. 1148–1149.

## 48. RLHF: Learning From Preferences

Raters compare responses more reliably than they score them, so the reward model learns from comparisons. The LLM is then fine-tuned with RL, for example PPO, to score well while staying close to its original behaviour. This happens during training; when the agent runs, it is not learning from rewards.

## 49. Online vs Continual Learning

Online learning updates incrementally as data arrives. Continual learning means acquiring new knowledge without forgetting; the central difficulty is catastrophic forgetting. §19.7 also covers domain and concept drift.

## 50. Remembering Is Not Learning

Three different things can change when people say an agent learned. Only the third changes the model. During an agent run the weights are fixed, so LLM agents are not automatically reinforcement-learning agents. Continual learning, getting better on the job without forgetting, is still an open problem: PML2 §19.7.

## 51. Hallucination and Overclaiming

LLMs can state false things fluently, express unjustified confidence, and report actions as completed when they were not. For agents the last is the most dangerous. Always verify by checking the actual result of the tool call.

## 52. Modern Agentic Architectures

Part 5 maps the components of LLM agents. PML2 (2023) predates most of this; its background is transformers and LLMs (§22.4) and the formal agent model (§34.5.2).

## 53. LLM-Based Agents

In an LLM agent the model reads its context and proposes the next action. The system executes it, appends the result and asks the model again. Interleaving reasoning with actions is the basic pattern.

## 54. Tools, Skills and Memory

Tools let the agent observe and act. The model outputs a structured request; the system decides whether to run it. Skills package know-how; working memory holds task state; long-term memory persists across sessions and should be enabled deliberately.

## 55. Inside a Modern Agent

The LLM reads its context and proposes one action at a time. Tools observe and change the world; memory keeps state; skills package know-how; a perception step turns screenshots and voice into structured data. MCP standardises agent-to-tool connections; A2A standardises agent-to-agent communication. Biggest risks: hallucination, prompt injection hidden in web pages or images, unverified tool results.

## 56. Multimodal Agents

Multimodal agents handle images and voice. A common design is a perception step: a vision model converts the screenshot into fields that text agents use. Multimodality is a property of the chosen models and pipeline.

## 57. Multi-Agent Systems

A multi-agent system splits work among specialised agents coordinated by a supervisor. Each extra agent adds model calls, latency, cost and coordination overhead, and agents on the same model can agree with each other’s mistakes.

## 58. Interoperability: MCP and A2A

MCP is a universal adapter between agents and tools or data sources. A2A is a common language between agents, including agents built by different organisations. They solve different connection problems.

## 59. Reliability: How Agents Fail

The main failure paths: hallucination, prompt injection hidden in retrieved content, unverified tool results and poor calibration. External content must be treated as data, never as instructions.

## 60. Building Reliable Agents

Part 6 turns the theory into design rules. After these slides, switch to the n8n + Ollama workspace and show each rule in the real system.

## 61. Do You Need an Agent?

Not every task needs an agent. If the steps are always the same, a fixed workflow is simpler, cheaper and more reliable. Each agent should have a narrow task, defined inputs and outputs, and only the tools it needs.

## 62. Supervisor–Worker Pattern

In the supervisor–worker architecture, a supervisor decomposes the task, delegates, collects results, routes feedback and decides when to stop. Research and budget can run in parallel; the planner must wait for both. All agents work from one shared, versioned state.

## 63. Judge Agents and Bounded Loops

The judge returns structured feedback so the supervisor can route fixes to the responsible agents. The loop is capped. A judge LLM can be wrong; if it shares the model with the agents it evaluates, it may share their blind spots, so its reliability must itself be tested.

## 64. Code Checks and Guardrails

Anything checkable by ordinary code should be checked by code: this is how hard constraints from Part 2 are enforced strictly. Least privilege, allow-lists, validation and execution limits bound what can go wrong; human approval is required for consequential, hard-to-reverse actions.

## 65. Knowing When to Stop or Escalate

A good system knows when not to answer. Selective prediction lets a model abstain when uncertain; out-of-distribution detection flags inputs unlike the training situation. Both underpin escalation. Record execution traces, tool-call logs and iteration history.

## 66. Evaluation and Impact

Part 7 shifts from “can the agent do the task?” to “does deploying it improve outcomes?” PML2 Chapter 36.

## 67. Two Different Causal Questions

Causal reasoning by an agent and the causal effect of deploying an agent are entirely different questions. Good reasoning inside the task says nothing about whether deployment improves outcomes.

## 68. A Demo Is Not Evidence

Two different causal questions: an agent reasoning about causes, versus the causal effect of deploying the agent. A demo shows what is possible, not how often it works or for whom. Compare against a baseline, ideally with randomisation, and break results down by user group. A classroom comparison illustrates the method; it is not causal evidence about real deployment.

## 69. Measuring the Effect

Random assignment makes the groups alike on average in everything except the agent, so differences in outcomes can be attributed to it. Without randomisation, PML2 covers confounder adjustment, difference-in-differences and credibility checks.

## 70. Applications and Risks

Agentic systems are applied across healthcare, finance, education, logistics, software engineering and science, at very different levels of readiness and risk. Healthcare needs strong human oversight; coding agents are the most mature.

## 71. Two AI Steps, Zero Verification

Per CNN’s report, the incident happened in spring 2026 at Special Operations Command Pacific. AI outputs were chained together without verification, and nothing triggered escalation before a consequential action was planned. In this lecture’s terms: no deterministic or human check, no value-of-information thinking about verifying before acting, and no stop rule proportionate to the stakes.

## 72. Future of AI

Part 8: what is shaping agents now, and the open research directions.

## 73. Where Agents Are Heading

Three trends, each tying back to the lecture. Long-horizon: METR’s measure of task length agents complete reliably has roughly doubled every seven months; at 99% reliability per step, a 100-step task succeeds only about 37% of the time. Verifiable rewards: much recent progress comes from RL on checkable outcomes, which are much harder to hack. Continual learning: today’s agents remember by taking notes; genuinely learning on the job without catastrophic forgetting is still open.

## 74. Why Long Tasks Are Hard

Longer tasks mean more sequential decisions; per-step errors compound. 0.99 to the power 100 is about 0.37. METR measures the length of task, in human-expert time, that agents complete reliably; it has roughly doubled every seven months.

## 75. Beyond Today’s Agents

Research directions grounded in the book: continual learning without catastrophic forgetting; world models that predict consequences before acting (model-based RL); agents that choose experiments via active learning; and combining neural proposals with symbolic verification, like the deterministic budget check.

## 76. Will the next breakthrough come from bigger models, or from systems that learn, reason, experiment and improve themselves?

Open the floor. If the room is quiet, prompt: what evidence would change your mind either way? Photo: Timur Seyfelmlyukov, Unsplash.
