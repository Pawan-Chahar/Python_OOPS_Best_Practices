name = ["manish", "ram", "Shyam"]


final_result = " "

for i in name:
    final_result = " #  ".join(name)
    # final_result = final_result +"  " + name

print(final_result)

state_dept_info = [
    {"state": "Bihar", "department": "IT"},
    {"state": "Delhi", "department": "Marketing"},
]

"""
Find out all the employee name who are available in the above condition.
you dont know exact number of filter condition which will come in the list. It can change each run.
"""
query = """
Select * from (
    Select e.employee_name , e.state , e.zip , e.salary , d.department
    from employee_tbl e 
    Inner Join department d 
    ON e.emp_id = d.emp_id 

) a 
Where salary > 100000

"""
from loguru import logger

final_result = []

for condition in state_dept_info:
    for key, value in condition.items():
        final_result.append(f"{key} = {value}")


logger.info(final_result)

result = "  OR  ".join(final_result)

logger.info(result)

logger.info(query + "  AND  ( " + result + " )")


"""

Q1. Secure the PII data.
Input = ["mverma6250@gmail.com","ramesh02@hotmail.com",
        "sohansingh@gmail.com","swatirahane@outlook.com"]

Output = ["m********0@gmail.com","r******2@hotmail.com",
        "s********h@gmail.com","s*********e@outlook.com"]

        """

Input = [
    "mverma6250@gmail.com",
    "ramesh02@hotmail.com",
    "sohansingh@gmail.com",
    "swatirahane@outlook.com",
]

# for i in Input:

my_var = "mverma6250@gmail.com"

result = my_var.split("@")

result[0]
print(result)


"""

Q2. Print the list of all unique ip addresses?

Input:- 
["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2"
]

Output:- ["10.168.155.2","10.168.156.2","10.168.151.2"
           "10.168.155.22","10.168.167.2",
           "10.168.179.28","10.168.155.31" ]
"""
