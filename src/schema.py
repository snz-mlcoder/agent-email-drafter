from pydantic import BaseModel as base_model

class EmailBrief(base_model):
    purpose: str
    key_points: list[str]
    call_to_action: str
    subject_line: str

class Critique(base_model):
    approved: bool
    feedback: str
    