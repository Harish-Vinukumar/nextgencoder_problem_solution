# A number is called SPU number if the sum
# and product of its digit are equal
# Eg: 123 is a SPY Number
# (1+2+3) = (1*2*3) = 6

import numpy as np

def spy(num):
    num_str = str(num)
    num_list = list(num_str)
    num_list = [int(x) for x in num_list]
    if sum(num_list) == np.prod(num_list):
        print(num, ' is a SPY Number!')
    else:
        print(num, ' is not a SPY Number!')

num = 456
spy(num)