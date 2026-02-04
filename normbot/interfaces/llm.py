from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from enum import Enum

class LLMType(Enum):
    MAIN = "main"
    SANDBOX = "sandbox"

class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    def __init__(self, llm_type: LLMType = LLMType.MAIN, **kwargs):
        self.llm_type = llm_type
        self.config = kwargs
    
    @abstractmethod
    async def generate(self, 
                      prompt: str, 
                      system_prompt: Optional[str] = None,
                      temperature: float = 0.7,
                      max_tokens: int = 1000) -> str:
        """Generate completion from LLM"""
        pass
    
    @abstractmethod
    async def generate_structured(self, 
                                 prompt: str,
                                 schema: Dict[str, Any],
                                 system_prompt: Optional[str] = None) -> Dict[str, Any]:
        """Generate structured JSON output according to schema"""
        pass
    
    @abstractmethod
    def get_context_window(self) -> int:
        """Return context window size in tokens"""
        pass
    
    def is_sandboxed(self) -> bool:
        """Check if this instance is sandboxed (no system access)"""
        return self.llm_type == LLMType.SANDBOX