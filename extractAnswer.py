import numpy as np

def extractAnswer(WinCount, LoseCount):
    m = len(WinCount)
    n_d = len(WinCount[0][0])
    res = np.zeros([len(WinCount), len(WinCount)])

    for x in range(m):
        for y in range(m):
            p_J = np.zeros(n_d)
            for j in range(n_d):
                if WinCount[x][y][j] + LoseCount[x][y][j] > 0:
                    p_J[j] = WinCount[x][y][j] / (WinCount[x][y][j] + LoseCount[x][y][j])
                else:
                    p_J[j] = 0

            for j in range(n_d):
                if p_J[j] == max(p_J):
                    res[x][y] = j
    return res

