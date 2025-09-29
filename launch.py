import subprocess
import sys

# Path to your Streamlit app
app_path = r"C:\Users\rajas\OneDrive\Desktop\genai\code.py"

# Run the Streamlit command
subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])
