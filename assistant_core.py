from analytics import get_subscriber_summary
from query_parser import parse_query


def answer_query(question):

    # Step 1: Extract filters from the user's natural-language question
    parsed = parse_query(question)

    region = parsed["region"]
    plan = parsed["plan"]

    # Step 2: Get real analytics from subscribers.csv
    summary = get_subscriber_summary(
        region=region,
        plan=plan
    )

    # Step 3: Handle no matching data
    if "message" in summary:
        return summary["message"]

    # Step 4: Build a readable response
    scope_parts = []

    if plan:
        scope_parts.append(plan)

    if region:
        scope_parts.append(region)

    if scope_parts:
        scope_text = " ".join(scope_parts)
    else:
        scope_text = "all"

    response = (
        f"For {scope_text} subscribers:\n\n"
        f"- Total subscribers: {summary['total_subscribers']}\n"
        f"- Average spend: ${summary['average_spend']:,.2f}\n"
        f"- Churn rate: {summary['churn_rate']:.2f}%\n"
        f"- Average tenure: {summary['average_tenure_days']:.1f} days\n"
        f"- Active subscribers: {summary['active_subscribers']}\n"
        f"- Churned subscribers: {summary['churned_subscribers']}"
    )

    return response


if __name__ == "__main__":

    question = input(
        "Ask a subscriber analytics question: "
    )

    answer = answer_query(question)

    print("\n" + answer)
