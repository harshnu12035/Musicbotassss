from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pyrogram import Client
from config import API_ID, API_HASH, SESSION

app = Client(
    "vc_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

call = PyTgCalls(app)


async def start_client():
    await app.start()
    await call.start()
    print("✅ Client Started")


async def join_vc(chat_id):
    try:
        await call.join_group_call(
            chat_id,
            AudioPiped(
                "input.raw",  # ⚠️ same folder me hona chahiye
                bitrate=48000
            )
        )
        print("🎧 VC Joined")
    except Exception as e:
        print("❌ Join Error:", e)


async def leave_vc(chat_id):
    try:
        await call.leave_group_call(chat_id)
        print("❌ VC Left")
    except Exception as e:
        print("❌ Leave Error:", e)