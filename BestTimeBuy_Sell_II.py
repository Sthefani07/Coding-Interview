def maxGold(potions):
    gold = 0 # Start with 0 gold

    # Go through each day's price / Starting from day 1
    for i in range(1, len(potions)):

        # If today's price is higher than yesterday, we make a trade!
        if potions[i] > potions[i - 1]:

            # Buy at yesterday's price and sell at today's price
            gold += potions[i] - potions[i - 1]
    return gold    
    


    
# Exemplos for a diferent days:
potions = [10, 2, 8, 4, 12, 6]
print('Max Gold:', maxGold(potions))
print("---------------------")

potions = [3, 5, 7, 9, 11]
print("Max Gold:", maxGold(potions))
print("---------------------")

potions = [15, 10, 5, 3, 1]
print('Max Gold:', maxGold(potions))
