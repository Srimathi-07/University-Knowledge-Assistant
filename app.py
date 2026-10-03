import os
import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="University Knowledge Assistant",
    page_icon="🎓",
    layout="centered"
)


# =========================
# LOAD API KEY
# =========================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# =========================
# LOAD EMBEDDING MODEL
# =========================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================
# CONNECT TO CHROMADB
# =========================

db = chromadb.PersistentClient(
    path="chroma_db"
)

collection = db.get_collection(
    name="university_documents"
)


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 17px;
    margin-bottom: 25px;
}

.answer-box {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
    margin-top: 10px;
}

.source-box {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.markdown(
    '<div class="main-title">🎓 University Knowledge Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask questions about your university documents</div>',
    unsafe_allow_html=True
)


# =========================
# QUESTION INPUT
# =========================

question = st.text_input(
    "💬 Ask your question",
    placeholder="Example: What is the minimum attendance required?"
)


# =========================
# ASK BUTTON
# =========================

if st.button("🔍 Ask Question", use_container_width=True):

    if question.strip():

        # =========================
        # CREATE QUESTION EMBEDDING
        # =========================

        question_embedding = model.encode(question)


        # =========================
        # SEARCH CHROMADB
        # =========================

        results = collection.query(
            query_embeddings=[
                question_embedding.tolist()
            ],
            n_results=2,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )


        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]


        # =========================
        # CHECK RELEVANCE
        # =========================

        best_distance = distances[0]

        # Smaller distance = more similar
        # Larger distance = less similar

        if best_distance > 1.0:

            st.warning(
                "🔎 I couldn't find this information "
                "in the university documents."
            )

        else:

            # =========================
            # COMBINE RETRIEVED CONTENT
            # =========================

            context = "\n".join(documents)


            # =========================
            # GEMINI PROMPT
            # =========================

            prompt = f"""
Answer the question using ONLY the information provided below.

Information:
{context}

Question:
{question}

Rules:
- Answer only from the provided information.
- Do not use outside knowledge.
- Do not guess.
- If the information does not answer the question, say:
"I couldn't find this information in the university documents."
- Give a simple and clear answer.
"""


            # =========================
            # GENERATE ANSWER
            # =========================

            with st.spinner(
                "🤖 Searching university documents..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )


            # =========================
            # DISPLAY ANSWER
            # =========================

            st.markdown("### 📌 Answer")

            st.markdown(
                f"""
                <div class="answer-box">
                {response.text}
                </div>
                """,
                unsafe_allow_html=True
            )


            # =========================
            # DISPLAY SOURCE
            # =========================

            st.markdown("### 📚 Source")

            source = metadatas[0]

            st.markdown(
                f"""
                <div class="source-box">
                📄 <b>Document:</b> {source['source']}<br>
                📖 <b>Page:</b> {source['page']}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.warning(
            "⚠️ Please enter a question."
        )