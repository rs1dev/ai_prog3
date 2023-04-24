
# refer to Gameplay section in background.md file for more details on this program

def chooseDice(Score, LoseCount, WinCount, NDice, M):
    X = Score[0]
    Y = Score [1]
    K = NDice

    f_j = [0] * (K+1)
    for j in range(1, K+1): 
        if WinCount[X][Y][j] + LoseCount[X][Y][j] == 0: 
            f_j[j] = 0.5 
        else: 
            f_j[j] = WinCount[X][Y][j] / (WinCount[X][Y][j] + LoseCount[X][Y][j]) 
    
    # breaking ties 
    B = -1 
    for j in range(len(f_j)): 
        if f_j[j] == max(f_j): 
            B = j 
    
    g = 0 
    for j in range(len(f_j)):
        if j != B:
            g += f_j[j]

    T = 0
    for j in range(K+1):
        T += (WinCount[X][Y][j] + LoseCount[X][Y][j])

    p_B = (T * f_j[B] + M) / ((T * f_j[B]) + (K*M))


    # For J != B, the player rolls J dice with probability... 
    p_J = [0] * (K+1)
    p_J[B] = p_B

    for i in range(1, K+1):
        if i != B:
            p_J[i] = ((1-p_B) * ((T * f_j[i]) + M)) / ((g*T) + (K-1) * M)

    return p_J
