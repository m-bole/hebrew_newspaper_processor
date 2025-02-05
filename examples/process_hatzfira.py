from hebrew_newspaper_processor.ocr_processor import OCRProcessor
from hebrew_newspaper_processor.text_cleaner import TextCleaner
from hebrew_newspaper_processor.pos_tagger import POSTagger
import glob
import os

def process_newspaper(pdf_dir):
    """Process all PDFs in directory."""
    ocr = OCRProcessor()
    cleaner = TextCleaner()
    tagger = POSTagger()

    for pdf_path in glob.glob(f'{pdf_dir}/*.pdf'):
        print(f"Processing {pdf_path}")
        
        # OCR
        ocr_path = ocr.process_pdf(pdf_path)
        print(f"OCR completed: {ocr_path}")

        # Clean
        clean_path = cleaner.process_file(ocr_path)
        print(f"Cleaning completed: {clean_path}")

        # POS tag
        pos_path = tagger.process_file(clean_path)
        print(f"POS tagging completed: {pos_path}")

if __name__ == "__main__":
    pdf_dir = "path/to/your/pdfs"
    process_newspaper(pdf_dir)
