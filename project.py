import numpy as np 
import sounddevice as sd 
import customtkinter as ctk 
import os 
import time 

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

decay = 0 #loses fraction of volume for every second of key held
attack = 0 # sec, this long to reach full volume 
dampening = 0 # sec, this long after key is released to  reach 0 volume 
extra_buffer_duration = 1 #sec,  create extra buffer 
osc_1_enabled = True
osc_2_enabled = False
osc_1_attack_curve = "None"
osc_1_dampening_curve = "None"
osc_2_attack_curve = "None"
osc_2_dampening_curve = "None"
pluck = True
sample_rate = 44100

voices = []

class Config:
    def __init__(self, 
                 decay = 0, #loses fraction of volume for every second of keypress
                 attack = 0, # sec, this long to reach full volume 
                 dampening = 0, # sec, this long after key press is over ot reach 0 volume 
                 extra_buffer_duration = 1, #sec,  create extra buffer 

                 osc_1_enabled = True, 
                 osc_2_enabled = False,

                 attack_curve : "None", 
                 dampening_curve : "None",
                 sample_rate = 44100
                 ):

        self.decay = decay
        self.attack = attack
        self.dampening = dampening
        self.buffer_duration = self.dampening + extra_buffer_duration
        self.osc_1_enabled = osc_1_enabled
        self.osc_2_enabled = osc_2_enabled
        self.attack_curve = attack_curve
        self.dampening_curve = dampening_curve
        self.sample_rate = sample_rate
Config conf

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
        self.start_play_at = start_play_at
        self.end_play_at = end_play_at
        self.next_queued_note = next_queued_note

class Voice:
    def __init__(self, ):

def generate_wave(note_freq, oscillator, octaves = False, conf):
    samples = np.linspace(0, buffer_duration, int(sample_rate * buffer_duration), False)
    wave = np.zeros(conf.buffer_duration)
    match oscillator["type"]:
        case "sine":
            wave =  np.sin(2 * np.pi * note_freq * samples)
        case "square":
            wave = np.sign(np.sin(2*np.pi * note_freq * samples))
        case "sawtooth":
            wave = 2 * (samples * note_freq - np.floor(0.5 + samples * note_freq)) 
        case "triangle":
            wave = 2 * np.abs(2 * (samples * note_freq - np.floor(0.5 + samples * note_freq))) - 1 
        case _ :
            raise ValueError("Unsupported wave type")
    return wave

def main():

