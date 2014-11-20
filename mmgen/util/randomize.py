import random
def weighted_roll(value_map):
    """
    Rolls a random value from a dict
    It should be structured like:
    {
        "spam": 200,
        "eggs": 100
    }

    In the above example, there's a 33% chance of rolling eggs and a 66% chance of rolling spam
    """
    weightsum = 0
    rollist = {}
    for choice in value_map:
        prob = value_map[choice]
        rollist[(prob + weightsum)] = choice
        weightsum += prob
    possible = sorted(rollist.keys())
    roll = random.randint(0, weightsum)
    for x in possible:
        if roll <= x:
            return rollist[x]
