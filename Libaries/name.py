""" import sys

try:
    print('Hello, my name is', sys.argv[1])
except IndexError:
    print("To few arguments") """

#################################################
""" import sys

if len(sys.argv) < 2:
    print('Too Few Arguments.')
elif len(sys.argv) > 2:
    print('Too Many Arguments.')
else:
    print('Hello, my name is', sys.argv[1]) """

#################################################
""" import sys

if len(sys.argv) < 2:
    sys.exit('Too Few Arguments.')
elif len(sys.argv) > 2:
    sys.exit('Too Many Arguments.')

print('Hello, my name is', sys.argv[1]) """

#################################################
import sys

if len(sys.argv) < 2:
    sys.exit('Too Few Arguments.')

for arg in sys.argv[1:]:
    print('Hello, my name is', arg)

