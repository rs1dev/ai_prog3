# ai prog 3 

## Program that learns to play a simple game {Blackjack} of chance (like AlphaZero)

### Blackjack Rules: 
- 2 players alternately roll dice and keep track of their total across turns
- each trying to reach sum in a specified target (fixed low - high value)
- if player reaches a score in target range, they win; if exceed high value, they lose 
- players can choose the number of dice to roll on each turn (1 - fixed max)

## Blackjack Parameters (4)
- NSides: number of sides of die (1 to NSides), equiprobable 
- LTarget: lowest winning value 
- UTarget: highest winning value 
- NDice: max num dice player can roll 

## Learning Algo 
- machine plays a series of games with itself, playing both sides 
- initially both players play randomly 
- as series progresses, they hopefully play better and better 

## Program Specs 
- 2 3-d integer matrices of size LTarget x LTarget x [NDice + 1].
  - WinCount[X,Y,J]
    - value is num. times current player eventually won when state was <X,Y> and current player rolled J dice 
  - LoseCount[X,Y,J]
    - num. times they lost 
  - X = current point count for player abt to play 
  - Y = point count for opponent 
  - J = num dice current player rolls 
- after each game, 2 matrices get updated, reflecting result of game 

## Game Play 
- Suppose current state is <X, Y>
- Let K=NDice
- For J=1...K let f_J = WinCount[X, Y, J]/(WinCount[X,Y,J] + LoseCount[X, Y, J]) ^ f_J = 0.5 if denominator = 0 
- Let B be value of J with highest value of f_J
- Let g = sum over all J that aren't B
- Let T = sum_J=1 ^K WinCount(X, Y, J) + LoseCount(X, Y, J) {the total number of games that have gone thru state <X,Y>}. Let M be a hyperparameter set in the input (controls "explore/exploit" trade-off)
- player rolls B dice with prbltly p_B = (T_fB + M) / (T_fB + KM)
- for J =/ B, player rolls J dice with prblty ...

- Choosing Action: Explore/exploit trade-off 
  - how much effort should you spend exploring all the possibilities vs exploiting actions that've been found successful. 
  - new envt: exploring > 
  - exploring to exploiting speed controlled by hyperparameter M: larger M = longer to change from one regime to another 

## Input/Output 
- input (parameters): int NSides, int LTarget, int UTarget, int NDice, float M, int NGAMES
  - prog3(NSides, LTarget, UTarget, NDice, M, NGames)
- output: 2 LTarget x LTarget arrays; the correct number of dice to roll in state <X,Y> and prblty of winning if you roll the correct number of dice (written above)

## Sampling  from a given distribution 
- u_0 = 0
- for (i=1...k) u_i = u_i-1 + p_i 
- x = rand() # uniform distribution from 0 to 1
- for (i=0...k-1)
  - if x < u_i return i 
- return k 
- use random.choices() function for python https://docs.python.org/3/library/random.html

## Limits on results quality 
- if enough games are played and M is not set too small, then the answers should more or less converge to the true answer. But there are a number of important limitations on that:
  - A/ state where player has prblty 0 always. ex: target range is [10,20], NDice = 2, NSides = 3, player B's turn and is behind 2 to 9, then B has lost...best move is arbitrary 
  - B/ state is mathematically unattainable starting from [0,0]. 
  ex: NDice = 2, NSides = 2, then no way to attain the state ⟨5,0⟩
  - C/ state may be unattainable unless one or both players play really stupidly. 
  ex: target range is [10,20], NSides = 3, NDice = 2, then both players should always roll 2 dice bc can’t overshoot upper bound. State ⟨1,X⟩ for any X is unattainable unless the first player rolls 1 die. Such states will presumably only be achieved in early games in the sequence bc program will learn not to make the stupid moves. Therefore, the probability estimates for these may be extremely far off, and the policy may be wrong.
  - D/ state may be attainable if both players are playing optimally but very unlikely.
  ex: NSides=4, NDice=10, then state [0,40] is possible if first player rolls ten 4s, only occurs in 1/1M games, so take an enormous number of plays to build up reliable statistics. Again, with reasonable number of games played, the computed probability may be far off and the policy may be wrong.
  - E/ if probabilities for success for two different actions in a given state are close, then it is quite possible that the recommended action will be not the truly optimal one.
- *SOOO, for states which will occur reasonably frequently if both players play reasonably well, the probability matrix should be fairly accurate, and if the best move is significantly better than the alternatives, then the policy matrix should recommend it.*


