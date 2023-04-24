
from extractAnswer import *
from chooseDice import *
from playGame import *
import numpy as np
import sys

def main(NDice, NSides, LTarget, UTarget, M, n):

    WinCount = np.zeros([LTarget, LTarget, NDice+1])
    LoseCount = np.zeros([LTarget, LTarget, NDice+1])

    for i in range(n):
        PlayGame(NDice, NSides, LTarget, UTarget, LoseCount, WinCount, M)

    answer = (extractAnswer(WinCount, LoseCount))
    p_win = np.zeros([LTarget, LTarget])

    for x in range(LTarget):
        for y in range(LTarget):
            correct_dice = int(answer[x][y])
            if (WinCount[x][y][correct_dice] + LoseCount[x][y][correct_dice]) == 0:
                p_win[x][y] = 0
            else:
                p_win[x][y] = WinCount[x][y][correct_dice] / (WinCount[x][y][correct_dice] + LoseCount[x][y][correct_dice])
    
    print(answer)
    print(p_win)

if __name__ == "__main__":
    input = sys.argv

    if len(input) == 5:
        print("Defaulting to M = 100 and 100000 training runs")
        main(int(input[1]), int(input[2]), int(input[3]), int(input[4]), 100, 100000)

    if len(input) == 6:
        print("Defaulting to 100000 training runs")
        main(int(input[1]), int(input[2]), int(input[3]), int(input[4]), int(input[5]), 100000)

    if len(input) == 7:
        main(int(input[1]), int(input[2]), int(input[3]), int(input[4]), int(input[5]), int(input[6]))

    if len(input) not in [5,6,7]:
        print("incorrect number of arguments")
