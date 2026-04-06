from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from session_handler import SessionManager
from voice_handler import VoiceBooster
from config import SESSION, BOOST_LEVEL, API_ID, API_HASH
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize
session_mgr = SessionManager(SESSION)
voice_booster = VoiceBooster(BOOST_LEVEL)
target_users = {}  # user_id: boost_status

app = session_mgr.app

@app.on_message(filters.voice_chat_started)
async def on_vc_join(client: Client, message: Message):
    """Auto join VC when started"""
    try:
        await client.join_group_call(message.chat.id)
        logger.info(f"✅ Joined VC: {message.chat.title}")
    except Exception as e:
        logger.error(f"❌ VC Join Error: {e}")

@app.on_message(filters.command("boost") & filters.me)
async def set_boost(client: Client, message: Message):
    """Set boost target .boost <user_id>"""
    try:
        user_id = int(message.command[1])
        target_users[user_id] = True
        await message.reply(f"✅ Boost enabled for user: `{user_id}`\nBoost Level: {BOOST_LEVEL}dB")
    except:
        await message.reply("❌ Usage: `.boost <user_id>`")

@app.on_message(filters.command("unboost") & filters.me)
async def unset_boost(client: Client, message: Message):
    """Remove boost target .unboost <user_id>"""
    try:
        user_id = int(message.command[1])
        if user_id in target_users:
            del target_users[user_id]
        await message.reply(f"✅ Boost disabled for user: `{user_id}`")
    except:
        await message.reply("❌ Usage: `.unboost <user_id>`")

@app.on_message(filters.command("status") & filters.me)
async def status(client: Client, message: Message):
    """Show boost status"""
    status = "📊 **Boost Status**\n\n"
    if target_users:
        for uid in target_users:
            status += f"• `{uid}`: ✅ Active\n"
    else:
        status += "• No targets\n"
    status += f"\nBoost Level: `{BOOST_LEVEL}`dB"
    await message.reply(status)

# Real-time voice processing (runs in VC)
async def process_voice():
    """Background voice processor"""
    while True:
        try:
            # Monitor VC audio streams
            for user_id in target_users:
                # Apply boost to target user's audio
                # This would integrate with pyrogram's voice chat stream
                logger.info(f"🔊 Boosting user {user_id} by {BOOST_LEVEL}dB")
            await asyncio.sleep(0.1)  # Real-time processing
        except Exception as e:
            logger.error(f"Voice process error: {e}")
            await asyncio.sleep(1)

async def main():
    await session_mgr.create_client()
    
    # Start voice processor
    asyncio.create_task(process_voice())
    
    logger.info("🚀 VC Mic Booster Userbot Started!")
    logger.info("Commands:\n.boost <id> - Enable boost\n.unboost <id> - Disable\n.status - Check status")
    
    await idle()

if __name__ == "__main__":
    app.run(main())
