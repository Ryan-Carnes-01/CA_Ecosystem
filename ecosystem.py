import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

prey_move_left_options=[9209,#upper right corner, predator below
                        2909,#lower right corner, predator above
                        2202,#surrounded by preds except for left
                        2209,#right border, preds above and below
                        9202,#top border, preds below and right
                        2902] #bottom border, preds above and right

prey_move_right_options=[9290, #upper left corner, predator below
                         2990, #lower left corner, predator above
                         2220, #surrounded by preds except for right
                         2290, #left border, preds above and below
                         9220, #top border, preds below and left
                         2920] #bottom border, preds above and left

prey_move_down_options = []

prey_move_up_options = []


pred_move_left_options = []

pred_move_right_options = []

pred_move_down_options = []

pred_move_up_options = []


class Prey:
    def __init__(self):
        self.reproduce = False
        self.value = 1
        self.location = (0,0)
        self.move = True

class Predator:
    def __init__(self):
        self.reproduce = False
        self.value = 2
        self.location = (0,0)
        self.move = True

def move_up(board,cell):
    cell_row,cell_col = cell.location
    #print(f"Moving cell up from {cell.location} to {cell_row-1} {cell_col}")
    board[cell_row-1][cell_col] = cell
    board[cell_row][cell_col] = None
    cell.location = (cell_row-1, cell_col)
    cell.move = False

def move_down(board,cell):
    cell_row,cell_col = cell.location
    #print(f"Moving cell down from {cell.location} to {cell_row+1} {cell_col}")
    board[cell_row+1][cell_col] = cell
    board[cell_row][cell_col] = None
    cell.location = (cell_row+1, cell_col)
    cell.move = False

def move_right(board,cell):
    cell_row,cell_col = cell.location
    #print(f"Moving cell right from {cell.location} to {cell_row} {cell_col+1}")
    board[cell_row][cell_col+1] = cell
    board[cell_row][cell_col] = None
    cell.location = (cell_row, cell_col+1)
    cell.move = False

def move_left(board,cell):
    cell_row,cell_col = cell.location
    #print(f"Moving cell left from {cell.location} to {cell_row} {cell_col-1}")
    board[cell_row][cell_col-1] = cell
    board[cell_row][cell_col] = None
    cell.location = (cell_row, cell_col-1)
    cell.move = False

def move_random(board,cell):
    random_number = random.randint(0, 3)
    if random_number == 0:
        move_up(board,cell)
    elif random_number == 1:
        move_down(board,cell)
    elif random_number == 2:
        move_left(board,cell)
    elif random_number == 3:
        move_right(board,cell)

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
    #Populate predators
    for _ in range(num_predators):
        row = random.randint(0, num_rows - 1)
        col = random.randint(0, num_cols - 1)
        if board[row][col] is None:
            board[row][col] = Predator()
            board[row][col].location = (row, col)
    return

def visualize_board(board):
    print("\nVisualizing board...")
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

def get_neighborhood_option(board, cell):
    neighborhood_checklist = [9,9,9,9] #[up,down,left,right]
    cell_row,cell_col = cell.location
    rows = len(board)-1
    cols = len(board[0])-1
        
    #check if cell is on upper border
    if cell.location[0] == 0:
        #Cell on top border
        neighborhood_checklist[0] = 9
    elif isinstance(board[cell_row-1][cell_col],Predator):
        #print("Predator above cell")
        neighborhood_checklist[0] = 2
    elif isinstance(board[cell_row-1][cell_col],Prey):
        #print("Prey above cell")
        neighborhood_checklist[0] = 1
    else:
        neighborhood_checklist[0] = 0

    #check if cell is on bottom border
    if cell.location[0] == rows:
        #print("Cell on bottom border")
        neighborhood_checklist[1] = 9
    elif isinstance(board[cell_row+1][cell_col],Predator):
        #print("Predator below cell")
        neighborhood_checklist[1] = 2
    elif isinstance(board[cell_row+1][cell_col],Prey):
        #print("Prey below cell")
        neighborhood_checklist[1] = 1
    else:
        neighborhood_checklist[1] = 0

    #check if cell is on left border
    if cell.location[1] == 0:
        #print("Cell on left border")
        neighborhood_checklist[2] = 9
    elif isinstance(board[cell_row][cell_col-1],Predator):
        #print("Predator left of cell")
        neighborhood_checklist[2] = 2
    elif isinstance(board[cell_row][cell_col-1],Prey):
        #print("Prey left of cell")
        neighborhood_checklist[2] = 1
    else:
        neighborhood_checklist[2] = 0

    #check if cell is on right border
    if cell.location[1] == cols:
        #print("Cell on right border")
        neighborhood_checklist[3] = 9
    elif isinstance(board[cell_row][cell_col+1],Predator):
        #print("Predator right of cell")
        neighborhood_checklist[3] = 2
    elif isinstance(board[cell_row][cell_col+1],Prey):
        #print("Prey right of cell")
        neighborhood_checklist[3] = 1
    else:
        neighborhood_checklist[3] = 0

    return neighborhood_checklist

def update_cell(board,cell,option):
    #[up,down,left,right]
    #0 = open, 1 = Prey, 2 = Predator, 9 = border
    cell_row,cell_col = cell.location
    option_str = ''.join(map(str, option))
    option_int = int(option_str)
    print(f"CELL: {cell}, OPTION: {option_int}")
    #if cell has already moved, dont move it
    if cell.move == False:
        print("     - CELL ALREADY MOVED, SKIPPING")
        return
    if(isinstance(cell, Predator)): #update predator based on option
        if(option_int == 0): #no neighbors, move randomly
            print("     - PREDATOR random move")
            move_random(board,cell)
        #if reason to move left
            #move left
        #if reason to move right
            #move right
        #if reason to move down
            #move down
        #if reason to move up
            #move up
    elif(isinstance(cell, Prey)): #update prey based on option
        if(option_int == 0): #no neighbors, move randomly
            print("     - PREY random move") 
            move_random(board,cell)
        elif option_int in prey_move_left_options: #if reason to move left
            print("     - PREY left move")
            move_left(board,cell)
        elif option_int in prey_move_right_options: #if reason to move right
            print("     - PREY right move")
            move_right(board,cell)
        #if reason to move down
            #move down
        #if reason to move up
            #move up

def update_board_state(board):
    for row in board:
        for cell in row:
            if cell != None:
                option = get_neighborhood_option(board, cell)
                update_cell(board,cell,option)
    #reset cell movement flag
    for row in board:
        for cell in row:
            if cell != None:
                cell.move = True
    return