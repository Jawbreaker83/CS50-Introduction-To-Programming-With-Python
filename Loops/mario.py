""" def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print('#')

main() """

##############################################

""" def main():
    print_row(4)

def print_row(width):
    print('?' * width)

main() """

##############################################

""" def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            # Print brick
            print('#', end='')
            # Print out a new blank line
        print()

main() """

##############################################

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print ('#' * size)
main()