from loguru import logger

length_of_land = 100
breadth_of_land = 60

circumference_for_land = 2 * (length_of_land + breadth_of_land)
logger.info(f"circumference_for_land {circumference_for_land}")

cost_for_fencing_land = circumference_for_land * 17
logger.info(f"cost_for_fencing_land {circumference_for_land}")


def calculate_fencing_cost(length, breadth, cost_per_ft):
    circumference = 2 * (length + breadth)
    cost_for_fencing = circumference * cost_per_ft
    return cost_for_fencing


cost_for_fencing_land = calculate_fencing_cost(length_of_land, breadth_of_land, 17)

logger.info(f"fencing cost for land is:  {cost_for_fencing_land}")


## Postional Argument *args


def final_cart_amount(*args, discount):
    result = 0
    for amount in args:
        result += amount
    print(result)

    amount_after_discount = result - (result * discount)

    return amount_after_discount


final_amount_to_be_paid = final_cart_amount(1000, 500, 280, 430, discount=0.5)


logger.info(f"final_amount_to_be_paid : {final_amount_to_be_paid}")


# Keyword Argument  **kwarg


"""
1. Write a program where you need to take n numbers of inputs from user and return the total sum of it.

"""


"""
2. Write a programme in which functions take logs input from the user and write this into a file. 
How to write in to file has not
"""
