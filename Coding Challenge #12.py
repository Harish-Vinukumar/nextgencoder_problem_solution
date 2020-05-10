"""
Write a program which will take two arrays
as input and will display two arrays with Union
and Intersection of them.
"""

input_1  = set([int(x) for x in input().split()])
input_2  = set([int(x) for x in input().split()])

print("Union", input_1.union(input_2))
print("Intersection", input_1.intersection(input_2))