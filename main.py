import os
import logging
from chroma_client import ChromaDBClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PATH = "./"
COLLECTION_NAME = "test_collection"


def create_collection(client):
    logger.info("Creating collection...")
    collection = client.create_collection(COLLECTION_NAME)
    logger.info("Collection created.")


def insert_documents(client, sample_texts):
    logger.info("Inserting documents...")
    ids = [f"doc{i}" for i in range(len(sample_texts))]
    client.insert_document(COLLECTION_NAME, sample_texts, ids)
    logger.info("Documents inserted.")


def update_document(client):
    logger.info("Updating a document...")
    updated_text = ["This is an updated document."]
    client.update_document(COLLECTION_NAME, ids=["doc0"], documents=updated_text)
    logger.info("Document updated.")


def retrieve_documents(client):
    logger.info("Retrieving documents...")
    results = client.retrieve_documents(COLLECTION_NAME, query_texts=["test"], n_results=2)
    logger.info("Retrieved documents:")
    for doc in results['documents']:
        logger.info(doc)


def delete_document(client):
    logger.info("Deleting a document...")
    client.delete_document(COLLECTION_NAME, ids=["doc1"])
    logger.info("Document deleted.")


def main():
    client = ChromaDBClient(path=DB_PATH)

    create_collection(client)

    logger.info("Reading sample texts from file...")
    with open('sample_texts.txt', 'r') as file:
        sample_texts = [line.strip() for line in file.readlines()]

    insert_documents(client, sample_texts)

    update_document(client)

    retrieve_documents(client)

    delete_document(client)

    logger.info("Retrieving documents after deletion...")
    remaining_docs = client.retrieve_documents(COLLECTION_NAME, query_texts=["test"], n_results=10)
    logger.info("Remaining documents:")
    for doc in remaining_docs['documents']:
        logger.info(doc)


if __name__ == "__main__":
    main()
