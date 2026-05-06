class TopicDiscoveryEngine:
    """
    Advanced topic modeling for discovering themes and trends
    """

    def __init__(self, n_topics=5, method='lda'):
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.decomposition import LatentDirichletAllocation

        self.n_topics = n_topics
        self.method = method

        # Vectorizer for topic modeling
        self.vectorizer = CountVectorizer(
            max_df=0.9,
            min_df=1,  # Changed from 2 to 1 to prevent pruning all terms on small datasets
            stop_words='english'
        )

        # LDA model
        self.model = LatentDirichletAllocation(
            n_components=self.n_topics,
            random_state=42
        )

        self.feature_names = None
        self.is_trained = False

    # -------------------------------
    # 🧠 Fit Topics
    # -------------------------------

    def fit_topics(self, documents):
        """
        Discover topics in a collection of documents
        """

        # Vectorize documents
        doc_term_matrix = self.vectorizer.fit_transform(documents)
        self.feature_names = self.vectorizer.get_feature_names_out()

        # Train LDA
        self.model.fit(doc_term_matrix)

        self.is_trained = True

    # -------------------------------
    # 📄 Get Topics for Single Article
    # -------------------------------

    def get_article_topics(self, article_text):
        """
        Get topic distribution for a single article
        """

        if not self.is_trained:
            raise Exception("Model not trained yet!")

        vec = self.vectorizer.transform([article_text])
        topic_distribution = self.model.transform(vec)[0]

        return {
            f"Topic_{i}": float(score)
            for i, score in enumerate(topic_distribution)
        }

    # -------------------------------
    # 📈 Track Topic Trends Over Time
    # -------------------------------

    def track_topic_trends(self, articles_with_dates):
        """
        Analyze how topics change over time
        articles_with_dates = [(text, datetime), ...]
        """

        import pandas as pd

        if not self.is_trained:
            raise Exception("Model not trained yet!")

        records = []

        for text, date in articles_with_dates:
            topics = self.get_article_topics(text)

            for topic, score in topics.items():
                records.append({
                    "date": pd.to_datetime(date).date(),
                    "topic": topic,
                    "score": score
                })

        df = pd.DataFrame(records)

        # Aggregate by date + topic
        trend_df = df.groupby(["date", "topic"])["score"].mean().reset_index()

        return trend_df

    # -------------------------------
    # 🎨 Visualize Topics
    # -------------------------------

    def visualize_topics(self, top_n_words=10):
        """
        Display top words for each topic
        """

        if not self.is_trained:
            raise Exception("Model not trained yet!")

        topics = {}

        for idx, topic in enumerate(self.model.components_):
            top_indices = topic.argsort()[::-1][:top_n_words]
            top_words = [self.feature_names[i] for i in top_indices]

            topics[f"Topic_{idx}"] = top_words

        return topics


# -------------------------------
# 🧪 Example Usage
# -------------------------------

if __name__ == "__main__":
    documents = [
        "The government passed a new law on taxes",
        "Stock markets are growing rapidly",
        "AI is transforming technology industries",
        "Elections are coming soon",
        "Inflation affects global economy"
    ]

    topic_engine = TopicDiscoveryEngine(n_topics=3)
    topic_engine.fit_topics(documents)

    article = "AI is changing the global economy"

    print("📄 Article Topics:")
    print(topic_engine.get_article_topics(article))

    print("\n🎨 Topics:")
    print(topic_engine.visualize_topics())

print("🔍 Topic discovery engine ready for implementation!")
