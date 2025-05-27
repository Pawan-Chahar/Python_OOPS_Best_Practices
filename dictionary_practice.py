from loguru import logger

labour_with_cost = {"Mahesh": 500, "Mithilesh": 400, "Ramesh": 400, "Sumesh": 300}

labour_with_cost["Jagmohan"] = 1000

logger.info(labour_with_cost)

labour_with_cost["Shyam Mohan"] = 2000

logger.info(labour_with_cost.keys())

logger.info(labour_with_cost.values())

logger.info(labour_with_cost.items())

logger.info(labour_with_cost)


for name in labour_with_cost:
    logger.info(f"{name}, {labour_with_cost[name]}")


for key, value in labour_with_cost.items():
    logger.info(f"{key} , {value}")


# get method

logger.info(labour_with_cost.get("Mahesh"))

logger.info(labour_with_cost["Mahesh"])

# Keys and values

logger.info(labour_with_cost.keys())

logger.info(labour_with_cost.values())

# Item Method

logger.info(labour_with_cost.items())


# Update Method

logger.info(labour_with_cost.update({"manish": 700, "Ram": 800}))

logger.info(labour_with_cost)

new_dict = {"Vinay": 600, "Mahendra": 900}

final_dict = {**labour_with_cost, **new_dict}

print(final_dict)


# Pop Method

logger.info(labour_with_cost.pop("Mahesh"))

logger.info(labour_with_cost.popitem())

# Copy Method

new_labour_with_cost = labour_with_cost.copy()

print(id(labour_with_cost))

print(id(new_labour_with_cost))
