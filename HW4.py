import pygame
import random

MIN = 0
MAX = 30


class Gene:
    def __init__(self, value):
        self.value = random.randrange(MIN, MAX)
        self.min = MIN
        self.max = random.randrange(4, 8)
        self.mutationProbability = random.randrange(MIN, 10)
        self.mutationRange = random.randrange(MIN, 15)
        self.isReturnInteger = isinstance(value, int)
