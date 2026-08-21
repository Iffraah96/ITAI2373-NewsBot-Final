# 📰 NewsBot 2.0 — Intelligent News Analysis System

> An NLP-based news intelligence project that combines text classification, topic discovery, sentiment analysis, named entity recognition, semantic search, summarization, multilingual processing, and conversational query understanding.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-green)](https://en.wikipedia.org/wiki/Natural_language_processing)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?logo=spacy)](https://spacy.io/)
[![Transformers](https://img.shields.io/badge/Transformers-Hugging%20Face-yellow)](https://huggingface.co/)

---

## 📌 Overview

**NewsBot 2.0** is an advanced Natural Language Processing project designed to transform unstructured news articles into structured information and useful insights.

The project brings together multiple NLP and machine learning techniques into a modular workflow rather than treating each technique as an isolated task.

Given a news article, the system can analyze areas such as:

* 🏷️ Article classification
* 😊 Sentiment
* 🧠 Topics
* 👤 Named entities
* 🔗 Entity relationships
* ✂️ Article summaries
* 🔎 Semantically similar articles
* 🌍 Language detection
* 💬 Natural-language user queries

The project was developed as a comprehensive AI/NLP learning project and demonstrates how multiple NLP components can be integrated into a larger intelligent-information system.

---

# 🎯 Project Goals

The main goals of NewsBot 2.0 are to:

* Process and analyze unstructured news text
* Extract meaningful information from articles
* Discover hidden topics and trends
* Analyze sentiment and sentiment changes over time
* Identify important people, organizations, and locations
* Explore relationships between entities
* Generate concise article summaries
* Search articles based on semantic similarity
* Detect the language of incoming content
* Understand natural-language news queries
* Integrate multiple NLP components into one system
* Create a foundation for a future real-time news intelligence platform

---

# 🧠 Core Capabilities

## 1. 🏷️ News Classification

NewsBot includes an `AdvancedNewsClassifier` based on:

* TF-IDF feature extraction
* Logistic Regression
* One-vs-Rest classification
* Confidence scoring
* Alternative category predictions
* Feature-based explanation

The classifier is designed to return a primary category along with confidence scores and alternative categories.

### Example

```text
Prediction:
Primary Category: Politics
Confidence: 0.4523

Alternatives:
Technology: 0.3001
Economy: 0.2292
```

The notebook also demonstrates an explanation mechanism that identifies influential TF-IDF terms associated with a prediction.

> **Note:** The notebook contains a working classifier implementation and demonstration, but the final integrated example requires the classifier to be trained before production-style predictions can be made.

---

# 2. 🧠 Topic Discovery

NewsBot uses **Latent Dirichlet Allocation (LDA)** for unsupervised topic discovery.

The topic engine can:

* Discover multiple topics
* Assign topic distributions to articles
* Extract representative topic words
* Track topic scores over time
* Visualize topic information

### Example Topic Output

```text
Topic_0:
stock, growing, markets, rapidly, elections...

Topic_1:
taxes, law, government, economy, inflation...

Topic_2:
technology, AI, industries, transforming...
```

This allows the system to move beyond simple keyword matching and identify broader themes within a collection of articles.

---

# 3. 😊 Sentiment Analysis

NewsBot uses **VADER sentiment analysis** to classify text as:

* Positive
* Negative
* Neutral

The system returns:

* Overall sentiment
* Compound sentiment score
* Positive score
* Negative score
* Neutral score

It also includes functionality for tracking sentiment over time and identifying unusual sentiment patterns.

### Example

```text
Text:
"This is a fantastic product! I love it."

Sentiment:
Positive

Compound Score:
0.8439
```

The notebook also demonstrates a daily sentiment timeline containing positive, neutral, and negative sentiment values across multiple dates.

---

# 4. 👤 Named Entity Recognition

The project uses **spaCy** for Named Entity Recognition (NER).

Entities can include:

* People
* Organizations
* Locations
* Geopolitical entities
* Other recognized entity types

### Example

```text
Article:
"Elon Musk is the CEO of Tesla. Tesla is based in the United States."

Entities:
Elon Musk → PERSON
Tesla → ORG
United States → GPE
```

---

# 5. 🔗 Entity Relationship Mapping

NewsBot extends entity extraction into relationship analysis.

The `EntityRelationshipMapper` can:

* Extract entities
* Identify entity co-occurrences
* Extract simple rule-based relationships
* Build a NetworkX knowledge graph
* Search for connections between entities

Example relationships include:

```text
Elon Musk → Tesla
Tesla → United States
```

This provides a foundation for understanding how people, organizations, locations, and other entities are connected within news content.

---

# 6. ✂️ Intelligent Summarization

The project includes an `IntelligentSummarizer`.

The current implementation uses **extractive summarization**, selecting important sentences from the original article.

It supports:

```text
Brief      → 2 sentences
Balanced   → 3 sentences
Detailed   → 5 sentences
```

The summarizer also includes:

* Multi-article summarization
* Simple headline generation
* Summary coverage measurement
* Compression ratio calculation

### Important Implementation Note

The notebook originally explores transformer-based summarization, but the implemented fallback uses extractive summarization so that the system can continue operating when a generative summarization pipeline is unavailable.

---

# 7. 🔎 Semantic Search

NewsBot includes semantic search using:

**Sentence Transformers — `all-MiniLM-L6-v2`**

Articles are converted into embeddings and compared using cosine similarity.

This enables searches based on **meaning**, rather than requiring exact keyword matches.

### Example

Query:

```text
technology and AI
```

Possible results:

```text
AI is transforming the technology industry
Similarity: 0.7080

Advances in artificial intelligence continue
Similarity: 0.6051

New regulations impact tech companies
Similarity: 0.3310
```

The system can also cluster similar articles using K-Means.

---

# 8. 🌍 Multilingual Processing

The project includes a `MultilingualProcessor` designed to support:

| Code | Language |
| ---- | -------- |
| `en` | English  |
| `es` | Spanish  |
| `ar` | Arabic   |
| `ur` | Urdu     |
| `hi` | Hindi    |
| `zh` | Chinese  |

The current implementation provides:

* Language detection
* Detection confidence
* Cultural keyword detection
* Cross-language article comparison structure

### ⚠️ Current Limitation

Translation is currently implemented as a **placeholder interface** rather than a fully connected translation service.

Future versions could integrate:

* Hugging Face translation models
* Google Translate
* Azure Translator
* Other dedicated translation APIs

---

# 9. 💬 Conversational Interface

NewsBot includes a conversational interface for understanding natural-language queries.

The system can identify intents such as:

```text
search
summarize
analyze_sentiment
compare
explain_relationship
trend_analysis
general_query
```

It can also extract:

* Sentiment filters
* News categories
* Timeframes
* Companies/entities
* Search keywords

### Example

User:

```text
Show me positive tech news from this week
```

The system identifies:

```text
Intent:
search

Category:
tech

Sentiment:
positive

Timeframe:
this week
```

The interface also supports follow-up queries using stored conversation context.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │     News Article     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Text Processing &   │
                    │   Feature Extraction │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │Classification│  │  Sentiment  │  │   Topics    │
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │   Entity Extraction  │
                    │   & Relationships    │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      ┌────────────┐   ┌────────────┐   ┌──────────────┐
      │ Summarizer │   │  Semantic  │   │ Multilingual │
      │            │   │   Search   │   │  Processing  │
      └──────┬─────┘   └──────┬─────┘   └──────┬───────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Conversational Query │
                    │      Interface       │
                    └──────────────────────┘
```

---

# 🛠️ Technology Stack

## Programming

* Python
* Jupyter Notebook

## NLP

* NLTK
* spaCy
* Transformers
* Sentence Transformers
* Gensim

## Machine Learning

* Scikit-learn
* Logistic Regression
* One-vs-Rest Classification
* TF-IDF
* LDA
* K-Means
* Cosine Similarity

## NLP Techniques

* Text preprocessing
* Tokenization
* Lemmatization
* POS tagging
* Named Entity Recognition
* Sentiment analysis
* Topic modeling
* Text summarization
* Semantic search
* Language detection
* Intent classification

## Data & Visualization

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* WordCloud

## Other Tools

* NetworkX
* Requests
* BeautifulSoup
* Git
* GitHub

---

# 📂 Project Structure

```text
ITAI2373-NewsBot-Final/
│
├── config/
│   └── settings.py
│
├── data/
│   └── raw/
│
├── docs/
│
├── notebooks/
│   └── FP_Newsbot2_0_Iffraah_Rehman_ITAI2373.ipynb
│
├── reports/
│
├── src/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Iffraah96/ITAI2373-NewsBot-Final.git
cd ITAI2373-NewsBot-Final
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Additional NLP resources/models may be required depending on the notebook environment.

For example:

```python
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("vader_lexicon")
```

The spaCy English model used by the notebook is:

```bash
python -m spacy download en_core_web_sm
```

---

# ▶️ Running the Project

Open the main notebook:

```text
notebooks/FP_Newsbot2_0_Iffraah_Rehman_ITAI2373.ipynb
```

Then run the notebook cells sequentially.

The notebook demonstrates the individual NewsBot components and their integration into a larger system.

---

# 🧪 Testing & Evaluation

The project includes a testing framework covering:

### Component Testing

Individual tests for:

* Classification
* Sentiment analysis
* Entity extraction
* Topic modeling
* Summarization
* Language detection

### Integration Testing

The project includes an end-to-end analysis workflow that combines multiple components.

### Performance Testing

The framework measures:

* Number of articles processed
* Total processing time
* Average processing time per article

### Edge Cases

The testing framework considers:

* Empty text
* Very short text
* Very long text
* Non-English text
* Malformed input

---

# 📊 Demonstrated Results

The notebook contains several working demonstrations.

| Component            | Demonstration                                         |
| -------------------- | ----------------------------------------------------- |
| Sentiment Analysis   | Positive, negative, and neutral classification        |
| Topic Modeling       | LDA topic distributions and topic words               |
| Entity Extraction    | PERSON, ORG, GPE entities                             |
| Relationship Mapping | Entity co-occurrence and rule-based relationships     |
| Semantic Search      | Similarity-based article retrieval                    |
| Article Clustering   | K-Means grouping of related content                   |
| Summarization        | Extractive article summaries                          |
| Language Detection   | Language identification with confidence               |
| Conversational AI    | Intent, category, sentiment, and timeframe extraction |

### Example Integrated Analysis

For a sample AI article, the system produced:

```text
Sentiment:
Positive

Compound Score:
0.8519

Detected Entity:
AI

Detected Language:
English

Related Articles:
Similarity scores up to approximately 0.58

Summary:
Extractive summary generated from the source article
```

---

# ⚠️ Current Limitations

This project is an educational and portfolio implementation, and several components are intentionally designed as foundations for future development.

### Real-Time News

The project does not currently depend on a live news feed. Real-time NewsAPI/GDELT integration is a future enhancement.

---

# 🔮 Future Improvements

## Phase 1 — Stronger NLP Models

* Fine-tune transformer-based classifiers
* Improve named entity recognition
* Add transformer-based summarization
* Improve relation extraction
* Add better multilingual models

## Phase 2 — Real-Time News

* Integrate NewsAPI or GDELT
* Automatically collect new articles
* Schedule periodic analysis
* Track emerging topics
* Monitor sentiment changes

## Phase 3 — Interactive Application

Build a web interface with:

* Streamlit or Flask
* Interactive dashboards
* Search functionality
* Article analysis
* Topic visualizations
* Sentiment trends
* Knowledge graphs
* Conversational querying

## Phase 4 — Production Architecture

Potential improvements include:

* Vector database integration
* Persistent article storage
* API layer
* Authentication
* Model serving
* Cloud deployment
* Automated testing and CI/CD

---

# 🎓 What I Learned

This project helped me move from implementing individual NLP techniques to thinking about how multiple AI components can work together as a larger system.

### Technical Skills

* Natural Language Processing
* Machine Learning
* Text preprocessing
* TF-IDF feature engineering
* Classification
* Topic modeling
* Sentiment analysis
* Named Entity Recognition
* Semantic embeddings
* Similarity search
* Text summarization
* Multilingual NLP
* Conversational AI
* Knowledge graphs
* Python development

### Software Engineering Skills

* Modular architecture
* Component integration
* Error handling
* Testing
* Configuration management
* Project organization
* Documentation
* Git/GitHub workflow

---

# 💼 Potential Real-World Applications

A system based on this architecture could eventually support:

* 📰 News aggregation
* 📊 Media monitoring
* 📈 Trend detection
* 😊 Public sentiment monitoring
* 🔎 Research assistance
* 🏢 Competitive intelligence
* 🌍 Cross-language news analysis
* 🤖 AI-powered news assistants

---

# 🚀 Why This Project Matters

NewsBot 2.0 demonstrates an important transition from **learning individual machine learning algorithms** to designing a broader AI system.

Instead of asking:

> "Can I classify this text?"

the project explores:

> "How can multiple NLP capabilities work together to understand, organize, search, summarize, and interact with large collections of news content?"

That systems-level perspective is the primary goal of the project.

---

# 👩‍💻 Author

## Iffraah Rehman

AI & Computer Science Student
Machine Learning | NLP | Artificial Intelligence

### 🔗 GitHub

https://github.com/Iffraah96

### 🔗 Project Repository

https://github.com/Iffraah96/ITAI2373-NewsBot-Final

---

# 📜 License

This project was developed primarily for educational and portfolio purposes.

---

## ⭐ Like the Project?

If you find the project interesting, feel free to explore the repository, review the notebook, and connect with me.

**Built with Python, NLP, Machine Learning, and a lot of experimentation. 🤖📰**
