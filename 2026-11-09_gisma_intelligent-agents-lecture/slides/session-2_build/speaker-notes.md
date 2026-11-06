# Speaker notes · Intelligent Agents, Session 2: Build It

## 1. Intelligent Agents

Welcome back. Session 2 of 2: we turn last session’s theory into a working agent, built live in n8n with a local model from Ollama. Photo: Annamaria Kupo, Unsplash.

## 2. Where We Left Off

Ninety seconds of recap. Ask: who tried building it? What broke? Collect two or three answers; they set up today’s build.

## 3. Today: Build It in 30 Minutes

Three parts; most of the time goes into building. Check that everyone has Ollama and n8n running before Part 2.

## 4. PART 1 · 0–8 MIN

Four design rules. Today’s build uses a small version of each: one planner, code checks, a judge and a human.

## 5. Do You Need an Agent?

Not every task needs an agent. If the steps are always the same, a fixed workflow is simpler, cheaper and more reliable. Each agent should have a narrow task, defined inputs and outputs, and only the tools it needs.

## 6. Supervisor–Worker Pattern

In the supervisor–worker architecture, a supervisor decomposes the task, delegates, collects results, routes feedback and decides when to stop. Research and budget can run in parallel; the planner must wait for both. All agents work from one shared, versioned state. Today’s build is a small version of this: one planner agent, code instead of a budget agent, a judge and a human.

## 7. Judge Agents and Bounded Loops

The judge checks only what code can’t (here, a closing day) and returns structured feedback so the supervisor can route fixes to the responsible agents. The loop is capped. A judge LLM can be wrong; if it shares the model with the agents it evaluates, it may share their blind spots, so its reliability must itself be tested.

## 8. Code Checks and Guardrails

Anything checkable by ordinary code should be checked by code: this is how hard constraints from Session 1, Part 2 are enforced strictly. Least privilege, allow-lists, validation and execution limits bound what can go wrong; human approval is required for consequential, hard-to-reverse actions.

## 9. PART 2 · 8–26 MIN

Build along. One step per slide, each with a checkpoint. Don’t move on until most of the room passes.

## 10. What We Build Today

The whole workflow at once, so students see where each step lands. Planner drafts; code rejects anything over budget; the judge rules only on what code can’t check; failures loop back with one fix, at most twice, then a human decides. Nothing is booked.

## 11. Step 1: A Planner That Can Talk

Build it live. Point out the three slots on the AI Agent node: chat model, memory, tools.

## 12. Step 2: Give It a Tool

If the tool is never called, the description is usually too vague, or the model is weak at tool use.

## 13. Step 3: Make the Plan Structured

Structured output is the bridge between the LLM and deterministic code.

## 14. Step 4: Check the Budget in Code

The most important node in the workflow: a hard constraint enforced by code, exactly as in Session 1.

## 15. Step 5: Route on the Result

Test with one cheap and one expensive plan so both branches light up.

## 16. Step 6: A Judge for the Rest

Keep the judge narrow. Everything checkable is already done by code.

## 17. Step 7: Feedback, Cap, Human

This closes the loop from Session 1: bounded revision, then escalation. The numbers on the right are illustrative.

## 18. PART 3 · 26–30 MIN

Close with testing, the evidence question, and the future.

## 19. Test It Like an Engineer

Run one or two live; show the rest from a prepared run. The last one is prompt injection: the agent should treat it as data.

## 20. A Demo Is Not Evidence

Two different causal questions: an agent reasoning about causes, versus the causal effect of deploying the agent. A demo shows what is possible, not how often it works or for whom. Compare against a baseline, ideally with randomisation, and break results down by user group. A classroom comparison illustrates the method; it is not causal evidence about real deployment.

## 21. Where Agents Are Heading

Three trends, each tying back to the lecture. Long-horizon: METR’s measure of task length agents complete reliably has roughly doubled every seven months; at 99% reliability per step, a 100-step task succeeds only about 37% of the time. Verifiable rewards: much recent progress comes from RL on checkable outcomes, which are much harder to hack. Continual learning: today’s agents remember by taking notes; genuinely learning on the job without catastrophic forgetting is still open.

## 22. DISCUSSION

Open the floor. If the room is quiet, prompt: what evidence would change your mind either way? Photo: Timur Seyfelmlyukov, Unsplash.
