from loguru import logger
from src.main.database.mysql_connector import MySQLConnection , MySQLCRUDOperation

class Labour:
    total_count = 0

    def __init__(self, first_name, last_name, wage,role):
        self.first = first_name
        self.last = last_name
        self.wage = wage
        self.role = role
        Labour.total_count += 1

    def save_to_database(self):
        
        query = "Select id from labours where first_name = %s And last_name = %s"
        result = self.crud.read_from_mysql(query, (self.first_name, self.last_name))

        if result:  # If labour already exists, return existing ID
            logger.info(f"Labour already exists with ID: {result[0][0]}")
            return result[0][0]
        
        insert_query = """
                INSERT INTO labours (first_name , last_name , wage , role , email)
                VALUES (%s, %s, %s, %s, %s)
        
        """

        email = self.first_name + "." + self.last_name + "@gmail.com"

        crud.insert_into_mysql(insert_query , (self.first_name , self.last_name , self.wage , self.role, None))

        result = crud.read_from_mysql(query, (self.first_name , self.last_name))

        logger.info(f"New labour added with ID:  {result[0][0]}")
        return result[0][0]


    """
    1. Check if user is already present in table.
    2. If yes then skip saving
    3. Insert into query and write
    """

    # db_connection.save()

    def login(self):
        pass


labour1 = Labour("manish", "Kumer", 2000)

config = configparser.ConfigParser()
config.read('')
config.set("mysql_database" , "password" , decrypt(config[""][""]))
mysql_db_conn_obj = MySqlConnection(config)
crud = MySQLCRUDOperation(mysql_db_conn_obj.connection)

labour1 = Labour("Rajesh", "Singh", 400)
labour1.save_to_database(crud)
print(labour1._Labour__wage)


print(Labour.total_count)

logger.info(f"{labour1}")

logger.info(f"{labour1.__dict__}")

labour2 = Labour("Rajesh", "Singh", 400)

print(Labour.total_count)

logger.info(f"{labour2}")

logger.info(f"{labour2.__dict__}")
