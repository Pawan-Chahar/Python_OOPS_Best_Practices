from loguru import logger 

class Labour:
    total_count = 0
    def __init__(self, first_name , last_name , wage):

        self.first = first_name
        self.last = last_name
        self.wage = wage 
        Labour.total_count += 1

labour1 = Labour("manish" ,"Kumer", 2000)



print(Labour.total_count)

logger.info(f'{labour1}')

logger.info(f'{labour1.__dict__}')

labour2 = Labour("Rajesh" , "Singh" , 400)

print(Labour.total_count)

logger.info(f'{labour2}')

logger.info(f'{labour2.__dict__}')