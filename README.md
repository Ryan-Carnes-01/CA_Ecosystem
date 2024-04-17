# CA_Ecosystem
This program uses a 2D cellular automata to create a simulated ecosystem with variable parameters. "Prey" and "Predators" are randomly spawned on the 2D CA with a specified density, then the program runs for a number of iterations, with each cell changing state based on it's neighboring states and according to it's own rules. The "Prey" wander and reproduce, while the "Predators" consume the prey. Varying the parameters given to the program will result in different ecosystem balances with varying outcomes. Our goal is to try to find the optimal balance that holds a "healthy, diverse, and self-sustaining" ecosystem for as long as possible.
# How it works
ecosystem.py - contains the class definitions and helper functions for the 2D CA ecosystem.

main.py - contains the driver code that implements the functions from ecosystem.py. Run this one to run the CA.
# To run the program
python main.py {--help} {--rows} int {--columns} int {--prey_density} float between 0.0-1.0 {--predator_density} float between 0.0-1.0
