from typing import Dict, Any, Optional
from dataclasses import dataclass
from config.baseconfig import bot_config

@dataclass
class Message:
    user_id: str
    text: str
    platform: str
    media: Optional[str] = None
    command: Optional[str] = None  
    raw_command: Optional[str] = None 
    message_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class MessageHandler:
    def __init__(self, message: Message):
        self.message = message


    async def is_command(self) -> bool:
        if not self.message.text.startswith(f"{bot_config.COMMAND_PREFIX}{bot_config.PREFIX_SEPARATOR}"):
            return False
        return True
    
    async def parse_command(self) -> Optional[str]:
        if not await self.is_command():
            return None
        command = self.message.text.split(f"{bot_config.COMMAND_PREFIX}{bot_config.PREFIX_SEPARATOR}")[1]
        return command
    
    async def parse_command_args(self) -> Optional[str]:
        if not await self.is_command():
            return None
        args = self.message.text.split(f"{bot_config.COMMAND_PREFIX}{bot_config.PREFIX_SEPARATOR}")[2:]
        return " ".join(args)
    



