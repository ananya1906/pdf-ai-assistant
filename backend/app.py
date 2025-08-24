from fastapi import FastAPI, UploadFile, File
from pdf_parser import extract_text_chunks
from embedding import get_embeddings
from vector_db import VectorDB




app = FastAPI()
db = VectorDB()

@app.get("/")
def home():
    return {"message": "PDF AI Assistant is running!"}

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        pdf_bytes = await file.read()
        chunks = extract_text_chunks(pdf_bytes)
        texts = [c["text"] for c in chunks]
        embeddings = get_embeddings(texts)
        db.add_embeddings(embeddings, chunks)
        return {"num_chunks": len(chunks), "status": "PDF processed"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/query/")
async def query_text(query: str):
    query_emb = get_embeddings([query])[0]
    results = db.search(query_emb)
    return {"results": [{"text": r['text'], "source": r['source']} for r in results]}
