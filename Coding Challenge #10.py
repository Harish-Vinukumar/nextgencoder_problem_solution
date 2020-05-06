# Happy kite flying festival!
# Create a program which should give
# design of kite as an output
# Program should contain only for loops
# and no direct print statement an any part
# part of the kite


n = 10

for i in range(n):
    if i % 2 != 0:
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print('* ', end='')
        print()

for i in range(n-2, 0 , -1):
    if i % 2 != 0:
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print('* ', end='')
        print()

for i in range(n):
    if i % 2 != 0 and i <= 3:
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print('* ', end='')
        print()

for i in range(n-2, 0, -1):
    if i % 2 != 0 and i < 3:
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print('* ', end='')
        print()

