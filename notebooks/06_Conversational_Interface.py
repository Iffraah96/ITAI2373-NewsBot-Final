# 🎯 Intent Classification and Query Understanding

class ConversationalInterface:
    """
    Advanced conversational AI for natural language interaction with NewsBot
    """

    def __init__(self, newsbot_system):
        self.newsbot = newsbot_system

        # Store conversation memory
        self.conversation_history = []
        self.current_context = {
            "last_intent": None,
            "last_entities": {},
            "last_results": None
        }

    def classify_intent(self, user_query):
        """
        Classify user intent from natural language query.
        """

        query = user_query.lower()

        if any(word in query for word in ["search", "find", "show me", "articles about"]):
            return "search"

        elif any(word in query for word in ["summarize", "summary", "brief"]):
            return "summarize"

        elif any(word in query for word in ["sentiment", "tone", "positive", "negative"]):
            return "analyze_sentiment"

        elif any(word in query for word in ["compare", "versus", "vs", "difference"]):
            return "compare"

        elif any(word in query for word in ["explain", "relationship", "connected", "link"]):
            return "explain_relationship"

        elif any(word in query for word in ["trend", "trending", "popular", "emerging"]):
            return "trend_analysis"

        else:
            return "general_query"

    def extract_query_entities(self, user_query):
        """
        Extract entities and parameters from user queries.
        """

        import re

        query = user_query.lower()

        entities = {
            "sentiment": None,
            "category": None,
            "timeframe": None,
            "companies": [],
            "keywords": []
        }

        # Sentiment
        if "positive" in query:
            entities["sentiment"] = "positive"
        elif "negative" in query:
            entities["sentiment"] = "negative"
        elif "neutral" in query:
            entities["sentiment"] = "neutral"

        # Category
        categories = ["technology", "tech", "politics", "business", "economy", "health", "sports", "science"]
        for category in categories:
            if category in query:
                entities["category"] = category

        # Timeframe
        if "today" in query:
            entities["timeframe"] = "today"
        elif "this week" in query:
            entities["timeframe"] = "this week"
        elif "last week" in query:
            entities["timeframe"] = "last week"
        elif "this month" in query:
            entities["timeframe"] = "this month"
        elif "last month" in query:
            entities["timeframe"] = "last month"

        # Simple company/entity extraction using capitalized words
        companies = re.findall(r"\b[A-Z][a-zA-Z]+\b", user_query)
        entities["companies"] = companies

        # Keywords
        stopwords = {
            "show", "me", "find", "search", "about", "the", "a", "an",
            "compare", "summarize", "analyze", "what", "is", "are",
            "from", "this", "last", "week", "month", "today"
        }

        words = re.findall(r"\b\w+\b", query)
        entities["keywords"] = [w for w in words if w not in stopwords]

        return entities

    def process_query(self, user_query, conversation_context=None):
        """
        Process natural language query and generate response.
        """

        intent = self.classify_intent(user_query)
        entities = self.extract_query_entities(user_query)

        # Store basic query result
        query_results = {
            "intent": intent,
            "entities": entities,
            "message": "Query processed successfully."
        }

        # Example routing logic
        if intent == "summarize":
            query_results["result"] = "I can summarize articles related to your query."

        elif intent == "analyze_sentiment":
            query_results["result"] = "I can analyze sentiment trends for the requested topic."

        elif intent == "compare":
            query_results["result"] = "I can compare coverage, sentiment, and entities between the requested topics."

        elif intent == "search":
            query_results["result"] = "I can search for articles matching your keywords."

        elif intent == "explain_relationship":
            query_results["result"] = "I can explain relationships between people, organizations, and topics."

        elif intent == "trend_analysis":
            query_results["result"] = "I can identify emerging trends from article collections."

        else:
            query_results["result"] = "I understood your query and can help analyze related news content."

        response = self.generate_response(query_results, intent, entities)

        # Update context
        self.current_context = {
            "last_intent": intent,
            "last_entities": entities,
            "last_results": query_results
        }

        self.conversation_history.append({
            "user_query": user_query,
            "intent": intent,
            "entities": entities,
            "response": response
        })

        return response

    def generate_response(self, query_results, intent, entities):
        """
        Generate helpful natural language responses.
        """

        response = f"Intent detected: {intent}\n\n"

        if entities.get("category"):
            response += f"Category: {entities['category']}\n"

        if entities.get("sentiment"):
            response += f"Sentiment filter: {entities['sentiment']}\n"

        if entities.get("timeframe"):
            response += f"Timeframe: {entities['timeframe']}\n"

        if entities.get("companies"):
            response += f"Entities found: {', '.join(entities['companies'])}\n"

        if entities.get("keywords"):
            response += f"Keywords: {', '.join(entities['keywords'])}\n"

        response += f"\nResponse: {query_results.get('result')}"

        return response

    def handle_follow_up(self, follow_up_query, conversation_history=None):
        """
        Handle follow-up questions using previous context.
        """

        if conversation_history is None:
            conversation_history = self.conversation_history

        if not conversation_history:
            return self.process_query(follow_up_query)

        previous_context = self.current_context
        new_entities = self.extract_query_entities(follow_up_query)

        # Merge old and new context
        merged_entities = previous_context["last_entities"].copy()

        for key, value in new_entities.items():
            if value:
                merged_entities[key] = value

        intent = self.classify_intent(follow_up_query)

        if intent == "general_query":
            intent = previous_context["last_intent"]

        query_results = {
            "intent": intent,
            "entities": merged_entities,
            "result": "Follow-up query processed using previous conversation context."
        }

        response = self.generate_response(query_results, intent, merged_entities)

        self.conversation_history.append({
            "user_query": follow_up_query,
            "intent": intent,
            "entities": merged_entities,
            "response": response
        })

        return response


#-------------------------------------------
# Test conversation
#-------------------------------------------
# conversation = ConversationalInterface(newsbot_system)

conversation = ConversationalInterface(newsbot_system=None)

print(conversation.process_query("Show me positive tech news from this week"))

print(conversation.handle_follow_up("What about last month?"))

print("💬 Conversational interface ready for implementation!")
