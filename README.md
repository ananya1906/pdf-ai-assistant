# PDF AI Assistant

A FastAPI-powered backend that lets you upload, process, and semantically search multiple PDF files using natural language queries. Powered by PyMuPDF, sentence-transformers, FAISS, and NLTK.

## Tech Stack Used

- **FastAPI:** Python API backend
- **PyMuPDF:** Fast and efficient PDF parsing (`fitz`)
- **Sentence Transformers:** For semantic text embeddings
- **FAISS:** Fast vector similarity search
- **NLTK:** Paragraph and sentence chunking for robust document handling

## How to Run Locally

1. **Clone the Repository**
git clone https://github.com/ananya1906/pdf-ai-assistant.git
cd pdf-ai-assistant


2. **Install Dependencies**
pip install -r requirements.txt


3. **Start the FastAPI Server**
uvicorn backend.app:app --reload


4. **Open Swagger Docs**
Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## How to Test

1. **Upload One or More PDFs:**  
Use the `/upload/` endpoint and select your PDF(s).

2. **Ask Questions:**  
Use the `/query/` endpoint and type in your natural language queries.

3. **Sample PDFs:**  
Use the provided files in `sample-pdf/` or add your own.

## Known Issues / Limitations

- Only processes text-based PDFs (does not extract from scanned images).
- Embeddings saved in a local pickle file (`embeddings.pkl`) each session.
- No authentication or user separation—future improvement.
- Processing very large PDFs may have memory limits depending on your system.

## File Structure

backend/
│ app.py
│ pdf_parser.py
│ embedding.py
│ vector_db.py
│ storage.py
│ requirements.txt

sample pdf/
│ AI-assignment.pdf


## Instructions to Run Locally

- Follow steps under "How to Run Locally" above.
- All source code and dependencies are in the backend folder.
- Example PDF files are in the sample pdf folder.

---



