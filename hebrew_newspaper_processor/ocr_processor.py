import os
from PIL import Image, ImageEnhance, ImageOps
import pytesseract
import bidi.algorithm as bidi
from pdf2image import convert_from_path, pdfinfo_from_path

class OCRProcessor:
    def __init__(self, dpi=300):
        self.dpi = dpi

    def preprocess_image(self, image):
        """Preprocess image for better OCR results."""
        image = image.convert('L')
        image = ImageEnhance.Contrast(image).enhance(2.0)
        return ImageOps.autocontrast(image)

    def split_page(self, page_image):
        """Split page into right and left halves."""
        width = page_image.size[0]
        right_half = page_image.crop((width//2, 0, width, page_image.size[1]))
        left_half = page_image.crop((0, 0, width//2, page_image.size[1]))
        return right_half, left_half

    def process_image(self, image):
        """Process single image with OCR."""
        processed = self.preprocess_image(image)
        text = pytesseract.image_to_string(processed, lang='heb')
        return bidi.get_display(text).strip()

    def process_pdf(self, pdf_path, output_dir='ocr_output'):
        """Process PDF file and save OCR results."""
        os.makedirs(output_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = f'{output_dir}/{base_name}_ocr.txt'
        
        info = pdfinfo_from_path(pdf_path)
        ocr_texts = []

        for page in range(1, info["Pages"] + 1):
            images = convert_from_path(
                pdf_path, 
                dpi=self.dpi, 
                first_page=page, 
                last_page=page
            )
            page_image = images[0]
            right_half, left_half = self.split_page(page_image)

            for half in [right_half, left_half]:
                text = self.process_image(half)
                if text:
                    ocr_texts.append(text)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(ocr_texts))

        return output_path
