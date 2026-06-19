import asyncio
import yaml
from src.utils.file_loader import load_scenarios, load_config
from src.pipelines.evaluation_pipeline import run_full_evaluation
from src.utils.logger import logger

async def main():
    scenarios = load_scenarios()
    models = load_config("configs/models.yaml")['models']
    eval_config = load_config("configs/evaluation.yaml")
    strategies = eval_config['strategies']
    
    logger.info(f"Starting evaluation with {len(scenarios)} scenarios, {len(models)} models, {len(strategies)} strategies")
    
    results = await run_full_evaluation(scenarios, models, strategies, eval_config)
    logger.info("Evaluation completed. Check reports/ folder.")

if __name__ == "__main__":
    asyncio.run(main())