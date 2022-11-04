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
    return demand


def optimal_production_simulation(mean, stddev, size, retail_price, production_cost, disposal_cost, number_to_manufacture):
    """
    Uses inputs to calculate the optimal production level given randomly generated demand

    Parameter retail_price: the price that the product is being sold for
    Precondition: retail_price is an integer >= $0.00

    Parameter production_cost: the costs associated with manufacturing the product
    Precondition: production_cost is an integer >= $0.00

    Parameter disposal_cost: the costs associated with disposing of the product in an environmentally sustainable way
    Precondition: disposal_cost is an integer >= $0.00

    Parameter number_to_manufacture: the number that is manufactured as a result of the inputs
    Precondition: number_to_manufacture is an integer >= 0
    """

# print(generate_random_demand(150, 20, 1000))
