from loguru import logger 

import configparser

config = configparser.ConfigParser()

config.read("/Users/pawanchahar/Python_Manish/config_file.ini")


brick_cost = config["raw_materials"]["brick_cost"]

logger.info(f'{brick_cost} , type of brick cost {type(brick_cost)}')

def total_no_of_bricks(length , breadth , height):
    no_of_bricks_in_length_side = length * (height*2)
    total_no_of_bricks_in_length_side = no_of_bricks_in_length_side *2 


    no_of_bricks_in_breadth_side = breadth * (height *2)
    total_no_of_bricks_in_breadth_side = no_of_bricks_in_breadth_side*2 

    total_no_of_bricks = total_no_of_bricks_in_length_side + total_no_of_bricks_in_breadth_side

    return total_no_of_bricks

def total_cost_bricks(config):
    brick_cost = float(config["raw_materials"]["brick_cost"])
    total_no_bricks = total_no_of_bricks(15, 15,10)
    final_cost = brick_cost * total_no_bricks
    return final_cost 

result = total_cost_bricks(config )

logger.info(f"Total bricks cost to make 1 room {result}")



"""
a. Calculate the cost of books bought by each students.

book_name      cost
Science         262
Maths           178
History         59
Physics         231
Biology         165
Chemistry       110

student_details = {1 : ['Maths' ,'History'],
                    2 : ['Biology' , 'Chemistry' , 'History'],
                    3 : ['Science']}


condition: 
# Save the book cost details in ini file

b. What will be the cost for books if discount is 10% . But the condition to
get discount is , you will have to buy 2 or more books.

"""
