# import the standard math library
import math

# define some variables
absolute = -5.999
floor_test = 198.42
floor_test_string = "foo"

# Perform some math functions.
result1 = math.fabs(absolute)
result2 = math.floor(floor_test)
# the following line results in an error: TypeError: must be real number, not str
#result3 = math.floor(floor_test_string)

print("We used the math.fabs() function: ", result1, " is the absolute value of ", absolute)
print("We used the math.floor(): ",result2, " is the floor of ", floor_test)
# Commented out because you cannot assign a sting to the math.floor function.
#print(result3, " is the floor of ", floor_test_string)