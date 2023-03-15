import gurobipy as gp
from gurobipy import GRB
import numpy as np
import sys
import os

def get_board():
    n, s = map(int, input("Enter the size (also the length and width) and the number of stars in one region: ").split())
    board = []
    for i in range(n):
        region = []
        ncell = int(input("Enter the number of cells in region: "))
        print(".......")
        print("Now it comes to enter the coordinates of cells")
        
        for j in range(ncell):
            x, y = map(int, input("Enter the x- and y-coordinate of the cell: ").split())
            region.append([x, y])
            if (j != ncell - 1):
                print("Next cell")
        
        board.append(region)

    return n, s, board

model = gp.Model('StarBattle')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
sys.stdin = open("./GameBoard/Sample.txt", "r")
n, s, K = get_board()
#print(n, K)

T = model.addMVar(shape = (n, n), lb = 0, ub = 1, vtype = GRB.INTEGER, name = "fool" )

#sum of numbers in each rows must be s
for i in range(n):
    constraint = 0
    for j in range(n):
        constraint += T[i][j]
    model.addConstr(constraint == s)

#sum of numbers in each columns must be s
for i in range(n):
    constraint = 0
    for j in range(n):
        constraint += T[j][i]
    model.addConstr(constraint == s)
#sum of numbers in the adjacent cells <= 1

for i in range(n-1):
    for j in range(n-1):
        model.addConstr(T[i][j]+T[i][j+1]+T[i+1][j]+T[i+1][j+1] <= 1)
        
#sum of numbers in a region

for i in range(n):
    constraint = 0
    for j in range(len(K[i])):
        constraint += T[K[i][j][0]][K[i][j][1]]
    model.addConstr(constraint == s)
        
        
model.setObjective(T[0][0], sense = GRB.MAXIMIZE)

model.optimize()
print('-' * 50)
if model.status == GRB.OPTIMAL:
    print('The status meaning is OPTIMAL')
print(f'model status: {model.status}')
print(f'model runtime: {model.runtime}')

values = model.getAttr("X", model.getVars())
#for i in range(n**2):
#    if i % (n-1) == 0 and i != 0:
#        print(values[i])
#    print(values[i], end = " ")
for k in range (4 * n + 1):
    print("-", end = "")
print("")
for i in range(n):
    print("|", end = "")
    for j in range(n):
        if (int(values[i * n + j]) == 1):
            print(" * ", end = "|")
        else:
            print("   ", end = "|")
    print("")
    for k in range (4 * n + 1):
        print("-", end = "")
    print("")

#print(values)