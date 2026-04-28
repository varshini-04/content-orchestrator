import os
from .research_agent import BaseAgent
from dotenv import load_dotenv

load_dotenv()

class AdapterAgent(BaseAgent):
    def to_twitter(self, structured_data):
        prompt = f"""Create a punchy, short tweet (under 280 characters) based on this technical data:
        {structured_data}
        
        Include 2 relevant hashtags. Focus on the core value."""
        
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def to_whatsapp(self, structured_data):
        prompt = f"""Create a very brief 2-sentence WhatsApp summary of this technical data:
        {structured_data}
        
        Include one 'learning' emoji (e.g. 📚, 💡, 🧠)."""
        
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
