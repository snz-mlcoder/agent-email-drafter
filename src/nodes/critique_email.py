
from src.state import EmailState
from langchain_openai import ChatOpenAI
from src.schema import Critique
from langchain_core.prompts import PromptTemplate
import dotenv

dotenv.load_dotenv()

def critique_email(state: EmailState) -> dict:
    """
    Critiques the drafted email based on the provided context and user input.
    """
    # Implementation for critiquing an email goes here
    draft = state["draft"]
    tone = state["tone"]
    recipient = state["recipient"]
    brief = state["brief"]
    purpose = brief.purpose
    key_points = brief.key_points
    call_to_action = brief.call_to_action
    subject_line = brief.subject_line


    prompt = PromptTemplate(
        input_variables=["draft", "tone", "recipient", "purpose", "key_points", "call_to_action", "subject_line"],
        template="You are an expert email critic. Critique the following email draft:\n\n"
                 "Draft: {draft}\n"
                 "Tone: {tone}\n"
                 "Recipient: {recipient}\n"
                 "Purpose: {purpose}\n"
                 "Key Points: {key_points}\n"
                 "Call to Action: {call_to_action}\n"
                 "Subject Line: {subject_line}\n"
                "Provide constructive feedback on how to improve the email, focusing on clarity, engagement, and effectiveness."
    )

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    llm_response = llm.with_structured_output(Critique).invoke(prompt.format(draft=draft, tone=tone, recipient=recipient, purpose=purpose, key_points=key_points, call_to_action=call_to_action, subject_line=subject_line))
 
    return {"critique": llm_response}


