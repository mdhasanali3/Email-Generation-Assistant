import asyncio
from src.evaluators.fact_coverage import fact_coverage_score
from src.evaluators.tone_judge import tone_consistency_score
from src.evaluators.structure_score import structure_score
from src.schemas.evaluation import EvaluationResult
from src.utils.logger import logger
from src.evaluators.report_generator import generate_reports
from src.pipelines.generation_pipeline import generate_email

async def evaluate_scenario(scenario, model: str, strategy: str, generated_email: str, config):
    fact_score = fact_coverage_score(generated_email, scenario.facts)
    tone_score = await tone_consistency_score(generated_email, scenario.tone, config['metrics']['tone']['judge_model'])
    struct_score = structure_score(generated_email)
    
    overall = round((fact_score + tone_score + struct_score) / 3, 2)
    
    return EvaluationResult(
        scenario_id=scenario.id,
        model_name=model,
        prompt_strategy=strategy,
        fact_score=fact_score,
        tone_score=tone_score,
        structure_score=struct_score,
        overall_score=overall,
        generated_email=generated_email
    )

async def run_full_evaluation(scenarios, models, strategies, config):
    results = []
    tasks = []
    
    for scenario in scenarios:
        for model_config in models:
            model = model_config['name']
            for strategy in strategies:
                tasks.append(
                    (scenario, model, strategy, generate_email(scenario, model, strategy))
                )
    
    for scenario, model, strategy, gen_task in tasks:
        try:
            generated = await gen_task
            eval_result = await evaluate_scenario(scenario, model, strategy, generated, config)
            results.append(eval_result)
        except Exception as e:
            logger.error(f"Eval failed for {scenario.id}: {e}")
    
    generate_reports(results)
    return results