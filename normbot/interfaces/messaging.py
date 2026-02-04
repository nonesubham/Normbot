from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Message:
    """Represents a message from any messaging platform"""
    user_id: str
    text: str
    platform: str
    message_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class MessagingProvider(ABC):
    """Abstract base class for all messaging platforms"""
    
    @abstractmethod
    async def connect(self) -> bool:
        """Initialize connection to messaging service"""
        pass
    
    @abstractmethod
    async def send_message(self, user_id: str, text: str, **kwargs) -> bool:
        """Send a message to user"""
        pass
    
    @abstractmethod
    async def request_approval(self, user_id: str, action_summary: str, 
                              action_id: str) -> bool:
        """Request approval for an action from user"""
        pass
    
    @abstractmethod
    async def receive_messages(self) -> Message:
        """Yield incoming messages (generator)"""
        pass
    
    @abstractmethod
    def get_platform_name(self) -> str:
        """Return platform identifier"""
        pass
    
    async def disconnect(self):
        """Cleanup connection (optional)"""
        pass