import faiss
import numpy as np

class VectorDB:
    def __init__(self):
        self.index = None
        self.meta = []

    def add_embeddings(self, embeddings, chunks):
        vecs = np.array(embeddings).astype("float32")
        if self.index is None:
            self.index = faiss.IndexFlatL2(vecs.shape[1])
        self.index.add(vecs)
        self.meta.extend(chunks)

    def search(self, query_emb, k=3):
        D, I = self.index.search(np.array([query_emb]).astype("float32"), k)
        return [self.meta[i] for i in I[0]]
