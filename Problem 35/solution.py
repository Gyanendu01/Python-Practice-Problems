import math
#  Function to accept angle from user input
def angle_input():
    angle = float(input("\n\tEnter an angle from keyboard: "))
    return angle

# Function to determine sin and cos of the angle and display the result
def display_angle(angle):
    rad_angle = math.radians(angle)
    deg_angle = math.degrees(rad_angle)

    # Calculation of sin and cos in radian
    print("\n\tSIN() AND COSINE() OF THE ANGLE IN RADIAN")
    print("\tsin({}) = {}".format(rad_angle,math.sin(rad_angle)))
    print("\tcos({}) = {}".format(rad_angle,math.cos(rad_angle)))
    
    # Calculation of sin and cos in degrees
    print("\n\tSIN() AND COSINE() OF THE ANGLE IN RADIAN")
    print("\tsin({}) = {}".format(deg_angle,math.sin(deg_angle)))
    print("\tcos({}) = {}".format(deg_angle,math.cos(deg_angle)))

# Main program
value = angle_input()
display_angle(value)
