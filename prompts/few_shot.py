SYSTEM_PROMPT = """
You are an elite Executive Communications Specialist with 15+ years of experience writing high-stakes professional business emails for Fortune 500 companies.

CRITICAL RULES:
- You MUST include EVERY single key fact provided, weaving them naturally and seamlessly into the email body.
- Maintain the exact requested tone throughout.
- Use a complete professional business email format: compelling Subject line, personalized Greeting, clear Body paragraphs, professional Closing.
- NEVER add any information, details, or assumptions not explicitly provided in the key facts.
- Output ONLY the full email. No explanations, no markdown, no extra text.
"""

FEW_SHOT_EXAMPLES = [
    {
        "intent": "Meeting Follow-up",
        "facts": ["Discussed Q3 roadmap", "Need feedback by Friday", "Budget approval pending"],
        "tone": "Professional",
        "output": """Subject: Follow-Up on Q3 Roadmap Discussion

Dear Team,

Thank you for the productive discussion today regarding the Q3 roadmap. We covered several key initiatives, and budget approval is still pending.

As a next step, I require your feedback on the proposed roadmap by end of day Friday.

Thank you for your prompt attention to this matter.

Best regards,
Alex Johnson
Project Lead"""
    },
    {
        "intent": "Project Delay Notification",
        "facts": ["Launch delayed by two weeks", "Caused by security testing", "New target date July 15"],
        "tone": "Apologetic",
        "output": """Subject: Update on Project Launch Timeline

Dear Stakeholders,

I wanted to provide an update regarding our project launch. Due to additional security testing requirements, the launch will be delayed by two weeks.

Our revised target launch date is July 15. While this adjustment impacts the original schedule, it ensures we maintain the highest standards of security and reliability.

We appreciate your understanding and continued support.

Best regards,
Project Team"""
    }
]

def get_few_shot_prompt(intent: str, facts: list, tone: str) -> str:
    facts_str = "\\n".join([f"- {f}" for f in facts])
    examples = ""
    for ex in FEW_SHOT_EXAMPLES:
        examples += f"Example:\\nIntent: {ex['intent']}\\nFacts:\\n" + "\\n".join([f"- {f}" for f in ex['facts']]) + f"\\nTone: {ex['tone']}\\nOutput:\\n{ex['output']}\\n\\n"
    
    return f"""{examples}
            Now write a new email for:
            Intent: {intent}
            Key Facts:
            {facts_str}
            Tone: {tone}

            Email:"""