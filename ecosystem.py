import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Prey:
    def __init__(self):
        self.reproduce = False
        self.value = 1
        self.location = (0,0)
        self.previous_location = (0,0)

class Predator:
    def __init__(self):
        self.reproduce = False
        self.value = 2
        self.location = (0,0)
        self.previous_location = (0,0)

def create_empty_board(rows, columns):
    print("Creating empty board...\n")
    board = [[None for _ in range(columns)] for _ in range(rows)]
    return board

def populate_board(board, prey_density, predator_density):
    print("Populating board...\n")
    num_rows = len(board)
    num_cols = len(board[0])

    num_prey = int(num_rows * num_cols * prey_density)
    num_predators = int(num_rows * num_cols * predator_density)

    #Populate prey
    for _ in range(num_prey):
        row = random.randint(0, num_rows - 1)
        col = random.randint(0, num_cols - 1)
        if board[row][col] is None:
            board[row][col] = Prey()
            board[row][col].location = (row, col)
            board[row][col].previous_location = (row,col)

    #Populate predators
    for _ in range(num_predators):
        row = random.randint(0, num_rows - 1)
        col = random.randint(0, num_cols - 1)
        if board[row][col] is None:
            board[row][col] = Predator()
            board[row][col].location = (row, col)
            board[row][col].previous_location = (row,col)
    return

def visualize_board(board):
    print("Visualizing board...")
    empty_color = 'white'
    prey_color = 'green'
    predator_color = 'red'
    cmap = ListedColormap([empty_color, prey_color, predator_color])

    #Convert to a numpy array for plotting
    board_array = np.zeros_like(board, dtype=int)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if isinstance(board[i][j], Prey):
                board_array[i][j] = board[i][j].value
            elif isinstance(board[i][j], Predator):
                board_array[i][j] = board[i][j].value

    #Plot
    plt.figure(figsize=(8, 6))
    plt.imshow(board_array, cmap=cmap, interpolation='nearest')
    cbar = plt.colorbar(ticks=[0, 1, 2], label='Entity')
    cbar.set_ticks([0, 1, 2])
    cbar.set_ticklabels(['Empty', 'Prey', 'Predator'])
    plt.title('Cellular Automata Board')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.grid(False)
    plt.show()

#def update_cell_state(board):
    #return

def update_board_state(board):
    for row in board:
        for cell in row:
            if cell != None:
                print(f"cell: {cell}")
                location = list(cell.location)
                print(location)
    return