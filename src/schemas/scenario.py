from pydantic import BaseModel
from typing import List

class Scenario(BaseModel):
    id: int
    intent: str
    tone: str
    facts: List[str]