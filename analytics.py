from pathlib import Path
import pandas as pd


# ============================================================
# FILE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "subscribers.csv"


# ============================================================
# LOAD AND CLEAN DATA
# ============================================================

def load_subscriber_data():

    df = pd.read_csv(
        DATA_FILE,
        parse_dates=["signup_date"]
    )

    # Keep the latest record for duplicate subscriber IDs
    df = (
        df.sort_values("signup_date")
        .drop_duplicates(
            subset="subscriber_id",
            keep="last"
        )
        .copy()
    )

    # Convert numeric fields safely
    df["total_spend"] = pd.to_numeric(
        df["total_spend"],
        errors="coerce"
    )

    df["churned"] = pd.to_numeric(
        df["churned"],
        errors="coerce"
    )

    # Fixed reference date for reproducibility
    reference_date = pd.Timestamp("2026-10-26")

    df["tenure_days"] = (
        reference_date - df["signup_date"]
    ).dt.days

    df["tenure_days"] = (
        df["tenure_days"]
        .clip(lower=0)
    )

    return df


# ============================================================
# GET SUBSCRIBER SUMMARY
# ============================================================

def get_subscriber_summary(
    region=None,
    plan=None
):

    df = load_subscriber_data()

    # --------------------------------------------------------
    # FILTER BY REGION
    # --------------------------------------------------------

    if region:

        df = df[
            df["region"]
            .fillna("")
            .str.lower()
            == region.lower()
        ]

    # --------------------------------------------------------
    # FILTER BY PLAN
    # --------------------------------------------------------

    if plan:

        df = df[
            df["plan_type"]
            .fillna("")
            .str.lower()
            == plan.lower()
        ]

    # --------------------------------------------------------
    # HANDLE NO MATCHES
    # --------------------------------------------------------

    if df.empty:

        return {
            "message": "No matching subscribers found."
        }

    # --------------------------------------------------------
    # CALCULATE METRICS
    # --------------------------------------------------------

    total_subscribers = (
        df["subscriber_id"]
        .nunique()
    )

    average_spend = (
        df["total_spend"]
        .mean()
    )

    churn_rate = (
        df["churned"]
        .mean()
        * 100
    )

    average_tenure = (
        df["tenure_days"]
        .mean()
    )

    active_subscribers = (
        df["churned"] == 0
    ).sum()

    churned_subscribers = (
        df["churned"] == 1
    ).sum()

    # --------------------------------------------------------
    # CLEAN PYTHON TYPES
    # --------------------------------------------------------

    if pd.isna(average_spend):
        average_spend = 0.0

    if pd.isna(churn_rate):
        churn_rate = 0.0

    if pd.isna(average_tenure):
        average_tenure = 0.0

    # --------------------------------------------------------
    # RETURN SUMMARY
    # --------------------------------------------------------

    return {
        "total_subscribers": int(total_subscribers),
        "average_spend": float(
            round(
                average_spend,
                2
            )
        ),
        "churn_rate": float(
            round(
                churn_rate,
                2
            )
        ),
        "average_tenure_days": float(
            round(
                average_tenure,
                2
            )
        ),
        "active_subscribers": int(
            active_subscribers
        ),
        "churned_subscribers": int(
            churned_subscribers
        )
    }


# ============================================================
# TEST THE ANALYTICS FUNCTION
# ============================================================

if __name__ == "__main__":

    result = get_subscriber_summary(
        region="South",
        plan="Premium"
    )

    print(result)
