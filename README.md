# StarBattlePuzzles
The rules and demo playing can be found on: https://www.puzzle-star-battle.com
## Solving Strategy
![Star Battle Sample Map](Images/SampleMap.png)

Consider a $5\times 5$ Star Battle Map as above. Let $T[i][j] = 0$ if there are no star in cell corresponding to row $(i + 1)$ and column $(j + 1)$, and $T[i][j]=1$ otherwise. We analyse the restricting equations from the game rules:

* **2 stars cannot be adjacent horizontally, vertically or diagonally.**
