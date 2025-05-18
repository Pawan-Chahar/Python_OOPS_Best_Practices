from loguru import logger

labour_with_cost = {'Mahesh' : 500 , "Mithilesh" :400 , "Ramesh" : 400 , "Sumesh" : 300}


# Dictionary Comprehension 


labour_with_cost = {key : labour_with_cost.get(key)+ 100 
                    for key in labour_with_cost}

print(labour_with_cost)


labour_with_cost = {key : labour_with_cost.get(key)+ 100 if key!= "Sumesh"
                    else labour_with_cost.get(key)
                    for key in labour_with_cost}

name = "Manas"
letter_count = {}

for char in name :
    if char in name:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
        print(letter_count)

print(len(labour_with_cost))