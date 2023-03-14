import gurobipy as gp
from gurobipy import GRB
import numpy as np


def get_board():
    n = int(input("Enter the size (also the region): "))
    board = [0]*n
    for i in range(n):
        board[i] = []
        t = int(input("Enter the number of cells in region: "))
        print(".......")
        print("Now it comes to enter the coordinates of cells")
        
        for j in range(t):
            t = []
            x = int(input("Enter the x-coordinate of the cell: "))
            t.append(x)
            y = int(input("Enter the y-coordinate of the cell: "))
            t.append(y)
            board[i].append(t)
            print("Next cell")
        
    return n, board

model = gp.Model('StarBattle')

n, K = get_board()
print(n, K)


T = model.addMVar(shape = (n, n), lb = 0, ub = 1, vtype = GRB.INTEGER, name = "fool" )

#sum of numbers in each rows must be 1
for i in range(n):
    constraint = 0
    for j in range(n):
        constraint += T[i][j]
    model.addConstr(constraint == 1)

#sum of numbers in each columns must be 1
for i in range(n):
    constraint = 0
    for j in range(n):
        constraint += T[j][i]
    model.addConstr(constraint == 1)
#sum of numbers in the adjacent cells <= 1

for i in range(n-1):
    for j in range(n-1):
        model.addConstr(T[i][j]+T[i][j+1]+T[i+1][j]+T[i+1][j+1] <= 1)
        
#sum of numbers in a region

for i in range(n):
    constraint = 0
    for j in range(len(K[i])):
        constraint += T[K[i][j][0]][K[i][j][1]]
    model.addConstr(constraint == 1)
        
        
model.setObjective(T[0][0], sense = GRB.MAXIMIZE)

model.optimize()
print('-' * 50)
if model.status == GRB.OPTIMAL:
    print('The status meaning is OPTIMAL')
print(f'model status: {model.status}')
print(f'model runtime: {model.runtime}')

values = model.getAttr("X", model.getVars())
#for i in range(n**2):
    #if i % (n-1) == 0 and i != 0:
        #print(values[i])
    #print(values[i], end = " ")
    
print(values)
    
    
        




            
        