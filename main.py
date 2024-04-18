import argparse
import os
import subprocess
from datetime import datetime
from ecosystem import create_empty_board, populate_board, visualize_board, update_board_state

def main():
    #initialize directory to store images/gif    
    directory = 'runs/images'
    os.makedirs(directory, exist_ok=True)
    #Parse arguments
    parser = argparse.ArgumentParser(description='Generate and visualize a 2D cellular automata grid.')
    parser.add_argument('--itrs', type=int, default=3, help='Number of iterations')
    parser.add_argument('--rows', type=int, default=100, help='Number of rows in the grid')
    parser.add_argument('--columns', type=int, default=100, help='Number of columns in the grid')
    parser.add_argument('--prey_density', type=float, default=0.1, help='Density of populated cells representing "prey" (between 0 and 1)')
    parser.add_argument('--predator_density', type=float, default=0.05, help='Density of populated cells representing "predators" (between 0 and 1)')
    args = parser.parse_args()
    print(f"ROWS: {args.rows}\nCOLUMNS: {args.columns}\nPREY_DENSITY: {args.prey_density}\nPREDATOR_DENSITY: {args.predator_density}\n")

    #set up board
    board = create_empty_board(args.rows, args.columns)
    populate_board(board, args.prey_density, args.predator_density)

    #run for itrs iterations, save generated images to filename.
    for i in range(args.itrs):
        filename = os.path.join(directory, f'image_{i}.png')
        visualize_board(board, filename)
        update_board_state(board)

    #create gif out of saved images    
    subprocess.run(['python', 'gif_creator.py', directory, os.path.join('runs', f'video.gif')])

if __name__ == "__main__":
    main()