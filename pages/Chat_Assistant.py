import streamlit as st

from styles.theme import load_css
from components.header import show_header

from rag.retriever import retrieve_chunks
from rag.generator import generate_answer

# ------------------------
# Page Design
# ------------------------

load_css()

show_header(
    "💬 Chat Assistant",
    "Ask questions about your uploaded documents"
)

# ------------------------
# User Question
# ------------------------

question = st.text_input(
    "Ask a question"
)

# ------------------------
# Retrieve Chunks
# ------------------------

if question:
    chunks = retrieve_chunks(question)
    st.success(f"Retrieved {len(chunks)} relevant chunks")
    # Generate answer using Gemini
    answer = generate_answer(question, chunks)
    
    st.subheader("🤖 AI Answer")
    st.write(answer)
    st.divider()
    
    st.subheader("📚 Retrieved Chunks")
    for i, chunk in enumerate(chunks):
        st.markdown(f"### 📄 Chunk {i+1}")
        st.text_area(
            "",
            chunk,
            height=180,
            key=i
        )