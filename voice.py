import time
from synth_config import config


class Voice:
    def __init__(self, note_freq: float, start_time: float, duration: float = 1):
        self.note_freq = note_freq
        self.start_time = start_time if start_time is not None else time.perf_counter()
        self.duration = duration
        self.playing = False

    def __repr__(self):
        return f"Voice, freq: {self.note_freq}, start time : {self.start_time}"

    def __str__(self):
        return f"Voice, freq: {self.note_freq}"
