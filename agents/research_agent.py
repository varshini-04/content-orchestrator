import os
import requests
from groq import Groq
from duckduckgo_search import DDGS
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:
    def __init__(self, model_id="llama-3.3-70b-versatile"):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model_id = model_id

class ResearchAgent(BaseAgent):
    def run(self, topic):
        with DDGS() as ddgs:
            results = list(ddgs.text(topic, max_results=5))
        
        search_data = "\n".join([f"Title: {r['title']}\nSnippet: {r['body']}" for r in results])
        return search_data
