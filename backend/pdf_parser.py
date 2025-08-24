import fitz

def extract_text_chunks(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    chunks = []
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")
        current_chunk = ""
        for block in blocks:
            text = block[4].strip()
            
            if len(text) < 25:
                current_chunk += text + " "
            else:
                current_chunk += text
                chunks.append({"text": current_chunk.strip(), "source": f"page_{page_num+1}"})
                current_chunk = ""
       
        if current_chunk:
            chunks.append({"text": current_chunk.strip(), "source": f"page_{page_num+1}"})
    return chunks
