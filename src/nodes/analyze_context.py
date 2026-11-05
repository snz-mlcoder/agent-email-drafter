

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from src.state import EmailState
from src.schema import EmailBrief
import dotenv

dotenv.load_dotenv()


def analyze_context(state: EmailState)-> dict:
    """
    Analyze the email context and provide a brief summary of the purpose, key points, call to action, and subject line from the given state."""
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, max_tokens=300) 
    prompt = PromptTemplate(
        input_variables=["context", "recipient", "tone"],
        template="Analyze the following email context and provide a brief summary of the purpose, key points, call to action, and subject line. Context: {context}, Recipient: {recipient}, Tone: {tone}"
    )  
    response =llm.with_structured_output(EmailBrief).invoke(prompt.format(context=state["context"], recipient=state["recipient"], tone=state["tone"]))


    return {"brief": response}