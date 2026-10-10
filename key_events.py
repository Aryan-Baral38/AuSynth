import numpy as np
import sounddevice as sd
from generate_wave import generate_wave
pressed = {}


char_to_note = {
    "a" : "C", "w" : "C#", "s" : "D",
    "e" : "D#" , "d" : "E", "f" : "F",
    "t" : "F#" , "g" : "G", "y" : "G#",
    "h" : "A", "u" : "A#", "j" : "B",
}
def key_pressed(data):
    if not data.char in pressed or pressed[data.char] == "not":
        char = data.char 
        pressed[char] = char
        print(char)
        print(char_to_note[char], "played")
        #wave = generate_wave()
   

def key_released(data):
    pressed[data.char] = "not"
    print(data.char, "released")
   

