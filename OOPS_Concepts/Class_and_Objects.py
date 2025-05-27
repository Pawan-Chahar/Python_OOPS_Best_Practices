from loguru import logger


first_name = "Manish"
Last_name = "Kumar"
salary = 50000
age = 28
height = 165

# def save_user_email_to_db(first_name, last_name, salary , age, height= None):
#     pass


class User:
    def __init__(self, ip, phone_details, location=None):
        self.ip = ip
        self.phone_details = phone_details
        self.location = location
        # self.db = save_user_email_to_db()

    def signup(self):
        pass

    def login(self):
        pass

    def profile_update(self):
        pass


user1 = User("10.123.1.10", "Samsung/Android")

logger.info(f"{user1}")

logger.info(f"{user1.__dict__}")

user2 = User("10.123.1.12", "Iphone 16/ios", "Bangalore")

logger.info(f"{user2}")

logger.info(f"{user2.__dict__}")
