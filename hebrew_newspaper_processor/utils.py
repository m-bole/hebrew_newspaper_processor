import os
import logging
from datetime import datetime
from typing import List, Tuple, Optional

class Logger:
    """Utility class for logging operations."""
    def __init__(self, log_dir: str = "logs"):
        os.makedirs(log_dir, exist_ok=True)
        log_file = f"{log_dir}/processor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

def check_file_exists(filepath: str) -> bool:
    """Check if file exists and is readable."""
    return os.path.exists(filepath) and os.path.isfile(filepath)

def get_file_info(filepath: str) -> dict:
    """Get file information including size and modification date."""
    if not check_file_exists(filepath):
        return {}
    
    stats = os.stat(filepath)
    return {
        'size': stats.st_size,
        'modified': datetime.fromtimestamp(stats.st_mtime),
        'created': datetime.fromtimestamp(stats.st_ctime)
    }

def create_output_dirs(base_dir: str, subdirs: List[str]) -> None:
    """Create multiple output directories."""
    for subdir in subdirs:
        os.makedirs(os.path.join(base_dir, subdir), exist_ok=True)

def get_processed_files(directory: str, suffix: str) -> List[str]:
    """Get list of processed files with specific suffix."""
    return [f for f in os.listdir(directory) if f.endswith(suffix)]

def batch_process_status(processed: List[str], total: int) -> Tuple[int, int, float]:
    """Calculate processing status."""
    completed = len(processed)
    remaining = total - completed
    progress = (completed / total) * 100 if total > 0 else 0
    return completed, remaining, progress

def validate_hebrew_text(text: str) -> Optional[str]:
    """Validate if text contains Hebrew characters."""
    hebrew_chars = set(chr(i) for i in range(0x0590, 0x05FF + 1))
    if any(c in hebrew_chars for c in text):
        return text
    return None

def clean_filename(filename: str) -> str:
    """Clean filename for consistent format."""
    # Remove any unwanted characters
    cleaned = ''.join(c for c in filename if c.isalnum() or c in '.-_')
    return cleaned.lower()

# Example usage in main code:
"""
from hebrew_newspaper_processor.utils import Logger, create_output_dirs

# Initialize logger
logger = Logger()

# Create necessary directories
create_output_dirs('output', ['ocr', 'cleaned', 'pos'])

# Log operations
logger.logger.info(f"Processing file: {filename}")
"""
