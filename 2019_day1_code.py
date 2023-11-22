"""
The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""
### Part 1 of Challenge ###

import pandas as pd

# Set the file path for the input data
input_data_path = "C:/Users/javaih/OneDrive - Office for National Statistics/Advent-of-code/2019_day1_input.txt"

# Read the text file into a DataFrame
module_masses_df = pd.read_table(
    input_data_path,
    # Avoid treating the first row as a header
    header=None,)

# Extract the module masses from the DataFrame and convert them to a list
module_masses_list = module_masses_df.iloc[:, 0].tolist()

# Define the functions

def calculate_fuel(mass):
    """
    Calculate the fuel required for a module based on its mass.

    Parameters:
    - mass (int): The mass of the module.

    Returns:
    - int: The calculated fuel required for the module.
    """
    # Calculate the fuel required for a module
    return max(mass // 3 - 2, 0)

def total_fuel_requirements(module_masses):
    """
    Calculate the total fuel requirements for all modules.

    Parameters:
    - module_masses (list): A list of integers representing the masses of individual modules.

    Returns:
    - int: The total fuel requirements for all modules.
    """
    # Calculate the total fuel requirements for all modules
    return sum(calculate_fuel(mass) for mass in module_masses)

# Calculate the total fuel requirements for all modules
total_fuel = total_fuel_requirements(module_masses_list)

# Print the total fuel requirements
print(f'The total fuel requirements for all modules is: {total_fuel}')

### Part 2 of Challenge ###

def calculate_fuel_loop(mass):
    """
    Calculate the total fuel required for a module and its fuel in a loop.

    Parameters:
    - mass (int): The mass of the module.

    Returns:
    - int: The total fuel required for the module and its fuel.
    """
    total_fuel = 0

    # Continue calculating fuel loop until no additional fuel is needed
    while True:
        fuel = max(mass // 3 - 2, 0)
        if fuel == 0:
            # If no additional fuel is needed, break out of the loop
            break
        total_fuel += fuel
        mass = fuel

    return total_fuel

# Calculate the total fuel requirements for all modules, including additional fuel
total_fuel_loop = sum(calculate_fuel_loop(mass) for mass in module_masses_list)

# Print the total fuel requirements, including additional fuel
print(f'The total fuel requirements for all modules, including additional fuel, is: {total_fuel_loop}')
