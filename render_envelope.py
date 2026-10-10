from synth_config import config
import numpy as np
rendered_attack_envelope = []
rendered_decay_envelope = []
rendered_release_envelope = []

def render_attack_envelope():
    t = np.linspace(0, config.attack, int(config.sample_rate * config.attack), False)
    wave = t
    match config.attack_curve:
        case "instant":
            wave = 0 * t 
    rendered_attack_envelope = wave 

def render_decay_envelope():
    print("rendering decay")
    t = np.linspace(0, config.decay , int (config.sample_rate * config.decay), False)
    wave = t
    match config.decay_curve:
        case "linear":
            wave = (config.sustain_level - 1) / config.decay * t + 1
    rendered_decay_envelope = wave

def render_release_envelope():
    t = np.linspace(1, config.release, int(config.sample_rate * config.release), False)
    wave = t 
    match config.release_curve:
        case "instant":
            wave = 0 * t 

    rendered_release_envelope = wave 

def render_adr_envelope():
    render_attack_envelope()
    render_release_envelope()
    render_decay_envelope()

