import numpy as np 
import sounddevice as sd 
import customtkinter as ctk 
import os 
import time 
import 

NOTE_FREQUENCIES = {
    "C3": 130.81, "C#3": 138.59, "D3": 146.83, "D#3": 155.56, "E3": 164.81,
    "F3": 174.61, "F#3": 185.00, "G3": 196.00, "G#3": 207.65, "A3": 220.00,
    "A#3": 233.08, "B3": 246.94,

    "C4": 261.63, "C#4": 277.18, "D4": 293.66, "D#4": 311.13, "E4": 329.63,
    "F4": 349.23, "F#4": 369.99, "G4": 392.00, "G#4": 415.30, "A4": 440.00,
    "A#4": 466.16, "B4": 493.88,

    "C5": 523.25, "C#5": 554.37, "D5": 587.33, "D#5": 622.25, "E5": 659.25,
    "F5": 698.46, "F#5": 739.99, "G5": 783.99, "G#5": 830.61, "A5": 880.00,
    "A#5": 932.33, "B5": 987.77,
}


voices = {} # {"note": voice_obj}

class Config_class:
    def __init__(self, 
                 extra_buffer_duration = 0, #sec,  create extra buffer 
                
                 osc_1_enabled = True, 
                 osc_2_enabled = False,
                 
                 osc_1_volume = 1,
                 osc_2_volume = 1,
                
                 attack = 0.05,
                 sustain_level = 1,
                 decay = 0.01,
                 release = 0.2,

                 attack_curve = "instant",
                 sustain_level = 1,
                 decay_curve = "linear",
                 release_curve = "instant",

                 sample_rate = 44100
                 ):

        self.decay = decay
        self.attack = attack
        self.dampening = dampening
        self.buffer_duration = self.dampening + extra_buffer_duration

        self.osc_1_enabled = osc_1_enabled
        self.osc_2_enabled = osc_2_enabled

        self.osc_1_volume = osc_1_volume
        self.osc_2_volume = osc_2_volume

        self.attack_curve = attack_curve
        self.intensity = intensity
        self.dampening_curve = dampening_curve
        self.sample_rate = sample_rate

conf = Conf(osc_2_enabled = True)

class OSCILLATOR:
    def __init__ (self, 
                  type = "sine",
                  enabled = True,
                  active = False,
                  current_note = None,
                  start_play_at = None,
                  end_play_at = None,
                  next_queued_note = None):
        self.type = type
        self.enabled = enabled
        self.active = active
        self.current_note = current_note

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Synth App")
        self.geometry("300x200")

        # Trigger play_sound directly when clicked
        self.button = ctk.CTkButton(
            self, text="Play 440Hz Tone", command=self.play_sound
        )
        self.button.pack(padx=20, pady=50)
        self.bind("<KeyPress>", lambda event: print(event))
        self.bind("<KeyRelease>", lambda event: print(event))


    def play_sound(self):
        # Generates waveform and streams non-blocking audio on click
        sound = generate_wave(440, 1, oscillator={"type": "sine"})

        # sd.play runs in a background thread by default so the GUI stays responsive
        sd.play(sound, samplerate=44100)
def main():
    conf = Config_class()
    oscillators = [OSCILLATOR()]
    app = App()
    
    app.mainloop()

main()
    
