import itertools

# Generate all combinations of length 4 where each element can be 0, 1, or 2
combinations = list(itertools.product([0, 1, 2], repeat=4))

combinations.sort()

# Print all unique combinations
for combination in combinations:
    combination_str = ''.join(map(str, combination))
    combination_int = int(combination_str)
    #print(combination_int)

#print ("TOTAL: ", len(combinations))

def generate_combinations():
    for x1 in range(3):  # Loop for the first "x"
        for x2 in range(3):  # Loop for the second "x"
            for x3 in range(3):
                combination = f"{x1}{x2}{x3}9"  # Generate combination
                print(combination)

# Call the function to generate and print combinations
generate_combinations()