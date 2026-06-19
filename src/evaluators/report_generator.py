import pandas as pd
from pathlib import Path
from src.utils.logger import logger

def generate_reports(results: list, output_dir: str = "reports"):
    Path(output_dir).mkdir(exist_ok=True)
    
    df = pd.DataFrame([r.dict() for r in results])
    df.to_csv(f"{output_dir}/results.csv", index=False)
    
    summary = df.groupby(['model_name', 'prompt_strategy']).agg({
        'fact_score': 'mean',
        'tone_score': 'mean',
        'structure_score': 'mean',
        'overall_score': ['mean', 'std']
    }).round(3)
    summary.to_csv(f"{output_dir}/summary.csv")
    
    logger.info(f"Reports generated in {output_dir}/")