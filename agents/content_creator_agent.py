import os
from .research_agent import BaseAgent
from dotenv import load_dotenv

load_dotenv()

class ContentCreatorAgent(BaseAgent):
    def run(self, structured_data):
        prompt = f"""You are a developer advocate building a personal brand. 
        Take these structured technical takeaways and draft an engaging LinkedIn post:
        
        {structured_data}
        
        Include a hook, the technical breakdown, and 3-5 relevant hashtags. Keep the tone professional but enthusiastic."""
        
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def refine(self, original_draft, critique):
        if "PASSED" in critique.upper():
            return original_draft
            
        prompt = f"""You are a developer advocate. Refine your LinkedIn post based on this expert critique.
        
        Original Draft:
        {original_draft}
        
        Critique:
        {critique}
        
        Produce a finalized version of the post that addresses all feedback while maintaining your brand voice."""
        
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
