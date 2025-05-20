import argparse
import os
import subprocess
import sys
from datetime import datetime
from ecosystem import create_empty_board, populate_board, visualize_board, update_board_state, count_prey_predators

def main():
    #initialize directory to store images/gif    
    directory = '../runs/images'
    os.makedirs(directory, exist_ok=True)
    #Parse arguments
    parser = argparse.ArgumentParser(description='Generate and visualize a 2D cellular automata grid.')
    parser.add_argument('--itrs', type=int, default=3, help='Number of iterations')
    parser.add_argument('--rows', type=int, default=100, help='Number of rows in the grid')
    parser.add_argument('--columns', type=int, default=100, help='Number of columns in the grid')
    parser.add_argument('--prey_density', type=float, default=0.1, help='Density of populated cells representing "prey" (between 0 and 1)')
    parser.add_argument('--predator_density', type=float, default=0.05, help='Density of populated cells representing "predators" (between 0 and 1)')
    parser.add_argument('--predator_energy', type=int, default=20,help="Number of iterations a predator can survive without eating before dying")
    parser.add_argument('--breeding_cooldown', type=int, default=5,help="Number of iterations a prey has to wait before breeding again")
    args = parser.parse_args()

    #set up board
    print("Creating empty board...\n")
    board = create_empty_board(args.rows, args.columns)
    print("Populating board...\n")
    populate_board(board, args.prey_density, args.predator_density, args.predator_energy,args.breeding_cooldown)

    #run for itrs iterations, save generated images to filename.
    print("Running simulation...")
    for i in range(args.itrs):
        filename = os.path.join(directory, f'image_{i}.png')
        visualize_board(board, filename)
        update_board_state(board, args.predator_energy)

        # Check if the ecosystem has collapsed
        prey_count, predator_count = count_prey_predators(board)
        if prey_count == 0 or predator_count == 0:
            print(f"Ecosystem collapse detected at iteration {i+1}.")
            print(f"Remaining Prey: {prey_count}, Remaining Predators: {predator_count}")
            break  # Terminate simulation if there are no prey or predators left

    #create gif out of saved images  
    print("Creating gif...")  
    subprocess.run([sys.executable, 'code/gif_creator.py', directory, os.path.join('runs', f'video.gif')])

if __name__ == "__main__":
    main()