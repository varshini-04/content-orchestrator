import os
import json
from .research_agent import BaseAgent
from models import DistilledKnowledge

class DistillationAgent(BaseAgent):
    def run(self, raw_data):
        prompt = f"""Extract core technical facts and takeaways from this research:
        {raw_data}
        
        Respond ONLY with a JSON object matching this schema:
        {{
            "topic": "topic name",
            "key_concepts": ["concept1", "concept2"],
            "technical_details": ["detail1", "detail2"],
            "suggested_hashtags": ["#tag1", "#tag2"]
        }}"""
        
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )
        return json.loads(response.choices[0].message.content)
