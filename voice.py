from main import conf, voices
import time

class Voice:
    def __init__(self,note_freq, start_time, duration, conf):
        self.note_freq = note_freq
        self.start_time = start_time
        self.duration = duration

    def generate(self):

        wave = generate_wave()
        

