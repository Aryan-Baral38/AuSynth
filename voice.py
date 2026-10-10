import time
from synth_config import config

class Voice:
    def __init__(self,note_freq, start_time, duration):
        self.note_freq = note_freq
        self.start_time = start_time
        self.duration = duration

    def __repr__(self):
        return f"Voice, freq: {self.note_freq}"
    def __str__(self):
        return f"Voice, freq: {self.note_freq}"


