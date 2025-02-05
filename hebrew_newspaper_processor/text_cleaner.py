import re
import os

class TextCleaner:
    def __init__(self):
        self.hebrew_pattern = r'[^\u0590-\u05FF\uFB1D-\uFB4F\s\.\,\?\!\-]'

    def clean_text(self, text):
        """Clean and normalize Hebrew text."""
        cleaned = re.sub(self.hebrew_pattern, ' ', text)
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned.strip()

    def process_file(self, input_path, output_dir='cleaned_texts'):
        """Process text file and save cleaned version."""
        os.makedirs(output_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f'{output_dir}/{base_name}_clean.txt'

        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()

        cleaned_text = self.clean_text(text)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

        return output_path
