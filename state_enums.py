from enum import Enum 


@dataclass
class asdr_state(Enum):
    attack = "attack"
    decay = auto()
    sustain = Curves 
    release = Curves 


@dataclass 
class Attack(Enum):
    none = 0.05
    duration: float 
    duration = duration if  duration >= 0.05 else 0.05

    def __float__(self):
        return float(self.value)

class Decay(Enum):
    duration = 0.05
    duration = duration if  duration >= 0.05 else 0.05



@dataclass
class Curves(Enum):
    none = [0.1]
    linear = [0.5, 0, 1]
    exponential = [0.01, 1, 0.3] # [starting_value, max_intensity, curve_duration]



@dataclass
class Attack_curve(Enum):
    none : Curves = Curves.none #attak delay 
    linear: Curves = Curves.linear #(duration, starting_intensity, max_intensity)
    exponential = Curves.exponential
