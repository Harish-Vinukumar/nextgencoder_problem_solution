# A function to insert items in an array
# and another function to display the
# most repeated item from an array


array = list()

def insert(element):
    array.append(element)

def display(array):
    max_value = max([array.count(x) for x in list(set(array))])
    result_list = [x for x in list(set(array)) if array.count(x) == max_value]
    print(result_list)

for i in range(4):
    insert(input("Enter an element:\t"))

display(array)