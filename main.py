import numpy as np 
import sounddevice as sd 
import customtkinter as ctk 
import os 
import time
from event import event_handler
from synth_config import config
from voices import voices 


note_frequencies = {
    "C0": 16.35, "C#0": 17.32, "D0": 18.35,
    "D#0": 19.45, "E0": 20.60, "F0": 21.83,
    "F#0": 23.12, "G0": 24.50, "G#0": 25.96,
    "A0": 27.50, "A#0": 29.14, "B0": 30.87,
}


def midi_note_converter(key_no, octave):
    return 12 + (key_no) * octave


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
        self.bind("<KeyPress>", self.key_pressed)
        self.bind("<KeyRelease>", self.key_released)
    
    def key_pressed(self, press):
        event_handler("keyPress", press)

    def key_released(self, release):
        event_handler("KeyRelease", release)


    def play_sound(self):
        # Generates waveform and streams non-blocking audio on click
        sound = generate_wave(440, 1, oscillator={"type": "sine"})
        # sd.play runs in a background thread by default so the GUI stays responsive
        sd.play(sound, samplerate=44100)

def main():
    app = App()
    
    app.mainloop()

if __name__ == "__main__":
    main()
