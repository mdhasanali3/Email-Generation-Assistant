from pydantic import BaseModel

class EmailOutput(BaseModel):
    subject: str
    greeting: str
    body: str
    closing: str