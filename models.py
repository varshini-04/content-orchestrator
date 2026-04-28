from pydantic import BaseModel, Field, ConfigDict
from typing import List

class JargonEntry(BaseModel):
    # This ensures every nested object also has additionalProperties: false
    model_config = ConfigDict(extra='forbid')
    term: str = Field(description="The technical term")
    definition: str = Field(description="The simple explanation")

class DistilledKnowledge(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    core_concept: str = Field(description="The main idea in one sentence")
    key_takeaways: List[str] = Field(description="3-5 bullet points of technical details")
    # Using a List of objects is much more stable than a Dict
    jargon_explained: List[JargonEntry] = Field(description="List of complex terms and definitions")