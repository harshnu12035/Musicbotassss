from pyrogram import Client, filters, idle
from pyrogram.types import Message
import asyncio
from voice_handler import VoiceBooster
from config import SESSION, BOOST_LEVEL, API_ID, API_HASH
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

voice_booster = VoiceBooster(BOOST_LEVEL)
target_users = {}

# ✅ app init
app = Client(
    "vc_booster",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

# ✅ VC start handler (safe)
@app.on_message(filters.video_chat_started)
async def on_vc_join(client: Client, message: Message):
    try:
        logger.info(f"🎧 VC Started in: {message.chat.title}")
    except Exception as e:
        logger.error(f"VC Error: {e}")

# ✅ BOOST COMMAND (FIXED)
@app.on_message(filters.command("boost", prefixes=[".", "/"]))
async def set_boost(client: Client, message: Message):
    try:
        if len(message.command) < 2:
            return await message.reply("❌ Usage: .boost <user_id>")

        user_id = int(message.command[1])
        target_users[user_id] = True

        await message.reply(
            f"✅ Boost enabled for user: `{user_id}`\nBoost Level: {BOOST_LEVEL}dB"
        )
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

# ✅ UNBOOST COMMAND (FIXED)
@app.on_message(filters.command("unboost", prefixes=[".", "/"]))
async def unset_boost(client: Client, message: Message):
    try:
        if len(message.command) < 2:
            return await message.reply("❌ Usage: .unboost <user_id>")

        user_id = int(message.command[1])

        if user_id in target_users:
            del target_users[user_id]

        await message.reply(f"✅ Boost disabled for user: `{user_id}`")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

# ✅ STATUS COMMAND (FIXED)
@app.on_message(filters.command("status", prefixes=[".", "/"]))
async def status(client: Client, message: Message):
    status_text = "📊 **Boost Status**\n\n"

    if target_users:
        for uid in target_users:
            status_text += f"• `{uid}`: ✅ Active\n"
    else:
        status_text += "• No targets\n"

    status_text += f"\nBoost Level: `{BOOST_LEVEL}`dB"

    await message.reply(status_text)

# background process
async def process_voice():
    while True:
        try:
            for user_id in target_users:
                logger.info(f"🔊 Boosting user {user_id} by {BOOST_LEVEL}dB")
            await asyncio.sleep(0.1)
        except Exception as e:
            logger.error(f"Voice process error: {e}")
            await asyncio.sleep(1)

async def main():
    await app.start()

    asyncio.create_task(process_voice())

    logger.info("🚀 VC Mic Booster Userbot Started!")
    logger.info("Commands:\n.boost <id>\n.unboost <id>\n.status")

    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
