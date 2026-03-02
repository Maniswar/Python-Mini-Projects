#######       ceil function used to round up the values

import math

########################      to paint a wall 

def paint(height,width):  
    # print(height)
    # print(width)  
    area = height * width
    coverage = area/7
    cans_needed = math.ceil(coverage)
    print(f"You need total {cans_needed} cans to paint '{area}'sq meters")
    print("One '1' can paints 7sq meters")

height = int(input("Enter the height of the wall to be painted: "))
width = int(input("Enter the width of the wall to be painted: "))

paint(width = width, height = height)
print('\n')

def paint(**kwargs):
    height = kwargs.get('height')  # Get height from kwargs or default to 0
    width = kwargs.get('width')    # Get width from kwargs or default to 0

    area = height * width
    coverage = area / 7
    cans_needed = math.ceil(coverage)

    print(f"You need a total of {cans_needed} cans to paint {area} sq meters.")
    print("One can of paint covers 7 sq meters.")

height = int(input("Enter the height of the wall to be painted: "))
width = int(input("Enter the width of the wall to be painted: "))

paint(height=height, width=width)

