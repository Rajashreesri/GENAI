📚 Student Project Retriever (RAG with FAISS + Groq)

This project extracts text from PDF project reports, stores them as JSON, builds a FAISS vector index using SentenceTransformer embeddings, and retrieves relevant project details based on a student’s name.
It then uses Groq LLM to summarize the retrieved documents into a structured output.

🚀 Features

Extracts full text from PDF files using pdfplumber.

Converts all PDFs into JSON format with metadata.

Creates vector embeddings with sentence-transformers.

Stores and searches embeddings with FAISS.

Retrieves top-k relevant project documents for a given student name.

Uses Groq LLM to generate structured summaries of projects:

Project Title

Summary

Tech Stacks

🛠️ Tech Stack

Python 3.9+

pdfplumber
 – Extract text from PDFs

sentence-transformers
 – Generate embeddings

FAISS
 – Efficient similarity search

Groq
 – LLM inference for summarization

📂 Project Workflow

PDF Extraction → Extracts text from each PDF.

JSON Conversion → Saves extracted text into JSON files.

Index Building → Creates embeddings & builds FAISS index.

Query/Search → Input a student’s name, retrieve relevant documents.

LLM Summarization → Groq model summarizes into clean project details.

⚙️ Installation
# Clone the repository
git clone https://github.com/your-username/student-project-retriever.git
cd student-project-retriever

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

📑 Usage

Set your Groq API key
Either export it:

export GROQ_API_KEY="your_api_key_here"


Or put it directly in the code (less secure, only for testing).

Run the script

python main.py


Input a student name

Enter student name: John Doe


Example Output

📌 Project Title: Fake News Detection using Machine Learning
📝 Summary: Developed a Flask web app to classify real vs fake news using NLP techniques.
🛠️ Tech Stacks: Python, Flask, NLP, scikit-learn
