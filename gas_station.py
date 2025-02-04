def complete_circuit(gas, cost):
# Iniciate variables
    start_station= 0       # This keeps track where potentially we will start from 
    tank = 0               # Represent the current fuel balance as we travel
                       # these help determine if completing the journey is even possible
    total_gas = 0          
    total_cost= 0


#loop through all stations / I iterate through all stations using a for loop.
#I keep track of the total amount of gas available (total_gas) and the total fuel required (total_cost).
#This will help me quickly determine if a solution exists at the end.
    for i in range(len(gas)):
        total_gas += gas[i]   # Track total gas available
        total_cost += cost[i]  # Track total cost required

#Calculate/track fuel balance / At each station i, I update tank by adding the gas gained and subtracting the cost to reach the next station.
#This represents the running fuel balance as I move forward.
        tank += gas[i] - cost[i]  # Running fuel balance as we move forward 

# Restarting if fuel is insufficient / If at any point the tank goes negative, it means that I can't reach the next station from my current starting point.
#So, I update start_station = i + 1 and reset the tank to 0 because I need to try starting from the next station.
#This works because if a valid starting station exists, it must be after any station where we run out of fuel.

        if tank < 0:         # if we run out of fuel, restart from the next station
           start_station = i + 1
           tank = 0            # reset tank new start

# Ckecking if the trip is possible After the loop, I check if the total gas available is less than the total cost.
#If total_gas < total_cost, it's impossible to complete the circuit, so I return -1.

    if total_gas < total_cost:
        return -1 #no possible to complete the circuit

# Returning the Start Station / If the total gas is enough, then there must be one valid solution, and start_station will hold the correct index.
#So, I return start_station as the answer!

    return start_station
             

# Example 1
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(complete_circuit(gas, cost))  # Output: 3

# Example 2
gas = [2, 3, 4]
cost = [3, 4, 3]
print(complete_circuit(gas, cost))  # Output: -1             