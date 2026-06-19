import os
import httpx
import json
from dotenv import load_dotenv
from src.utils.logger import logger
from src.utils.retry import get_retry_decorator

load_dotenv()

class OpenRouterClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1"
    
    @get_retry_decorator()
    async def generate(self, model: str, prompt: str, system_prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://email-assistant-assessment.local",
            "X-Title": "Email Assistant Eval",
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 800
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                json=payload,
                headers=headers,
                timeout=60.0
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()