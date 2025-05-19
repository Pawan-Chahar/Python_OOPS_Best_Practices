from loguru import logger 

test = (1,2,45,65,32,"True" , "Manish",True)

print(type(test))



'''
# Q : Input:- test_tuple = ([5,6], [6,7,8,9] ,[3])
#       Output:- (5,6,6,7,8,9,3)
'''

test_tuple = ([5,6], [6,7,8,9] ,[3])

#Method: 1 use first convert all iterable objects to tuple and add them empty tuple

final = tuple( )
for i in test_tuple:
    result = tuple(i)
    final =  final + result

logger.info(final)


# Method: 2 Using first append all list objects to empty list and then last convert final list to tuple
test_tuple = ([5,6], [6,7,8,9] ,[3])
empty_lst = []

for i in test_tuple:
    # print(i)
    var_lst = list(i)
    empty_lst = empty_lst + var_lst
    
logger.info(tuple(empty_lst))


''' Write a program to return a tuple which is expontetial of given two tuples as an input.
Example:-

Input:-  tuple1 = (10 ,2,3, 5)
         tuple2 = (3, 6, 4, 3)

Output:  (1000 , 64 , 81. 125)
'''
tuple1 = (10 ,2,3, 5)
tuple2 = (3, 6, 4, 3)

final = ()

for i in range(len(tuple1)):
    result = tuple1[i] ** tuple2[i]

    final = final + (result,)

print(final) 

result_lst = [ ]
for i in range(len(tuple1)):
    result_lst.append(tuple1[i] ** tuple2[i])

print(tuple(result_lst))

# for i in tuple1:
#     for j in tuple2:
#         print( i**j)

