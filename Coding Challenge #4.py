# A function to insert items in an array
# and another function to remove all repeated
# items from an array and display the array.
# E.g., ['Next', 'Gen', 'Next', 'Coder'] -> ['Next', 'Gen', 'Coder']


array = list()

def insert(element):
    array.append(element)


def remove_and_display(array):
    print(list(set(array)))


for i in range(4):
    insert(input("Enter an element:\t"))

remove_and_display(array)




