import gurobipy as gp
from gurobipy import GRB
import numpy as np
import sys
import os
import json

"""def get_board():
    size_of_board, num_stars_reg = map(int, input("Enter the size (also the length and width) and the number of stars in one region: ").split())
    board = []
    for i in range(size_of_board):
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

    return size_of_board, num_stars_reg, board"""

def get_board_json():
    f = open('file_thu.json')
    data = json.load(f)
    size_of_board = data["size_of_board"]
    num_stars_reg = data["num_stars_per_region"]
    board = []
    region = data["region"]
    for i in region.values():
        board.append(i)
    return size_of_board, num_stars_reg, board



#sum of numbers in each rows must be s
def sum_row(size_of_board, T, num_stars_reg):
    for i in range(size_of_board):
        sum_row = 0
        for j in range(size_of_board):
            sum_row += T[i][j]
        model.addConstr(sum_row == num_stars_reg)

#sum of numbers in each columns must be s
def sum_column(size_of_board, T, num_stars_reg):
    for i in range(size_of_board):
        sum_col = 0
        for j in range(size_of_board):
            sum_col += T[j][i]
        model.addConstr(sum_col == num_stars_reg)
#sum of numbers in the adjacent cells <= 1
def sum_adj(size_of_board, T):
    for i in range(size_of_board-1):
        for j in range(size_of_board-1):
            model.addConstr(T[i][j]+T[i][j+1]+T[i+1][j]+T[i+1][j+1] <= 1)
        
#sum of numbers in a region
def sum_reg(size_of_board, T, K, num_stars_reg):
    for i in range(size_of_board):
        sum_reg = 0
        for j in range(len(K[i])):
            sum_reg += T[K[i][j][0]][K[i][j][1]]
        model.addConstr(sum_reg == num_stars_reg)
        
        

def print_board(size_of_board, values):
    for k in range (4 * size_of_board + 1):
        print("-", end = "")
    print("")
    for i in range(size_of_board):
        print("|", end = "")
        for j in range(size_of_board):
            if (int(values[i * size_of_board + j]) == 1):
                print(" * ", end = "|")
            else:
                print("   ", end = "|")
        print("")
        for k in range (4 * size_of_board + 1):
            print("-", end = "")
        print("")

#print(values)

if __name__ == "__main__":
    model = gp.Model('StarBattle')

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #print(os.getcwd())
    #sys.stdin = open("WP-2023-2.txt", "r")
    size_of_board, num_stars_reg, K = get_board_json()
    #print( K)

    T = model.addMVar(shape = (size_of_board,size_of_board), lb = 0, ub = 1, vtype = GRB.INTEGER, name = "fool" )
    sum_row(size_of_board, T, num_stars_reg)
    sum_column(size_of_board, T, num_stars_reg)
    sum_adj(size_of_board, T)
    sum_reg(size_of_board, T, K, num_stars_reg)
    model.setObjective(T[0][0], sense = GRB.MAXIMIZE)

    model.optimize()
    print('-' * 50)
    if model.status == GRB.OPTIMAL:
        print('The status meaning is OPTIMAL')
    print(f'model status: {model.status}')
    print(f'model runtime: {model.runtime}')

    values = model.getAttr("X", model.getVars())
    print_board(size_of_board, values)
    
    
   