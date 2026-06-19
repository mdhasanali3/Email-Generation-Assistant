from pydantic import BaseModel
from typing import Optional

class EvaluationResult(BaseModel):
    scenario_id: int
    model_name: str
    prompt_strategy: str
    fact_score: float
    tone_score: float
    structure_score: float
    overall_score: float
    generated_email: str
    raw_judgment: Optional[str] = None