# GenAI Subscriber Assistant

GenAI-powered subscriber analytics assistant that lets users ask natural-language questions about subscriber data and receive grounded business insights based on real metrics calculated from a CSV dataset.

## Overview

The application combines traditional data analytics with Generative AI.

A user can ask questions such as:

- Tell me about Premium subscribers in the South region
- How are Basic subscribers performing in the West?
- Give me insights about Standard subscribers in the North

The system extracts the relevant region and subscription plan, calculates real metrics from `subscribers.csv`, and sends those verified results to OpenAI to generate a concise business summary.

## Architecture

```text
User Question
     ↓
Natural Language Query Parser
     ↓
Subscriber Data Filtering
     ↓
Pandas Analytics
     ↓
Verified Metrics
     ↓
OpenAI API
     ↓
Generated Business Insight
```

## Features

- Natural-language subscriber queries
- Region and subscription-plan filtering
- Subscriber count analysis
- Average spend calculation
- Churn-rate analysis
- Average tenure analysis
- Active vs churned subscriber counts
- OpenAI-generated business insights
- Interactive Streamlit chat interface
- Light and dark theme support

## Tech Stack

- Python
- Pandas
- Streamlit
- OpenAI API
- python-dotenv

## Project Structure

```text
GenAI-Subscriber-Assistant/
├── app.py
├── analytics.py
├── query_parser.py
├── assistant_core.py
├── genai.py
├── subscribers.csv
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> `.env` is excluded from GitHub because it contains the OpenAI API key.

## Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
cd GenAI-Subscriber-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_openai_api_key
```

Run the application:

```bash
streamlit run app.py
```

## Example Query

```text
Tell me about Premium subscribers in the South region
```

Example workflow:

```text
Region: South
Plan: Premium
        ↓
Metrics calculated from subscribers.csv
        ↓
OpenAI generates a grounded business summary
```

## Important Design Choice

The GenAI model does not calculate subscriber metrics directly.

Pandas first computes the actual values from the dataset, and only those verified metrics are passed to OpenAI. This reduces hallucination and keeps the generated response grounded in real data.

## Author

**Prajwal Mrithyunjay Hulamani**
