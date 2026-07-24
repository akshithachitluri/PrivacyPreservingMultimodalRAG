import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="database/chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_chunks(query, k=3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0]