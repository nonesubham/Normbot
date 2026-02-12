import argparse
from interfaces.channels import BaseChannel, channelCommandHandler
from data.base_message import Message


class ChannelTerminal(BaseChannel, channelCommandHandler):
    """Terminal messaging interface"""
    
    def __init__(self, args: argparse.Namespace):
        self.args = args
        
    async def send_message(self, user_id: str, message: Message, **kwargs) -> bool:
        print(message.text)
        return True
        
    async def request_approval(self, user_id: str, action_summary: str, 
                                  action_id: str) -> bool:
        print(f"Approve {action_summary}?\nThis action will call {action_id} (y/n)")
        response = input().lower()
        while response not in ["y", "n"]:
            print("Invalid input. Please enter 'y' or 'n'.")
            response = input().lower()
        return response == "y"
        
        
    async def master_key_auth(self) -> None:
        key = self.passhandler("Enter master key:")
        if key == self.args.master_key:
            print("Authenticated")
        else:
            print("Invalid key")
        
    async def receive_messages(self) -> Message:
        print("Enter message:")
        text = input()
        return Message(platform="terminal", user_id="1", text=text)
        
    async def disconnect(self) -> None:
        pass
        
    def passhandler(self, message: str) -> str:
        print(message)
        usr_rsp = input()
        # clear once the key is captured
        print("\033[2K\r", end="")
        return usr_rsp
    
    async def command_handler(self, command: str, args: list[str]) -> None:
        if command == "help":
            print("Available commands:")
            print("help - display this help message")
            print("exit - exit the terminal")
        elif command == "exit":
            await self.disconnect()
        else:
            print(f"Unknown command: {command}")
        