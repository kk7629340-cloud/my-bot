import asyncio
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata
from highrise.__main__ import main

class MyBot(BaseBot):
    def __init__(self):
        super().__init__()
        # المعلومات تاعك راهي هنا
        self.room_id = "68bb81b6b3ad4d2c8d06e70d"
        self.api_token = "a7bc6b92e7aab123e5a044d7ce4d252671ae12cf7554a58fe4c1012a882d8d4f"

    async def on_user_join(self, user: User, position: Position) -> None:
        await self.highrise.chat(f"مرحبا بيك يا {user.username} نورت الروم! ✨")

if __name__ == "__main__":
    # استعملنا دالة main الصحيحة هنا
    main(MyBot(), "68bb81b6b3ad4d2c8d06e70d", "a7bc6b92e7aab123e5a044d7ce4d252671ae12cf7554a58fe4c1012a882d8d4f")


    
