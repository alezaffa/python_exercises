from math import pi


def calculate_area(radius):
    inner_area = radius**2 * pi
    print("Area of circle having radius is ", inner_area)
    return inner_area


calculate_area(1)
calculate_area(2)
calculate_area(3)
calculate_area(4)
calculate_area(5)
calculate_area(6)

calculate_area(float(input("Insert radius: ")))

