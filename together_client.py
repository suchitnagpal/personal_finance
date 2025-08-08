<<<<<<< HEAD
import os
import streamlit as st
from together import Together

def _get_api_key() -> str:
    # 1) Streamlit Cloud or local secrets.toml
    if "TOGETHER_API_KEY" in st.secrets:
        return st.secrets["TOGETHER_API_KEY"]
    # 2) Fallback to env var for non-Streamlit contexts
    return os.getenv("TOGETHER_API_KEY", "")

def summarize_statement(statement_text: str) -> str:
    api_key = _get_api_key()
    if not api_key:
        raise RuntimeError("TOGETHER_API_KEY not found. Set it in Streamlit Secrets or env.")
    """
    Ask your LLM to summarize a bank/credit-card statement
    in plain language, categorize spend, etc.
    """
    if not TOGETHER_API_KEY:
        raise RuntimeError("Please set the TOGETHER_API_KEY variable in together_client.py")

    client = Together(api_key=api_key)
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a personal finance consultant. "
                    "Your response should address in second person.."
                    "Given the raw transactions from a bank or credit card statement, "
                    "1) provide a concise summary: total spend, category breakdown, and patterns, using tabular, "
                    "2) suggest specific steps to reduce expenses, optimize budgets, "
                    "   and improve overall financial planning. "
                    
                
                            )
            },
            {"role": "user", "content": statement_text}
        ],
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"], 
    )
=======
from together import Together

# ←– replace with your real key
TOGETHER_API_KEY = "c321f7395f4246cffa47c6700c50797577236bd15d2d60a1e81d6c36c8629c21"

def summarize_statement(statement_text: str) -> str:
    """
    Ask your LLM to summarize a bank/credit-card statement
    in plain language, categorize spend, etc.
    """
    if not TOGETHER_API_KEY:
        raise RuntimeError("Please set the TOGETHER_API_KEY variable in together_client.py")

    client = Together(api_key=TOGETHER_API_KEY)
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a personal finance consultant. "
                    "Your response should address in second person.."
                    "Given the raw transactions from a bank or credit card statement, "
                    "1) provide a concise summary: total spend, category breakdown, and patterns, using tabular, "
                    "2) suggest specific steps to reduce expenses, optimize budgets, "
                    "   and improve overall financial planning. "
                    
                
                            )
            },
            {"role": "user", "content": statement_text}
        ],
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"], 
    )
>>>>>>> 4a8de3e3a9ae6372e8f996f07de9e7ad579ad7e7
    return response.choices[0].message.content