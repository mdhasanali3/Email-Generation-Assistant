import asyncio
from src.clients.openrouter_client import OpenRouterClient
from prompts.zero_shot import get_zero_shot_prompt, SYSTEM_PROMPT as ZERO_SYSTEM
from prompts.few_shot import get_few_shot_prompt, SYSTEM_PROMPT as FEW_SYSTEM
from src.utils.logger import logger

async def generate_email(scenario, model: str, strategy: str) -> str:
    client = OpenRouterClient()
    if strategy == "zero_shot":
        prompt = get_zero_shot_prompt(scenario.intent, scenario.facts, scenario.tone)
        system = ZERO_SYSTEM
    else:
        prompt = get_few_shot_prompt(scenario.intent, scenario.facts, scenario.tone)
        system = FEW_SYSTEM
    
    try:
        email = await client.generate(model, prompt, system)
        logger.info(f"Generated for scenario {scenario.id} with {strategy}")
        return email
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        return "Generation failed."