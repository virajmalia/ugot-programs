import time
from ugot import ugot

bot = ugot.UGOT()
bot.initialize('127.0.0.1') # Replace with your robot's IP address

ACTIVATION_PHRASE = "Hey Jarvis"
ROBOT_GREETING = "Hi! What's up?"
VOICE_TYPE = 0  # 0:female, 1:male

# Infinite loop, runs until stopped manually
while True:
    audio=""    # reset audio data
    audio = bot.start_audio_asr()   # start mic, get input
    if audio.lower().find(ACTIVATION_PHRASE.lower()) != -1: # check activation
        # send greeting
        bot.play_audio_tts(ROBOT_GREETING, wait=True, voice_type=VOICE_TYPE)
        time.sleep(0.5) # wait for greeting. Use longer time for longer greeting
        for _ in range(0, 50):  # Run 50 times
            query = bot.start_audio_asr()   # get first chat input
            bot.start_audio_nlp(query, wait=True)   # reply from AI
    time.sleep(0.5) # Wait for everything to be processed, reset and ready for the next loop
