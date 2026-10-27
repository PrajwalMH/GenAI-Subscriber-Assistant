# ============================================================
# NATURAL LANGUAGE QUERY PARSER
# ============================================================


VALID_REGIONS = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]


VALID_PLANS = [
    "Basic",
    "Standard",
    "Premium"
]


# ============================================================
# PARSE USER QUESTION
# ============================================================

def parse_query(question):

    question_lower = question.lower()

    region = None
    plan = None

    # --------------------------------------------------------
    # FIND REGION
    # --------------------------------------------------------

    for valid_region in VALID_REGIONS:

        if valid_region.lower() in question_lower:

            region = valid_region

            break

    # --------------------------------------------------------
    # FIND PLAN
    # --------------------------------------------------------

    for valid_plan in VALID_PLANS:

        if valid_plan.lower() in question_lower:

            plan = valid_plan

            break

    # --------------------------------------------------------
    # RETURN EXTRACTED FILTERS
    # --------------------------------------------------------

    return {
        "region": region,
        "plan": plan
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    question = (
        "I want to know about Premium subscribers "
        "in the South region"
    )

    result = parse_query(question)

    print(result)
