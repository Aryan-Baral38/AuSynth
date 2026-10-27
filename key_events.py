from ctypes import string_at

import numpy as np
from generate_wave import generate_wave
from voice import Voice
from voices import voices
import time


char_to_note = {
    "a": "C",
    "w": "C#",
    "s": "D",
    "e": "D#",
    "d": "E",
    "f": "F",
    "t": "F#",
    "g": "G",
    "y": "G#",
    "h": "A",
    "u": "A#",
    "j": "B",
}
frame_index = 0


def key_pressed(data):
    if not data.char in char_to_note:
        return
    note = char_to_note[data.char]
    if not note in voices:
        voices[note] = Voice(note_freq=440, duration=1, start_time=time.perf_counter())
        print(voices)


def key_released(data):
    if not data.char in char_to_note:
        return
    note = char_to_note[data.char]
    del voices[note]
    print(voices)
