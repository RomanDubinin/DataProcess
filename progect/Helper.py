import random
import math
from Vector import Vector

def get_random_vector(min_len, max_len):
    length = random.randint(min_len, max_len)
    angle  = random.random() * math.pi * 2

    return Vector(length * math.cos(angle), length * math.sin(angle))
