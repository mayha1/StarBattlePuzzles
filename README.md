# StarBattlePuzzles
The rules and demo playing can be found on: https://www.puzzle-star-battle.com
## Solving Strategy
![Star Battle Sample Map](Images/SampleMap.png)

Consider a $5\times 5$ one-star game map as above. Let $T[i][j] = 0$ if there are no star in cell corresponding to row $(i + 1)$ and column $(j + 1)$, and $T[i][j]=1$ otherwise. We analyse the restricting equations from the game rules:

* **2 stars cannot be adjacent horizontally, vertically or diagonally.**

    For two adjacent cells, their $T$-sum must not exceed one. Therefore
    * $T[i][j] + T[i][j + 1] \le 1$ for $i\in[0;4]$ and $j\in[0;3]$ (horizontal adjacency);
    * $T[i][j] + T[i + 1][j] \le 1$ for $i\in[0;3]$ and $j\in[0;4]$ (vertical adjacency);
    * $T[i][j] + T[i + 1][j + 1] \le 1$ and $T[i + 1][j] + T[i][j + 1] \le 1$ for $i\in[0;3]$ and $j\in[0;3]$ (diagonal adjacency).

* **You have to place 1 star on each row, column and shape.**

    * On a row, its $T$-sum must be equal to one. Therefore $\displaystyle\sum_{j=0}^4 T[i][j] = 1$ for $i\in[0;4]$.
    * On a column, its $T$-sum must also be equal to one. Therefore $\displaystyle\sum_{i=0}^4 T[i][j] = 1$ for $j\in[0;4]$.
    * In a shape $S_i$, its $T$-sum must also be equal to one. Therefore $\displaystyle\sum_{(i, j)\in S_x} T[i][j]=1$ for $S_x$ denotes one particular region in the map. For the sample map, there are five shapes $S_1$ (contains the cells $T[0][0]$, $T[0][1]$, $T[0][2]$, $T[1][1]$ and $T[2][1]$), $S_2$, $S_3$, $S_4$ and $S_5$.