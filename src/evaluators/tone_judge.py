import json
from src.clients.openrouter_client import OpenRouterClient
from src.utils.logger import logger

async def tone_consistency_score(generated_email: str, target_tone: str, judge_model: str = "google/gemini-2.5-flash-lite") -> float:
    client = OpenRouterClient()
    judge_prompt = f"""You are an expert tone evaluator.
                    Target tone: {target_tone}
                    Email:
                    {generated_email}

                    Rate how well the email matches the target tone on a scale of 1-10. 
                    Output ONLY valid JSON: {{"score": <number>}}"""

    try:
        result = await client.generate(judge_model, judge_prompt, "You are a precise JSON evaluator.")
        score_data = json.loads(result)
        score = score_data.get("score", 5) / 10.0
        return round(max(0.0, min(1.0, score)), 2)
    except Exception as e:
        logger.error(f"Tone judge failed: {e}")
        return 0.7