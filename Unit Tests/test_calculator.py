""" from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2)== 4
    except AssertionError:
        print('2 squared was not 4 ')
    try:
        assert square(3) ==9 
    except AssertionError:
        print('3 squared was not 9')
    try:
        assert square(-2) == 4 
    except AssertionError:
        print('-2 squared was not 4')
    try:
        assert square(-3) == 9 
    except AssertionError:
        print('-3 squared was not 9')
    try:
        assert square(0) == 0 
    except AssertionError:
        print('0 squared was not 0')

if __name__ == '__main__':
    main() """

##########################################################
#  pytest - automates the testing of code as long as you write
#  the tests.  A 3rd party library.

import pytest
from calculator import square

def test_postive():
    assert square(2) == 4
    assert square (3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
   
def test_zero():
    assert square (0)== 0

def test_str():
    with pytest.raises(TypeError):
        square('Cat')

    


