
import numpy as np

from chooseDice import *
from rollDice import *
from choosefromDistribution import *

def PlayGame(NDice, NSides, LTarget, UTarget, LoseCount, WinCount, M):
    p1_score = 0
    p2_score = 0

    p1_prev = []
    p2_prev = []

    while checkWin(p1_score, p2_score, LTarget, UTarget) == "no winner":
        # player 1
        if checkWin(p2_score, p1_score, LTarget, UTarget) == "no winner":
            dice_prob = chooseDice([p1_score, p2_score], LoseCount, WinCount, NDice, M)
            dice_roll = chooseFromDistribution(range(NDice+1), dice_prob)
            roll_total = rollDice(dice_roll[0], NSides)
            p1_prev.append((p1_score, p2_score, dice_roll))
            p1_score += roll_total

        if checkWin(p1_score, p2_score, LTarget, UTarget) == "no winner":
            dice_prob = chooseDice([p2_score, p1_score], LoseCount, WinCount, NDice, M)
            dice_roll = chooseFromDistribution(range(NDice+1), dice_prob)
            roll_total = rollDice(dice_roll[0], NSides)
            p2_prev.append((p2_score, p1_score, dice_roll))
            p2_score += roll_total

    if checkWin(p1_score, p2_score, LTarget, UTarget) == "player2 wins":
        for p2, p1, rolls in p2_prev:
            WinCount[p2,p1,rolls] += 1
        for p1, p2, rolls in p1_prev:
            LoseCount[p1,p2,rolls] += 1
    else:
        for p1, p2, rolls in p1_prev:
            WinCount[p1,p2,rolls] += 1
        for p2, p1, rolls in p2_prev:
            LoseCount[p2,p1,rolls] += 1
    
    return checkWin(p1_score, p2_score, LTarget, UTarget)

def checkWin(p1, p2, LTarget, UTarget):
    if LTarget <= p1 <= UTarget:
        return "player1 wins"
    if LTarget <= p2 <= UTarget:
        return "player2 wins"
    if p1 > UTarget:
        return "player2 wins"
    if p2 > UTarget:
        return "player1 wins"
    return "no winner"
