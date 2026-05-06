import pytest
from src.data_processing.text_preprocessor import TextPreprocessor

def test_clean_text():
    processor = TextPreprocessor()
    text = "Hello!!! Visit http://example.com NOW!!!"
    
    cleaned = processor.clean_text(text)
    
    assert "http" not in cleaned
    assert cleaned.islower()

def test_preprocess_pipeline():
    processor = TextPreprocessor()
    text = "This is a SIMPLE test sentence."

    processed = processor.preprocess(text)

    assert isinstance(processed, str)
    assert len(processed) > 0
