"""
Author: GROUP 10
Date: 11/04/22
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_random_demand(mean, stddev, size):
    """
    Generates a random sample of demand instances from a normal (Gaussian) distribution.
    """
    demand = np.random.normal(mean, stddev, size)
    for i in range(size):
        demand[i] = round(demand[i],4)
    return demand

def calc_optimal_production(mean, stddev, size, retail_price, production_cost, disposal_cost, units_manufactured):
    """
    Uses inputs to calculate the optimal production level given randomly generated demand
    """
    demand = generate_random_demand(mean, stddev, size)
    profit = retail_price - production_cost
    profit_dict = {}

    for x in range(size):
        # Scenario where too many units are manufactured/higher than demand and results in loss from unsold units + disposal cost
        if demand[x] < units_manufactured:
            loss_units = units_manufactured - demand[x]
            profit_dict[demand[x]] = (demand[x] * profit) - (loss_units * (production_cost + disposal_cost))

        # Scenario where too little units are manufactured/lower than demand and results in loss profits from customers that want to buy
        elif demand[x] > units_manufactured:
            loss_customers = demand[x] - units_manufactured
            profit_dict[demand[x]] = (units_manufactured * profit) - (loss_customers * (retail_price - production_cost))

        else:
        # Scenario where demand and units manufactured are equal
            profit_dict[demand[x]] = (units_manufactured * profit)
    # print(profit_dict) # Checking what the profit dictionary looks like
    print(str(units_manufactured) + " units manufactured")

    # Calculate mean profit of the production level
    sum = 0
    for val in profit_dict.values():
        sum += val
    result = round(sum / len(profit_dict),2)
    print("AVG: " + str(result))

    # Calculate standard deviation of the profit
    profit_list = []
    for val in profit_dict.values():
        profit_list.append(val)
    std = round(np.std(profit_list),2)
    print("STD: " + str(std))
    print("===========================")
    return result

def run_simulation(min_lvl, max_lvl, mean, stddev, size, retail_price, production_cost, disposal_cost):
    """
    Simulation run - finds optimal production level by calculating average profit given a demand at various manufacturing levels
    Plots results on a graph and prints the optimal number of units to manufacture.
    """
    x_manufacture_level = []
    y_profit = []
    for i in range(min_lvl, max_lvl):
        x_manufacture_level.append(i)
        y_profit.append(calc_optimal_production(mean, stddev, size, retail_price, production_cost, disposal_cost, i))

    # Print out the recommendation to the user
    optimal_value_profit = max(y_profit)
    optimal_number = x_manufacture_level[y_profit.index(optimal_value_profit)]
    print("Recommendation: " + str(optimal_number) + " units yields an average profit of " + "$" + str(optimal_value_profit))

    plt.title("Manufacturing Level Simulation", loc = 'left', fontsize = 20)
    plt.xlabel('Manufacture Level')
    plt.ylabel('Profit')
    plt.xticks(np.arange(min(x_manufacture_level), max(x_manufacture_level)+1, 10.0))
    sctr = plt.scatter(x_manufacture_level, y_profit, c=y_profit, cmap='RdYlGn')
    plt.colorbar(sctr, format='$%d')
    plt.grid()
    plt.show()

def run_program():
    min_lvl = int(input("Enter the lowest manufacturing level you want to simulate: "))
    max_lvl = int(input("Enter the highest manufacturing level you want to simulate: "))
    mean = float(input("Enter the mean: "))
    stddev = float(input("Enter the standard deviation: "))
    size = int(input("Enter the number of demand simulations you want to run: "))
    retail_price = float(input("Enter the retail price: "))
    production_cost = float(input("Enter the production cost: "))
    disposal_cost = float(input("Enter the disposal cost: "))

    run_simulation(min_lvl, max_lvl, mean, stddev, size, retail_price, production_cost, disposal_cost)

# Testing Function: generate_random_demand(mean, stddev, size)
# print(generate_random_demand(150, 20, 1000))

# Enable to run program
run_program()
