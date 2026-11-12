import argparse
from src.state import EmailState
from src.graph import graph

def main():
    parser = argparse.ArgumentParser(description="Email Drafting Agent")
    parser.add_argument("--tone", type=str, required=True, help="Tone of the email (e.g., formal, casual)")
    parser.add_argument("--recipient", type=str, required=True, help="Recipient of the email")
    parser.add_argument("--context", type=str, required=True, help="Context for the email")
    args = parser.parse_args()

    # Create an initial state with user inputs
    initial_state = EmailState(
        tone=args.tone,
        recipient=args.recipient,
        context=args.context
    )

    # Execute the graph with the initial state
    final_state = graph.invoke(initial_state)

    # Print the final draft and critiques
    revision = final_state.get("revision_count", 0)
    print(final_state.get("draft", "No draft generated."))

    critique = final_state.get("critique")
    if critique.approved:
        print(f"\nStatus: Approved after {revision} rejected drafts.")
    else:
        print(f"\nStatus: Not approved after {revision} revisions.")
        print(f"Critique Feedback: {critique.feedback}")
if __name__ == "__main__":
    main()