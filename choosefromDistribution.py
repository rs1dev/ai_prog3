import random

# refer to 'Sampling from a given distribution' section in background.md

def chooseFromDistribution(p, weights):
    return (random.choices(p, weights = weights))