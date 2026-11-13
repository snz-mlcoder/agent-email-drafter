
from src.schema import EmailBrief
from src.state import EmailState
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import dotenv

dotenv.load_dotenv()

def draft_email(state: EmailState) -> dict:
    """
    Drafts an email using the provided context and user input.
    """
    # Implementation for drafting an email goes here
    tone =state["tone"]
    recipient = state["recipient"]
    brief = state["brief"]
    purpose = brief.purpose
    key_points = brief.key_points
    call_to_action = brief.call_to_action
    subject_line = brief.subject_line
    critique = state.get("critique")

    if critique is not None and not critique.approved:
        revision_note = (
            f"previous draft: {state.get('draft', '')}\n\n"
            f"Reviewer feedback: {critique.feedback}\n\n"
            "rewrite the email based on the feedback"
        )
    else:
        revision_note = ""

    prompt = PromptTemplate(
        input_variables=["tone", "recipient", "purpose", "key_points", "call_to_action", "subject_line", "revision_note"],
        template="You are an expert email writer. Draft an email with the following details:\n\n"
                 "Tone: {tone}\n"
                 "Recipient: {recipient}\n"
                 "Purpose: {purpose}\n"
                 "Key Points: {key_points}\n"
                 "Call to Action: {call_to_action}\n"
                 "Subject Line: {subject_line}\n"
                 "Critique: {revision_note}\n"
                 "write the email in a professional and engaging manner, around 200 words , good subject line and closing statment"
    )

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7, timeout=30, max_retries=2)
    llm_response = llm.invoke(prompt.format(tone=tone, recipient=recipient, purpose=purpose, key_points=key_points, call_to_action=call_to_action, subject_line=subject_line, revision_note=revision_note)).content
    return {"draft": llm_response}
 