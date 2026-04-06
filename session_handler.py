from pyrogram import Client
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SessionManager:
    def __init__(self, session_string):
        self.session_string = session_string
        self.app = None
    
    async def create_client(self):
        self.app = Client(
            "vc_booster",
            session_string=self.session_string,
            in_memory=True
        )
        await self.app.start()
        logger.info("✅ Userbot session started!")
        return self.app
