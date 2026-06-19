import json
import yaml
from pathlib import Path
from src.schemas.scenario import Scenario

def load_scenarios() -> list[Scenario]:
    path = Path("data/scenarios.json")
    with open(path, 'r') as f:
        data = json.load(f)
    return [Scenario(**item) for item in data]

def load_config(path: str):
    with open(path, 'r') as f:
        return yaml.safe_load(f)