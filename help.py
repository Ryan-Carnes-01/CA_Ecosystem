import itertools

# Generate all combinations of length 4 where each element can be 0, 1, or 2
combinations = list(itertools.product([0, 1, 2], repeat=4))

combinations.sort()

# Print all unique combinations
for combination in combinations:
    combination_str = ''.join(map(str, combination))
    combination_int = int(combination_str)
    print(combination_int)

print ("TOTAL: ", len(combinations))