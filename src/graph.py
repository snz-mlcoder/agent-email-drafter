
from src.state import EmailState
from langgraph.graph import StateGraph, START, END
from src.nodes.draft_email import draft_email
from src.nodes.critique_email import critique_email
from src.nodes.analyze_context import analyze_context


MAX_REVISIONS = 3

def should_continue(state: EmailState) -> str:
    critique = state.get("critique")
    if critique.approved:
        return "stop"
    if state.get("revision_count", 0) >= MAX_REVISIONS:
        return "stop"
    return "continue"

graph_builder = StateGraph(EmailState)

graph_builder.add_node("analyze_context", analyze_context)
graph_builder.add_node("draft_email", draft_email)
graph_builder.add_node("critique_email", critique_email)


graph_builder.add_edge(START, "analyze_context")
graph_builder.add_edge("analyze_context", "draft_email")
graph_builder.add_edge("draft_email", "critique_email")

graph_builder.add_conditional_edges(
            "critique_email",
            should_continue, 
            {"continue": "draft_email", "stop": END})

graph = graph_builder.compile()