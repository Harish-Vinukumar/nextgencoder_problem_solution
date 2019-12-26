# Take integer value as an input and display
# the number of 1's in the binary of that
# number as output
# E.g., 124 (1111100) -> 5


def num_of_ones(num):
    num_bin = bin(num)
    bin_str = str(num_bin)
    return bin_str.count('1')


num = 124
print(num_of_ones(num))