import pytest
from chroma_client import ChromaDBClient


@pytest.fixture(scope="module")
def client():
    # Setup: Initialize ChromaDBClient (change path as needed)
    client = ChromaDBClient(path="/path/to/db")
    yield client

@pytest.fixture(scope="module")
def sample_texts():
    with open('sample_texts.txt', 'r') as file:
        texts = file.readlines()
    return [text.strip() for text in texts]

def test_create_collection(client):
    collection = client.create_collection("test_collection")
    assert collection is not None

def test_insert_document(client, sample_texts):
    ids = [f"doc{i}" for i in range(len(sample_texts))]
    client.insert_document("test_collection", sample_texts, ids)
    collection = client.client.get_collection(name="test_collection")
    docs = collection.get()
    assert len(docs['documents']) == len(sample_texts)

def test_update_document(client):
    updated_text = ["This is an updated document."]
    client.update_document("test_collection", ids=["doc0"], documents=updated_text)
    collection = client.client.get_collection(name="test_collection")
    doc = collection.get(ids=["doc0"])
    assert doc['documents'][0] == "This is an updated document."

def test_retrieve_documents(client):
    results = client.retrieve_documents("test_collection", query_texts=["test"], n_results=2)
    assert len(results['documents']) > 0

def test_delete_document(client):
    client.delete_document("test_collection", ids=["doc1"])
    collection = client.client.get_collection(name="test_collection")
    doc = collection.get(ids=["doc1"])
    assert len(doc['documents']) == 0

if __name__ == "__main__":
    pytest.main()
