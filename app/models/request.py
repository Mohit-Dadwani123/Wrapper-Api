from pydantic import BaseModel
from .enums import Provider
from .shared import LLMConfig, VoiceConfig

class AgentCreateRequest(BaseModel):
    provider: Provider
    agent_name: str
    llm: LLMConfig
    voice: VoiceConfig
