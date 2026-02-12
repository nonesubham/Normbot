from abc import ABC, abstractmethod
from data.base_message import Message


# Base Channel which had to be implemented in order to add messaing channel
class BaseChannel(ABC):
    """Abstract base class for all messaging platforms"""
    
    @abstractmethod
    async def connect(self, auth_key:str) -> bool:
        """Initialize connection to messaging service"""
        pass
    
    @abstractmethod
    async def send_message(self, user_id: str, message: Message, **kwargs) -> bool:
        """Send a message to user"""
        pass
    
    @abstractmethod
    async def request_approval(self, user_id: str, action_summary: str, 
                              action_id: str) -> bool:
        """Request approval for an action from user"""
        pass
    
    # explicitly handle master key
    @abstractmethod
    async def master_key_auth(self) ->None:
        """Authenticate master key"""
        pass
    
    @abstractmethod
    async def receive_messages(self) -> Message:
        """Yield incoming messages (generator)"""
        pass
    
    @abstractmethod
    def get_platform_name(self) -> str:
        """Return platform identifier"""
        pass
        
    @abstractmethod
    async def disconnect(self) -> None:
        """Cleanup connection (optional)"""
        pass



# Every channel have to implement commandhandler
class channelCommandHandler(ABC):
    
    @abstractmethod
    async def extractCommand(self, raw : str):
        pass
    
    @abstractmethod
    async def start(self, auth_key:str = ""):
        pass
        
        
    @abstractmethod
    async def new(self):
        pass
        
        
    @abstractmethod
    async def help(self):
        pass
        
    @abstractmethod
    async def skill(self, skill_name: str = "", action: str = ""):
        pass
    
    @abstractmethod
    async def contact(self, action: str="", contact_data: dict= {}):
        pass