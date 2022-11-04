"""
Author: GROUP 10
Date: 11/04/22
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_random_demand(mean, stddev, size):
    """
    Generates a random sample of demand instances from a normal (Gaussian) distribution.

    Parameter mean: the average demand for the product
    Precondition: mean is an integer

    Parameter stddev: the standard deviation
    Precondition: stddev is an integer

    Parameter size: the number of instances or random samples to be created
    Precondition: size is an integer
    """
    demand = np.random.normal(mean, stddev, size)
    for i in range(size):
        demand[i] = round(demand[i],4)
    return demand

def optimal_production_simulation(mean, stddev, size, retail_price, production_cost, disposal_cost, units_manufactured):
    """
    Uses inputs to calculate the optimal production level given randomly generated demand

    Parameter retail_price: the price that the product is being sold for
    Precondition: retail_price is an integer >= $0.00

    Parameter production_cost: the costs associated with manufacturing the product
    Precondition: production_cost is an integer >= $0.00

    Parameter disposal_cost: the costs associated with disposing of the product in an environmentally sustainable way
    Precondition: disposal_cost is an integer >= $0.00

    Parameter units_manufactured: the number that is manufactured as a result of the inputs
    Precondition: units_manufactured is an integer >= 0
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
    # print(str(units_manufactured) + " units manufactured")

    # Calculate mean profit of the production level
    sum = 0
    for val in profit_dict.values():
        sum += val
    result = round(sum / len(profit_dict),2)
    # print("AVG: " + str(result))

    # Calculate standard deviation of the profit
    profit_list = []
    for val in profit_dict.values():
        profit_list.append(val)
    std = round(np.std(profit_list),2)
    # print("STD: " + str(std))
    # print("===========================")
    return result

x_manufacture_level = []
y_profit = []
for i in range(100, 250):
    x_manufacture_level.append(i)
    y_profit.append(optimal_production_simulation(150, 20, 1000, 150, 28.5, 8.5, i))

plt.plot(x_manufacture_level, y_profit, 'ro', markersize=1)
plt.xlabel('Manufacture Level')
plt.ylabel('Profit')
plt.show()
