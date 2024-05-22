# ChromaDBClient Task

This project demonstrates how to use the `ChromaDBClient` class to interact with a vector database using ChromaDB. It includes operations for creating a collection, inserting documents, updating a document, retrieving documents, and deleting a document.

## Prerequisites

- Python 3.6+
- `chromadb` package

## Setup

1. **Clone the repository** (if applicable) or download the project files.

2. **Install the required packages**:
   ```sh
   pip install -r requirements.txt

3. **Modify the sample text file**:
- Modify the file named sample_texts.txt with the custom content.

## Usage
- The main.py script performs the following operations:

- Create a Collection:
  - Initializes the ChromaDB client and creates a collection named "test_collection".

- Insert Documents:
  - Reads the sample texts from sample_texts.txt and inserts them into the collection.

- Update a Document:
  - Updates the first document in the collection with new text.

- Retrieve Documents:
  - Retrieves the top 2 documents that match the query text "test".

- Delete a Document:
  - Deletes the second document from the collection.

- To run the script and perform these operations, execute:
  - ```sh 
    python main.py
    
## Testing the App
- Unit tests are provided in the tests.py file. To run the tests, use the following command:
  - ```sh 
    pytest test_chroma_db_client.py
