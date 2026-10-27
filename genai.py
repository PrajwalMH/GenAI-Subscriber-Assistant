import os

from dotenv import load_dotenv
from openai import OpenAI

from analytics import get_subscriber_summary
from query_parser import parse_query


# ============================================================
# LOAD API KEY
# ============================================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY was not found. "
        "Add it to your .env file."
    )


client = OpenAI(
    api_key=api_key
)


# ============================================================
# BUILD GROUNDED PROMPT
# ============================================================

def build_prompt(question):

    parsed = parse_query(question)

    region = parsed["region"]
    plan = parsed["plan"]

    summary = get_subscriber_summary(
        region=region,
        plan=plan
    )

    if "message" in summary:
        return None, summary["message"]

    prompt = f"""
You are a professional subscriber analytics assistant.

The user asked:

"{question}"

Use only the factual analytics below.

Subscriber analytics:
- Region: {region if region else "All regions"}
- Plan: {plan if plan else "All plans"}
- Total subscribers: {summary["total_subscribers"]}
- Average spend: ${summary["average_spend"]:.2f}
- Churn rate: {summary["churn_rate"]:.2f}%
- Average tenure: {summary["average_tenure_days"]:.1f} days
- Active subscribers: {summary["active_subscribers"]}
- Churned subscribers: {summary["churned_subscribers"]}

Instructions:
- Give a short professional business summary.
- Use only the numbers above.
- Do not invent any metrics.
- Mention retention if relevant.
- Explain the most important insight.
- Keep the response concise.
"""

    return prompt, None


# ============================================================
# GENERATE OPENAI RESPONSE
# ============================================================

def generate_insight(question):

    prompt, error = build_prompt(question)

    if error:
        return error

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


# ============================================================
# COMMAND LINE CHAT
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("GENAI SUBSCRIBER ANALYTICS ASSISTANT")
    print("=" * 60)

    print("\nType 'exit' to stop.\n")

    while True:

        question = input(
            "Ask a subscriber analytics question: "
        )

        if question.lower().strip() in [
            "exit",
            "quit"
        ]:
            print(
                "\nSubscriber Analytics Assistant stopped."
            )
            break

        response = generate_insight(
            question
        )

        print("\nGenAI Response:\n")
        print(response)

        print("\n" + "-" * 60 + "\n")
