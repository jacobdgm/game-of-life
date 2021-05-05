import random
import time

true_char = " O"
false_char = " -"

class Board():
    def __init__(self, size_x = 12, size_y = 8):
        """
        Initiate board of dimensions size_x by size_y, with all cells
        set to false.
        """
        self.size_x = size_x
        self.size_y = size_y
        
        board = []
        for y in range(size_y):
            y_list = []
            for x in range(size_x):
                y_list.append(False)
            board.append(y_list)
        self.board = board
    
    def __repr__(self):
        """
        Instead of printing lists of True/False, print a grid using
        the values of true_char and false_char
        """
        output = "\n"
        for row in self.board:
            for cell in row:
                output = output + self.render_boolean(cell)
            output = output + "\n"
        return output
    
    def reset(self):
        'Reset board'
        for x in range(self.size_x):
            for y in range(self.size_y):
                self.board[y][x] = False
    
    def toggle(self, *commands):
        'For each pair of coordinates passed, toggle the corresponding cell'
        for coords in commands:
            self.board[coords[0]][coords[1]] = not self.board[coords[0]][coords[1]]
    
    def soup(self, density = 0.5):
        """
        Randomly populate board. Probability of any one cell being alive
        is equal to density.
        """
        # random.seed()
        for x in range(self.size_x):
            for y in range(self.size_y):
                self.board[y][x] = random.random() < density
    
    def next_generation(self, print_result = True):
        'Calculate the next generation.'
        output = []
        
        # for every cell, calculate how many of its neighbours are alive
        for row in range(len(self.board)):
            new_row = []
            for cell in range(len(self.board[0])):
                neighbour_sum = 0
                for y_off in [-1, 0, 1]:
                    if row + y_off >=0 and row + y_off < len(self.board):
                        for x_off in [-1, 0, 1]:
                            if cell + x_off >= 0 and cell + x_off < len(self.board[0]):
                                neighbour_sum += self.board[row + y_off][cell + x_off]
                # dead cells become alive if they have exactly 3 alive neighbours
                if self.board[row][cell] == False:
                    if neighbour_sum == 3:
                        new_row.append(True)
                    else:
                        new_row.append(False)
                
                # alive cells become dead unless they have 2 or 3 living neighbours
                elif self.board[row][cell] == True:
                    neighbour_sum -= 1 # since neighbour_sum includes the current cell
                    if neighbour_sum == 2 or neighbour_sum == 3:
                        new_row.append(True)
                    else:
                        new_row.append(False)
                        
            output.append(new_row)
        
        # check whether board position is the same as previous generation
        if output == self.board:
            still_life = True
        else:
            still_life = False
        
        # update board
        self.board = output
        
        # if required, print results
        if print_result:
            print(self.__repr__())
        
        # pass value of still_life to self.steps()
        return still_life
            
    def steps(self, iterations, step_time = 0.5, print_results = True, print_generation = True):
        'Run simulation a specificied number of times'
        for i in range(iterations):
            if print_generation:
                print(f'Generation {i+1}:')
            
            still_life = self.next_generation(print_results)
            
            # stop iterating if board is empty or unchanged
            if self.is_empty():
                print("Empty board!")
                break
            elif still_life:
                print("Still life!")
                break
            
            time.sleep(step_time)
            
    def step(self, print_results = True):
        'Run a single simulated generation'
        self.steps(1, print_results = print_results, print_generation = False)
    
    def is_empty(self):
        'Return true if there are no living cells'
        for row in self.board:
            if True in row:
                return False
        return True
        
    def render_boolean(self, i):
        'Convert single cells to True/False characters'
        if i:
            return true_char
        else:
            return false_char