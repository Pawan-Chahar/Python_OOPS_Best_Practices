'''
Write a programme to open a file. If file is empty then raise a exception 
If it's not empty then find out all of the unique names in the file.
'''

from loguru import logger

def final_cart_amount(*args , discount):
    try:

        result =0
        for amount in args:
            result +=  amount
        print(result)

        amount_after_discount = result - (result*discount)

        return amount_after_discount
    except NameError:
        logger.info(' Variable is not found')
        raise  Exception("Please check the variable name")
    except TypeError:
        logger.info('Please Provide the amount in Integer')
        raise Exception('Value provided is not an Integer coming from TypeError')
    except Exception as e:
        logger.info("Can not process the cart amount ")
        raise e 
    




try:

    final_amount_to_be_paid = final_cart_amount(1000,500,280,120,'500' ,430,discount =0.5)
    logger.info(f'final_amount_to_be_paid : {final_amount_to_be_paid}')

    

except Exception as e:
    logger.info(e)
    raise e



logger.info("Database Connection Succesfully. Job Run Succesfully")