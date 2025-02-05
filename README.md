# Hebrew Newspaper OCR and POS Tagging Processor

A Python package for processing historical Hebrew newspapers through OCR and linguistic annotation. This project was developed for processing Ha-Tsfira (הצפירה) newspaper, but can be used with other Hebrew newspaper scans.

## Project Overview

This tool processes historical Hebrew newspaper PDFs through:
1. Page splitting and OCR
2. Text cleaning and normalization
3. Part-of-Speech (POS) tagging

## Dataset

The processed Ha-Tsfira dataset is available on HuggingFace:
[mbole/hebrew-tzfira-dataset](https://huggingface.co/datasets/mbole/hebrew-tzfira-dataset)

### Dataset Details
- 50 newspaper issues from 1862-1976
- Each document contains:
  - Original OCR text
  - Cleaned text
  - POS-tagged text
- Total size: 15.2 MB
- Format: Hugging Face Dataset

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/hebrew-newspaper-processor.git
cd hebrew-newspaper-processor

# Install requirements
pip install -r requirements.txt
```

## System Requirements

Python 3.7+
Tesseract-OCR with Hebrew support
Poppler-utils

##  On Ubuntu/Debian:
bashCopysudo apt-get install tesseract-ocr tesseract-ocr-heb poppler-utils

### Usage
```python
from hebrew_newspaper_processor.ocr_processor import OCRProcessor
from hebrew_newspaper_processor.text_cleaner import TextCleaner
from hebrew_newspaper_processor.pos_tagger import POSTagger

# Initialize processors
ocr = OCRProcessor()
cleaner = TextCleaner()
tagger = POSTagger()

# Process a single PDF
pdf_path = "path/to/newspaper.pdf"
ocr_path = ocr.process_pdf(pdf_path)
clean_path = cleaner.process_file(ocr_path)
pos_path = tagger.process_file(clean_path)
```

See examples/process_hatzfira.py for batch processing example.

### Project Structure
```
hebrew_newspaper_processor/
├── hebrew_tsfira.ipynb # Notebook I used for analysis 
├── hebrew_newspaper_processor/
│   ├── ocr_processor.py    # PDF processing and OCR
│   ├── text_cleaner.py     # Text cleaning and normalization
│   ├── pos_tagger.py       # POS tagging using Stanza
│   └── utils.py            # Utility functions
└── examples/
    └── process_hatzfira.py # Usage example
```

### Features
- Automatic page splitting for two-column layouts
- Hebrew-specific OCR using Tesseract
- Text cleaning preserving Hebrew characters
- POS tagging using Stanza Hebrew model
- Batch processing support
- Progress tracking and logging

### Citation
If you use this tool or dataset in your research, please cite:
```
bibtexCopy@misc{bolek2025hatzfira,
    title={OCR and Corpus Analysis of Ha-Tsfira Hebrew Newspaper},
    author={Maria Bolek},
    year={2025},
    publisher={University of Warsaw},
    howpublished={https://huggingface.co/datasets/mbole/hebrew-tzfira-dataset}
}
```

### License
MIT License

### Contact
Maria Bolek
University of Warsaw
maria.bolek@uw.edu.pl


### Acknowledgments
National Library of Israel for providing access to Ha-Tsfira archives
Stanza team for the Hebrew NLP model
Tesseract OCR project for Hebrew language support

