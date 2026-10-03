# 🎓 University Knowledge Assistant

An AI-powered RAG (Retrieval-Augmented Generation) application that answers questions using university documents.

## 🚀 Features

* 📄 PDF document processing
* ✂️ Text chunking
* 🔢 Text embeddings using Sentence Transformers
* 🗄️ Vector storage and semantic search using ChromaDB
* 🤖 Gemini-powered answer generation
* 🔎 Relevant document retrieval
* 🚫 "I don't know" handling when information is not found
* 📚 Source and page display
* 🌐 Streamlit web interface

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Sentence Transformers
* ChromaDB
* pdfplumber
* python-dotenv

## 🔄 How It Works

```text
University PDF
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
ChromaDB
      ↓
User Question
      ↓
Semantic Search
      ↓
Relevant Information
      ↓
Gemini
      ↓
Answer + Source
```

## ▶️ How to Run

### 1. Install dependencies

```bash
python -m pip install pdfplumber sentence-transformers chromadb google-genai python-dotenv streamlit
```

### 2. Add Gemini API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Never upload the `.env` file to GitHub.

### 3. Store document embeddings

```bash
python store_embeddings.py
```

### 4. Start the application

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## 💡 Example Questions

* What is the minimum attendance required?
* What happens if attendance is below 75%?
* Can students with medical reasons get attendance consideration?
* What are the requirements for examination eligibility?

## 🎯 Project Goal

The goal of this project is to provide a simple university document assistant that retrieves relevant information from uploaded documents and generates grounded answers using RAG.
