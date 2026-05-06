from src.analysis.classifier import AdvancedNewsClassifier
from src.language_models.summarizer import IntelligentSummarizer

def test_basic_pipeline():
    # Step 1: Train classifier
    classifier = AdvancedNewsClassifier()

    X_train = [
        "Stock market rises",
        "Team wins championship",
        "Election results announced"
    ]
    
    y_train = ["business", "sport", "politics"]

    classifier.train(X_train, y_train)

    # Step 2: Predict
    prediction = classifier.predict(["New economic policy introduced"])
    
    assert len(prediction) == 1

def test_summarization():
    summarizer = IntelligentSummarizer()

    text = "Artificial intelligence is rapidly growing. It is used in many industries."

    summary = summarizer.extractive_summary(text)

    assert isinstance(summary, str)
    assert len(summary) > 0
