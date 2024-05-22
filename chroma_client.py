import chromadb


class ChromaDBClient:
    def __init__(self, path=None, host=None, port=None):
        if path:
            self.client = chromadb.PersistentClient(path=path)
        elif host and port:
            self.client = chromadb.HttpClient(host=host, port=port)
        else:
            raise ValueError("You must provide either a path for PersistentClient or host and port for HttpClient.")

    def create_collection(self, name, embedding_function=None):
        if embedding_function:
            return self.client.create_collection(name=name, embedding_function=embedding_function)
        return self.client.create_collection(name=name)

    def insert_document(self, collection_name, documents, ids, metadatas=None, embeddings=None):
        collection = self.client.get_collection(name=collection_name)
        collection.add(documents=documents, ids=ids, metadatas=metadatas, embeddings=embeddings)

    def update_document(self, collection_name, ids, documents=None, metadatas=None, embeddings=None):
        collection = self.client.get_collection(name=collection_name)
        collection.update(ids=ids, documents=documents, metadatas=metadatas, embeddings=embeddings)

    def delete_document(self, collection_name, ids=None, where=None):
        collection = self.client.get_collection(name=collection_name)
        collection.delete(ids=ids, where=where)

    def retrieve_documents(self, collection_name, query_texts=None, query_embeddings=None, n_results=10, where=None,
                           where_document=None):
        collection = self.client.get_collection(name=collection_name)
        if query_texts:
            return collection.query(query_texts=query_texts, n_results=n_results, where=where,
                                    where_document=where_document)
        elif query_embeddings:
            return collection.query(query_embeddings=query_embeddings, n_results=n_results, where=where,
                                    where_document=where_document)
        else:
            raise ValueError("You must provide either query_texts or query_embeddings.")

