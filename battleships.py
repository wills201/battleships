import pandas as pd
import numpy as np
import random as rn
class Battleships:
    def __init__(self, cpu_board, user_board):
        self.cpu_board = cpu_board
        self.user_board = user_board
    def user_grid():
        x_axis = {1:"",2:"",3:"",4:"",5:""}
        y_axis = [1,2,3,4,5]
        user_board = pd.DataFrame(data = x_axis, index = y_axis)
        return user_board
    
    def cpu_grid():
        x_axis = {1:"",2:"",3:"",4:"",5:""}
        y_axis = [1,2,3,4,5]
        cpu_board = pd.DataFrame(data = x_axis, index = y_axis)
        return cpu_board
        cpu_grid()
    def cpu_ship():
        row = rn.randint(1,5)
        column = rn.randint(1,5)
        new_grid = cpu_board.at(row, column) = "S"
        return new_grid
    cpu_ship()
    def user_ship(x,y):
        coor = input()
        user_input = coor.split(",")
        if len(coor) != 2:
            raise Exception("Too many or too few coordinates.")
        coor[0] = x
        coor[1] = y
        user_board.at(x,y,"S")

