"""
Task 3.3: https://stepik.org/lesson/862118/step/3?unit=866155
The \texttt{Rocks}Rocks algorithm determines if Player 1 wins or loses. If Player 1 wins in an n +mn+m game,
\texttt{Rocks}Rocks returns WW. If Player 1 loses, \texttt{Rocks}Rocks returns LL. We introduced an artificial
initial condition, R(0,0) = LR(0,0)=L to simplify the pseudocode.

Rocks(nn, mm):
     LR(0,0)←L
     for i from 1 to n:
        if R(i−1,0)=W:
          R(i,0)←L
        else:
          R(i,0)←W
     for j from 1 to m:
        if R(0,j−1)=W:
          R(0,j)←L
        else:
          R(0,j)←W
     for i from 1 to n:
        for j from 1 to mm:
          if R(i−1,j−1)=W andR(i,j−1)=W and R(i−1,j)=W:
            R(i,j)←L
          else:
            R(i,j)←W
     return R(n,m)


FastRocks(nn, mm):
     if nn and mm are both even:
        return LL
     else:
        return WW
"""

LOSE, WIN = 0, 1


def rocks(n, m):
    r = [[0 for _ in range(m+1)] for _ in range(n+1)]
    r[0][0] = LOSE
    for i in range(1, n + 1):
        if rocks(i - 1, 0) == WIN:
            r[i][0] = LOSE
        else:
            r[i][0] = WIN
    for j in range(1, m + 1):
        if rocks(0, j - 1) == WIN:
            r[0][j] = LOSE
        else:
            r[0][j] = WIN
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if r[i - 1][j - 1] == W and r[i][j - 1] == WIN and r[i - 1][j] == WIN:
                r[i][j] = LOSE
            else:
                r[i][j] = WIN
    return r[n][m]


