import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq
from pygments import highlight
from pygments.lexers import guess_lexer, PythonLexer
from pygments.formatters import HtmlFormatter

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set GROQ_API_KEY in .env")

# Init client
client = Groq(api_key=api_key)

# Function: Explain code
def explain_code(code_snippet):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert programming tutor. Explain code in detail with examples."},
            {"role": "user", "content": f"Explain the following code:\n\n{code_snippet}"}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="AI Code Explainer", layout="wide")
st.title("💡 AI Code Explainer")

code_input = st.text_area("Paste your code here:", height=200)

if st.button("Explain Code"):
    if code_input.strip():
        with st.spinner("Analyzing code..."):
            explanation = explain_code(code_input)

            # Highlight code
            try:
                lexer = guess_lexer(code_input)
            except:
                lexer = PythonLexer()
            formatter = HtmlFormatter(style="monokai", full=True, linenos=True)
            highlighted_code = highlight(code_input, lexer, formatter)

            st.subheader("📜 Your Code")
            st.components.v1.html(highlighted_code, height=300, scrolling=True)

            st.subheader("🧑‍🏫 AI Explanation")
            st.write(explanation)
    else:
        st.warning("Please paste some code first.")
        

