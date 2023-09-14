""" try:
    x = int(input('What is x? '))
    print(f'x is {x}')
except ValueError:
    print('x is not an integer') """

    #############################################

""" try:
    x = int(input('What is x? '))
except ValueError:
    print('x is not an integer')
else:
    print(f'x is {x}') """

#############################################
""" while True:
    try:
        x = int(input('What is x? '))
    except ValueError:
        print('x is not an integer')
    else:
        break
print(f'x is {x}') """
    
###########################################
""" 
while True:
    try:
        x = int(input('What is x? '))
        break
    except ValueError:
        print('x is not an integer')
print(f'x is {x}') """

############################################

""" def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            x = int(input('What is x? '))
        except ValueError:
            print('x is not an integer')
        else:
            break
    return x

main() """

##########################################

""" def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            x = int(input('What is x? '))
        except ValueError:
            print('x is not an integer')
        else:
            return x

main() """

############################################

""" def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            return int(input('What is x? '))
        except ValueError:
            print('x is not an integer')

main()
 """
##############################################

""" def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            return int(input('What is x? '))
        except ValueError:
            pass
main() """

##############################################

def main():
    x = get_int('What is x? ')
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()