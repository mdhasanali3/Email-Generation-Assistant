# Email Generation Assistant - Senior AI Engineer Assessment

## Overview
A **production-grade POC** demonstrating advanced LLM application development for professional email generation. This project showcases strong prompt engineering, custom evaluation frameworks, multi-model experimentation, and production engineering practices.

**Key Highlights:**
- Advanced **Role-Playing + Few-Shot** prompting strategy
- 3 **task-specific custom metrics** (Fact Coverage via embeddings, Tone via LLM-as-Judge, Structure Score)
- Evaluation across multiple models and prompting strategies
- Async pipelines, retries, Pydantic validation, config-driven design

## Custom Evaluation Metrics
1. **Fact Coverage Score (FCS)**: Semantic similarity using SentenceTransformers (per-fact matching)
2. **Tone Consistency Score (TCS)**: LLM-as-a-Judge (independent Gemini Flash evaluation)
3. **Professional Structure Score (PESS)**: Heuristic check for Subject/Greeting/Body/Closing

## Setup Instructions
1. `pip install -r requirements.txt`
2. Copy `.env.example` → `.env` and set your `OPENROUTER_API_KEY`
3. Run full evaluation: `python -m src.run`
4. (Optional) Run specific strategy: `python -m src.run --strategy few_shot`

## Project Structure
```
email-assistant-eval/
├── data/                 # Scenarios + references
├── prompts/              # Zero-shot & Few-shot templates
├── configs/              # Models & evaluation settings
├── src/
│   ├── clients/          # OpenRouter async client
│   ├── evaluators/       # 3 custom metrics + reporting
│   ├── pipelines/        # Generation & evaluation pipelines
│   ├── schemas/          # Pydantic models
│   └── utils/            # Logging, retries, loaders
├── reports/              # CSV, JSON, Markdown results
└── README.md
```

## Expected Results
With improved prompting, expect **Fact Coverage > 0.85**, **Tone > 0.90**, **Structure > 0.95** across top models.

This submission demonstrates senior-level skills in LLM engineering, evaluation science, and production ML practices.