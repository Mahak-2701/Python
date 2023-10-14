import itertools
def print_permutations(string):
    # Generate all permutations of the string
    permutations = itertools.permutations(string)
    # Print each permutation
    for permutation in permutations:
        print(''.join(permutation))

# Example usage
s = "abcd"
print_permutations(s)

