#!/usr/bin/env python3
# created by: [Mignonne Gihozo]
# created on: [2026-09-30]
# this program calculates the perimeter (circumference) and area of a circle given its radius
import math


def main():
    # set the radius from user input
    radius = float(input("Enter the radius (cm): "))

    # calculate the perimeter (circumference) and area of the circle
    perimeter = 2 * math.pi * radius
    area = math.pi * (radius**2)

    # display the results
    print("For a radius of {} cm:".format(radius))
    print("The perimeter is: {:.2f} cm".format(perimeter))
    print("The area is: {:.2f} cm²".format(area))


if __name__ == "__main__":
    main()
