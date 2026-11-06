# n8n workspace (to be added)

This folder is reserved for the n8n + Ollama multi-agent travel planner shown live in the lecture on 9 November 2026.

Suggested contents when you upload it:

- `workflows/`: exported n8n workflow JSON files (Input Interpreter, Supervisor, Research Agent, Budget Analyst, Planning Agent, Judge)
- `prompts/`: system prompts for each agent
- `test-data/`: the fixed travel data and the sample request with `hotel_screenshot.png`
- `SETUP.md`: Ollama models used (including the vision model), n8n version, and how to run it locally

Remove credentials and API keys from exported workflows before committing.
