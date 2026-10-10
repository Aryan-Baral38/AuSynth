

def rendered_attack_envelope(oscillator, config):
    t = np.linspace(0, config.attack, int(config.sample_rate * config.attack), False)
    wave = t
    match config.attack_curve:
        case "instant":
            wave = 0 * t 
    
    return wave 

def rendered_decay_envelope(oscillator, config):
    t = np.linspace(0, config.decay , int (config.sample_rate * config.decay), False)
    wave = t
    match config.decay_curve:
        case "linear":
            wave = (config.sustian_level - 1) / config.decay * t + 1

def rendered_release_envelope(oscillator, config):
    t = np.linspace(1, config.release, int(config.sample_rate * config.release), False)
    wave = t 
    match config.release_cyrve:
        case "instant":
            wave = 0 * t 

    return wave 
    

