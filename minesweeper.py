# Author : NaoCoding (Andy Lu)
# Last Update : 2025/04/05
# Task for PicCollage Interview 

import random

# I do the task with a class structure since I think it will be more clear and easier to maintain
class minesweeper:

    # This is the initiaize function of the class, there are also some default numbers for parameters.
    def __init__(self , width : 10 , height : 10 , bomb_count : 10) -> None:
        '''
        width : the width of the board
        height : the height of the board
        bomb_count : the number of bombs on the board
        board : the 2D array for board record
            '#' = not opened
            '0' = opened and no bomb around
            '1' - '8' = opened and there are bombs around
            '*' = opened and there is a bomb
            'F' = flag
        moves : the number of moves made
        '''
        self.width = width
        self.height = height
        self.bomb_count = bomb_count
        self.board = [['#' for _ in range(width)] for _ in range(height)]
        self.bomb_list = []
        self.moves = 0
        self.game_over = False
        pass

    # This function is used to deal with selection of the board
    def select(self , y : int , x : int) -> list[list[int]]:
        '''
        x : the x coordinate of the selection
        y : the y coordinate of the selection
        '''

        # If the selection is out of range, return
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        
        # If the selection is already opened, return
        if self.board[y][x] != '#':
            return

        # If the selection is a bomb, game over
        if self.board[y][x] == '*':
            self.game_over = True
            return
        
        # If the game is already game_over, no selection should be done
        if self.game_over:
            return
        
        if self.moves == 0:
            self.bomb_generation(y , x)
            self.bomb_positions()
        
        self.board[y][x] = self.get_value(y , x)
        self.moves += 1

        
        return self.bomb_list

    def bomb_generation(self , y : int , x : int) -> None:
        '''
        This function is used to generate the bombs on the board
        x : the x coordinate of the selection
        y : the y coordinate of the selection
        '''

        # Important : Notice that since the task in Google Doc doesn't require for full minesweeper game,
        # Therefore, only the target coordinate will be discover even if it is 0
        # (Since I think the traditional minesweeper game will discover the cordinates nearby if the block
        # user selected has no bomb nearby)

        possible_list = []

        for i in range(self.height):
            for j in range(self.width):
                if i != y and j != x:
                    possible_list.append([i , j])

        

        for _ in range(self.bomb_count):
            target = random.randint(0 , len(possible_list) - 1)
            print(target)
            print(target , possible_list[target])
            print(self.width , self.height)
            self.board[possible_list[target][0]][possible_list[target][1]] = '*'
            possible_list.pop(target)
        pass

    # This function is used to get the value of the selection
    def get_value(self , y : int , x : int) -> int:
        '''
        x : the x coordinate of the selection
        y : the y coordinate of the selection
        '''

        count = 0
        
        for i in range(-1 , 2):
            for j in range(-1 , 2):
                if i == 0 and j == 0: continue
                if x + i < 0 or x + i >= self.width or y + j < 0 or y + j >= self.height: continue
                if self.board[y + j][x + i] == '*': count += 1

        return count
    
    # This function append all bomb_position into self.bomb_list.
    def bomb_positions(self) -> None:

        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == '*':
                    self.bomb_list.append([i , j])


# if __name__ == "__main__":
# The example are listed in example.py.