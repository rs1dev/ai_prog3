
import random

def rollDice(count, sides):
    total = 0
    rolls = random.choices(range(1, sides + 1), k=count)
    for roll in rolls:
        total += roll
    return total

