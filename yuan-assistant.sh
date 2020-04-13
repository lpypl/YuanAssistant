#! /usr/bin/bash
cd /home/lpy/Coding/yuan-assistant/
arecord -d 3 -r 16000 -c 1 -f S16_LE /home/lpy/Coding/yuan-assistant/audio/voice-record.wav && /usr/bin/python /home/lpy/Coding/yuan-assistant/asr_raw.py