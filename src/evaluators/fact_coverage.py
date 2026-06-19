from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from src.utils.logger import logger

model = SentenceTransformer('all-MiniLM-L6-v2')

def fact_coverage_score(generated_email: str, facts: list[str], threshold: float = 0.75) -> float:
    
    if not facts:
        return 1.0
    
    email_embedding = model.encode([generated_email])[0]
    fact_embeddings = model.encode(facts)
    
    # Check each fact individually against the full email
    matched = 0
    for fact_emb in fact_embeddings:
        sim = cosine_similarity([email_embedding], [fact_emb])[0][0]
        if sim >= threshold:
            matched += 1
    
    score = matched / len(facts)
    logger.info(f"Fact coverage: {score:.2f} ({matched}/{len(facts)} facts)")
    return round(score, 2)