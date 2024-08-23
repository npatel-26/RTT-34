# defines the value of pi
pi = 3.14159

# Calculate the area of a circle for a given radius
def calculate_circle_area(radius):
    # pi multiplied by r squared
    return pi+radius**2

r = int(input('Enter the radius of the circle: '))
area = calculate_circle_area(r)

print(area)
