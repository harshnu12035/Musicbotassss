import numpy as np
from pydub import AudioSegment
from pydub.effects import normalize
import io
import asyncio
from pyrogram.types import Message

class VoiceBooster:
    def __init__(self, boost_level=180):
        self.boost_level = boost_level
    
    async def boost_audio(self, audio_data, user_id):
        """Real-time audio boost for specific user"""
        try:
            # Convert to pydub AudioSegment
            audio = AudioSegment.from_file(io.BytesIO(audio_data))
            
            # Apply boost only for target user
            if user_id:
                # Amplify by boost level (dB)
                boosted = audio + self.boost_level
                
                # Normalize to prevent clipping
                boosted = normalize(boosted)
                
                # Convert back to bytes
                output = io.BytesIO()
                boosted.export(output, format="ogg", codec="libopus")
                output.seek(0)
                return output.getvalue()
            
            return audio_data  # No boost for others
        
        except Exception as e:
            print(f"❌ Boost error: {e}")
            return audio_data
