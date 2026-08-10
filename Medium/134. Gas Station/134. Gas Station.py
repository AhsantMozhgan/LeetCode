# https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # If total gas is less than total cost, we cannot complete the circuit
        if total_gas < total_cost:
            return -1
        
        current_gas = 0
        start = 0
        
        for current_station in range(len(gas)):
            current_gas += gas[current_station] - cost[current_station]
            
            # If current gas falls below 0, we cannot start from 'start'
            if current_gas < 0:
                start = current_station + 1  # Set start to the next station
                current_gas = 0  # Reset current gas balance
                
        return start


# “I’d solve the gas-station circuit problem with a single greedy pass after a quick feasibility check.

# First I compare the total gas available with the total cost. If total gas is less than total cost, it’s impossible to complete the circuit no matter where I start, so I return -1.

# If the totals work, I know a unique starting point must exist. I keep two variables: `current_gas` (the running tank balance) and `start` (the candidate starting index, initially 0).

# I walk through every station. At each one I add the net gas I gain or lose: `gas[i] - cost[i]`.  

# If the tank ever drops below zero, that means I couldn’t have reached this station from the current `start`. 
# So I discard the whole prefix and set the new candidate start to the next station, resetting the tank to zero.

# Because a solution is guaranteed to exist when total gas ≥ total cost, the final value of `start` is the unique valid starting index.

# The algorithm makes one linear pass, so it runs in O(n) time and uses only O(1) extra space.”
