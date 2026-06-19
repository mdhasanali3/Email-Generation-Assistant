def structure_score(generated_email: str) -> float:
    
    email_lower = generated_email.lower().strip()
    score = 0.0
    weights = {'subject': 0.25, 'greeting': 0.25, 'body': 0.25, 'closing': 0.25}
    
    # Subject
    if 'subject:' in email_lower or email_lower.startswith('subject') or 're:' in email_lower:
        score += weights['subject']
    
    # Greeting
    if any(g in email_lower for g in ['dear', 'hi ', 'hello', 'greetings']):
        score += weights['greeting']
    
    # Body (multiple paragraphs or substantial content)
    paragraphs = [p.strip() for p in generated_email.split('\n\n') if p.strip()]
    if len(paragraphs) >= 2 or len(generated_email) > 150:
        score += weights['body']
    
    # Closing
    closing_indicators = ['best regards', 'sincerely', 'thank you', 'regards', 'yours', 'best']
    if any(c in email_lower for c in closing_indicators):
        score += weights['closing']
    
    final_score = min(score, 1.0)
    return round(final_score, 2)