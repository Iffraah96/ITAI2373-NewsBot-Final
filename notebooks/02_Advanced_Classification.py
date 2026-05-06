# 📊 Advanced Classification System
# TODO: Build your enhanced classification system
class AdvancedNewsClassifier:
    """    Enhanced news classification with confidence scoring and multi-label support
    TODO: This should be much more sophisticated than your midterm classifier
    """
    def __init__(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.multiclass import OneVsRestClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import Pipeline

        # 🔹 Pipeline: TF-IDF + Multi-label Logistic Regression
        self.pipeline = Pipeline([
            ("tfidf", TfidfVectorizer(max_features=1000, stop_words="english")),
            ("clf", OneVsRestClassifier(LogisticRegression(max_iter=1000)))
        ])

        self.is_trained = False
        self.label_names = None

    # -------------------------------
    # 🧠 Training
    # -------------------------------
    def train(self, X_train, y_train, label_names):
        """
        Train the classification model
        """

        # Store label names (important for decoding predictions)
        self.label_names = label_names

        # Train model
        self.pipeline.fit(X_train, y_train)
        self.is_trained = True

    # -------------------------------
    # 🔮 Prediction with Confidence
    # -------------------------------

    def predict_with_confidence(self, article_text):
        """
        Predict categories with confidence scores
        """

        if not self.is_trained:
            raise Exception("Model not trained yet!")

        # Get probabilities
        probs = self.pipeline.predict_proba([article_text])[0]

        results = dict(zip(self.label_names, probs))

        # Sort by confidence
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

        primary_category = sorted_results[0]
        alternatives = sorted_results[1:3]

        return {
            "primary_category": primary_category[0],
            "confidence": float(primary_category[1]),
            "alternatives": alternatives,
            "all_scores": results
        }

    # -------------------------------
    # 🔍 Explain Prediction
    # -------------------------------

    def explain_prediction(self, article_text):
        """
        Provide explanation using top TF-IDF features
        """

        if not self.is_trained:
            raise Exception("Model not trained yet!")

        vectorizer = self.pipeline.named_steps["tfidf"]
        classifier = self.pipeline.named_steps["clf"]

        feature_names = vectorizer.get_feature_names_out()
        article_vector = vectorizer.transform([article_text])

        # Get top features in this article
        sorted_indices = article_vector.toarray()[0].argsort()[::-1][:10]
        top_words = [feature_names[i] for i in sorted_indices]

        return {
            "key_influential_words": top_words
        }


# -------------------------------
# 🧪 Example Usage
# -------------------------------

if __name__ == "__main__":
    # Dummy data
    X = [
        "The government passed a new law on taxes",
        "Stock markets are seeing rapid growth",
        "New AI technology is transforming industries",
        "Elections are coming up next month"
    ]

    y = [
        [1, 0, 0],  # Politics
        [0, 1, 0],  # Economy
        [0, 0, 1],  # Tech
        [1, 0, 0]   # Politics
    ]

    labels = ["Politics", "Economy", "Technology"]

    classifier = AdvancedNewsClassifier()
    classifier.train(X, y, labels)

    test_article = "AI is impacting economic policies worldwide"

    prediction = classifier.predict_with_confidence(test_article)
    explanation = classifier.explain_prediction(test_article)

    print("Prediction:", prediction)
    print("Explanation:", explanation)

    print("📊 Advanced classification system ready for implementation!")
