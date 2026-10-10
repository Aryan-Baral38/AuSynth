from dataclasses import dataclass, field 
import json 
from pathlib import Path 

@dataclass
class OSCILLATOR:

    wave_type: str =  "sine"
    enabled: bool  = True 
 
@dataclass 
class Config_class:
    octave : int = 0
    input_device : str = "keyboard"

    osc_1_enabled : bool = True
    osc_2_enabled : bool = False
    osc_1_type : str = "sine"
    osc_2_type: str = "sine"
    osc_1_volume : float = 1 
    osc_2_volume : float = 1 

    attack: float = 0.05 
    sustain_level: float = 1 
    decay : float = 0.01 
    release : float = 0.2

    attack_curve: str = "instant"
    decay_curve : str = "linear"
    release_curve : str = "instant"
    sample_rate : int = 44100

    osc_1 : OSCILLATOR = field(init = False)
    osc_2 : OSCILLATOR = field(init=False)

    def __post_init__(self):
        self.refresh_state()

    def refresh_state(self):
        self.osc_1 = OSCILLATOR(
            wave_type = self.osc_1_type , enabled=self.osc_1_enabled
        )
        self.osc_2 = OSCILLATOR(
            wave_type = self.osc_2_type, enabled=self.osc_2_enabled
        )
    @classmethod 
    def from_json(cls, filepath: str = "config.json"):
        path = Path(filepath)
        if not path.exists():
            print(f"Config file '{filepath}' not found. Generating defaults..")
            default_config = cls()
            default_config.save_to_json(filepath)
            return default_config
        with open(path, "r") as f:
            data = json.load(f)

        valid_fields = {
            f.name for f in cls.__dataclass_fields__.values() if f.init 
        }
        filtered_data = {k: v for k , v in data.items() if k in valid_fields}
        print("Configs loaded")
        return cls(**filtered_data)
    
    def save_to_json(self, filepath: str = "config.json"):
        init_fields = {
            f.name for f in self.__dataclass_fields__.values() if f.init 
        }
        data = {k: getattr(self, k) for k in init_fields}
        with open(filepath, "w") as f:
            json.dump(data, f , indent = 4)
        print(f"Config saved")

conf = Config_class.from_json("config.json")


