
from typing import TypedDict
from src.schema import EmailBrief
from src.schema import Critique 

class EmailState(TypedDict):
    context: str
    recipient: str
    tone: str
    brief: EmailBrief | None
    draft: str | None
    critique: Critique | None
    revision_count: int
