from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pyrogram import Client
from config import SESSION, API_ID, API_HASH, BOOST_LEVEL
import asyncio

app = Client(
    "vc_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

call_py = PyTgCalls(app)


async def start_vc():
    await app.start()
    await call_py.start()
    print("✅ VC Client Started")


async def join_vc(chat_id, file="input.raw"):
    try:
        await call_py.join_group_call(
            chat_id,
            AudioPiped(
                file,
                bitrate=48000
            )
        )
        print("🎧 Joined VC")
    except Exception as e:
        print(f"❌ Join Error: {e}")


async def leave_vc(chat_id):
    try:
        await call_py.leave_group_call(chat_id)
        print("❌ Left VC")
    except Exception as e:
        print(f"Error: {e}")