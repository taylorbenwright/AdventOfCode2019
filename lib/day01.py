

from math import floor
import helpers


@helpers.timer
def solve_01():
    masses = [int(line) for line in open("../inputs/day01.txt", "r").read().splitlines()]
    fuel_needs = [(floor(mass / 3) - 2) for mass in masses]
    return fuel_needs


@helpers.timer
def solve_02():
    masses = [int(line) for line in open("../inputs/day01.txt", "r").read().splitlines()]
    total_fuel_needed = 0
    for mass in masses:
        needs_fuel = True
        fuel_needs = mass
        while needs_fuel:
            fuel_needs = (floor(fuel_needs / 3) - 2)
            if fuel_needs <= 0:
                needs_fuel = False
            else:
                total_fuel_needed += fuel_needs
    return total_fuel_needed


print("Day01 Part01 Solve: {}".format(sum(solve_01())))
print("Day01 Part02 Solve: {}".format(solve_02()))
