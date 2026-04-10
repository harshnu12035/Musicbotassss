from pyrogram import filters
from pyrogram.types import Message
from vc_handler import app, start_client, join_vc, leave_vc
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ START VC SYSTEM
@app.on_message(filters.command("startvc", prefixes=[".", "/"]) & filters.me)
async def startvc(_, message: Message):
    try:
        await start_client()
        await message.reply("✅ VC System Started")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

# ✅ JOIN VC
@app.on_message(filters.command("join", prefixes=[".", "/"]) & filters.me)
async def join(_, message: Message):
    try:
        await join_vc(message.chat.id)
        await message.reply("🎧 Joined Voice Chat")
    except Exception as e:
        await message.reply(f"❌ Join Error: {e}")

# ✅ LEAVE VC
@app.on_message(filters.command("leave", prefixes=[".", "/"]) & filters.me)
async def leave(_, message: Message):
    try:
        await leave_vc(message.chat.id)
        await message.reply("❌ Left Voice Chat")
    except Exception as e:
        await message.reply(f"❌ Leave Error: {e}")

# ✅ STATUS COMMAND
@app.on_message(filters.command("status", prefixes=[".", "/"]) & filters.me)
async def status(_, message: Message):
    await message.reply(
        "📊 **VC Bot Status**\n\n"
        "• System: ✅ Running\n"
        "• Mode: 🎧 Audio Playback\n"
        "• Engine: PyTgCalls"
    )

print("🚀 VC Userbot Running...")
app.run()