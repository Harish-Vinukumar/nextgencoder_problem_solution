"""
Write a program which will take one array of
marks of five students as input and display an array
of candies distributed to them based on their
marks (Max 15 candies)
"""

input_1 = [int(x) for x in input().split()]

candies_list = list()

for x in input_1:
    candies_list.append(round(x/2))
print(input_1, candies_list, sum(candies_list))