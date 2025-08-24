import fitz

def extract_text_chunks(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    chunks = []
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        for block in page.get_text("blocks"):
            text = block[4].strip()
            if text:
                chunks.append({"text": text, "source": f"page_{page_num+1}"})
    return chunks
