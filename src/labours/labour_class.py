from loguru import logger


class Labour:
    total_count = 0

    def __init__(self, first_name, last_name, wage):
        self.first = first_name
        self.last = last_name
        self.wage = wage
        Labour.total_count += 1



    def save_to_database(self):
        print(self.__wage)
        pass
        query = "Select id from labours where first_name = %s And last_name = %s"
        result = self.crud.read_from_mysql(query, (self.first_name , self.last_name))

        if result:  #If labour already exists, return existing ID
            logger.info(f"Labour already exists with ID: {result[0][0]}")
            return result[0][0]
        pass
    """
    1. Check if user is already present in table.
    2. If yes then skip saving
    3. Insert into query and write
    """
        
        # db_connection.save()

    def login(self):
        pass
    








labour1 = Labour("manish", "Kumer", 2000)


print(Labour.total_count)

logger.info(f"{labour1}")

logger.info(f"{labour1.__dict__}")

labour2 = Labour("Rajesh", "Singh", 400)

print(Labour.total_count)

logger.info(f"{labour2}")

logger.info(f"{labour2.__dict__}")
