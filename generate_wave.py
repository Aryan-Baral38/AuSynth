from synth_config import config

def generate_wave(note_freq, duration):
    t= np.linspace(0, duration, int(config.sample_rate * duration), False)
    wave = []
    match oscillator["type"]:
        case "sine":
            wave =  np.sin(2 * np.pi * note_freq * t)
        case "square":
            wave = np.sign(np.sin(2*np.pi * note_freq * t))
        case "sawtooth":
            wave = 2 * (t* note_freq - np.floor(0.5 + t* note_freq)) 
        case "triangle":
            wave = 2 * np.abs(2 * (t * note_freq - np.floor(0.5 + t* note_freq))) - 1 
        case _ :
            raise ValueError("Unsupported wave type")
    return wave


