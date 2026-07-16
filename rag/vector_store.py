import chromadb

client = chromadb.PersistentClient(path="database/chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)

def store_embeddings(chunks, embeddings):

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )