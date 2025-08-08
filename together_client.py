import os
import streamlit as st
from together import Together

def _get_api_key() -> str:
    # 1) Streamlit Cloud or local secrets.toml
    if "TOGETHER_API_KEY" in st.secrets:
        return st.secrets["TOGETHER_API_KEY"]
    # 2) Fallback to env var for local dev
    return os.getenv("TOGETHER_API_KEY", "")

def summarize_statement(statement_text: str) -> str:
    api_key = _get_api_key()
    if not api_key:
        raise RuntimeError("TOGETHER_API_KEY not found. Set it in Streamlit Secrets or env.")

    client = Together(api_key=api_key)
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a personal finance consultant. "
                    "Your response should address the user in second person. "
                    "Given the raw transactions from a bank or credit card statement, "
                    "1) provide a concise summary (total spend, category breakdown, patterns) with a simple table when helpful, "
                    "2) suggest specific steps to reduce expenses, optimize budgets, and improve overall planning."
                ),
            },
            {"role": "user", "content": statement_text},
        ],
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"],
    )
    return response.choices[0].message.content
