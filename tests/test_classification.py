from src.analysis.classifier import AdvancedNewsClassifier

def test_classifier_training_and_prediction():
    model = AdvancedNewsClassifier()

    X_train = [
        "Stock market is rising",
        "Team won the match",
        "New government policy announced"
    ]
    
    y_train = ["business", "sport", "politics"]

    model.train(X_train, y_train)

    predictions = model.predict(["Government announces new law"])

    assert len(predictions) == 1
