import os
from .research_agent import BaseAgent
from dotenv import load_dotenv

load_dotenv()

class CriticAgent(BaseAgent):
    def run(self, draft_text, structured_data):
        prompt = f"""You are a Technical Content Critic. 
        Compare this LinkedIn post draft with the original technical data and evaluate it for:
        1. Accuracy (Does it reflect the key technical details correctly?)
        2. Engagement (Is the hook strong? Is the tone right?)
        3. Formatting (Are the hashtags relevant? Is it easy to read?)

        Structured Data:
        {structured_data}

        Draft Post:
        {draft_text}

        If the post is excellent, respond with ONLY the word 'PASSED'.
        Otherwise, provide exactly 3 specific, actionable improvements."""
        
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
