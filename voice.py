import time
from config import config

class Voice:
    def __init__(self,note_freq, start_time, duration):
        self.note_freq = note_freq
        self.start_time = start_time
        self.duration = duration

    def generate(self):

        wave = generate_wave()
        

