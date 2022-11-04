"""
Author: GROUP 10
Date: 11/03/22
"""
import numpy as np

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
        demand[i] = round(demand[i])
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
        elif demand[x] > units_manufactured:
        # Scenario where too little units are manufactured/lower than demand and results in loss profits from customers that want to buy
            loss_customers = demand[x] - units_manufactured
            profit_dict[demand[x]] = (demand[x] * profit) - (loss_customers * (retail_price - production_cost))
        else:
        # Scenario where demand and units manufactured are equal
            profit_dict[demand[x]] = (units_manufactured * profit)
    print(profit_dict)



optimal_production_simulation(150, 20, 1000, 150, 28.5, 8.5, 160)
