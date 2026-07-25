import streamlit as st
import os

from utils.pdf_utils import extract_text

from styles.theme import load_css
from components.header import show_header
from utils.text_utils import split_text
from rag.embeddings import create_embeddings
from rag.vector_store import store_embeddings

from entity.detector import detect_entities
from entity.storage import save_entities

# ----------------------------
# Page Configuration
# ----------------------------

load_css()

show_header(
    "📂 Upload Data",
    "Upload PDF documents and images"
)

# ----------------------------
# Create folders if not present
# ----------------------------

DOCUMENT_FOLDER = "data/documents"
IMAGE_FOLDER = "data/images"

os.makedirs(DOCUMENT_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# ----------------------------
# Upload PDF
# ----------------------------

st.subheader("📄 Upload PDF")

uploaded_pdf = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_pdf:

    # Save uploaded PDF
    pdf_path = os.path.join(
        DOCUMENT_FOLDER,
        uploaded_pdf.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    st.success("✅ PDF uploaded successfully!")

    # ----------------------------
    # Extract Text
    # ----------------------------

    text = extract_text(pdf_path)

    # ----------------------------
    # Detect and Save Entities
    # ----------------------------

    entities = detect_entities(text)
    save_entities(entities)

    st.success(f"✅ Detected {len(entities)} entities")

    # Display detected entities
    with st.expander("🔍 View Detected Entities"):
        st.json(entities)

    # ----------------------------
    # Split Text into Chunks
    # ----------------------------

    chunks = split_text(text)

    st.success(f"✅ Created {len(chunks)} chunks")

    # ----------------------------
    # Generate Embeddings
    # ----------------------------

    embeddings = create_embeddings(chunks)

    st.success(f"✅ Generated {len(embeddings)} embeddings")

    # ----------------------------
    # Store in ChromaDB
    # ----------------------------

    store_embeddings(chunks, embeddings)

    st.success("✅ Stored in ChromaDB successfully!")

    # ----------------------------
    # Preview
    # ----------------------------

    st.subheader("📑 First Chunk")

    st.text_area(
        "Chunk 1",
        chunks[0],
        height=250
    )

    st.subheader("📄 Extracted Text")

    st.text_area(
        "Extracted Text",
        text[:3000],
        height=300
    )