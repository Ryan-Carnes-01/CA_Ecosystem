import argparse
import os
import subprocess
from datetime import datetime
from ecosystem import create_empty_board, populate_board, visualize_board, update_board_state

def main():
    #Parse arguments
    parser = argparse.ArgumentParser(description='Generate and visualize a 2D cellular automata grid.')
    parser.add_argument('--itrs', type=int, default=3, help='Number of iterations')
    parser.add_argument('--rows', type=int, default=100, help='Number of rows in the grid')
    parser.add_argument('--columns', type=int, default=100, help='Number of columns in the grid')
    parser.add_argument('--prey_density', type=float, default=0.1, help='Density of populated cells representing "prey" (between 0 and 1)')
    parser.add_argument('--predator_density', type=float, default=0.05, help='Density of populated cells representing "predators" (between 0 and 1)')
    args = parser.parse_args()
    print(f"ROWS: {args.rows}\nCOLUMNS: {args.columns}\nPREY_DENSITY: {args.prey_density}\nPREDATOR_DENSITY: {args.predator_density}\n")

 # Create a unique directory for this run using a timestamp and a subdirectory for images
    run_directory = f'runs/experiment'
    image_directory = os.path.join(run_directory, 'images')
    os.makedirs(image_directory, exist_ok=True)

    board = create_empty_board(args.rows, args.columns)
    populate_board(board, args.prey_density, args.predator_density)

    for i in range(args.itrs):
        filename = os.path.join(image_directory, f'image_{i}.png')
        visualize_board(board, filename)
        update_board_state(board)

    # Call the script to create a GIF from the images and save it in the run directory
    subprocess.run(['python', 'gif_creator.py', image_directory, os.path.join(run_directory, f'video.gif')])

if __name__ == "__main__":
    main()