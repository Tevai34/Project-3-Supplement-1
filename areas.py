# areas.py
import math

def area_rectangle(length, width):
     # Check if the rectangle is actually a square (length == width)
    if length == width:
        return length ** 2
    return length * width

def area_circle(radius):
    # Calculate the area of a circle using the formula π * r^2
    return math.pi * (radius ** 2)

def area_triangle(base, height):
    # Calculate the area of a triangle using the formula 0.5 * base * height
    return 0.5 * base * height
