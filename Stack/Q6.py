# https://neetcode.io/problems/car-fleet

# Car Fleet
# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.

# Example 1:

# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

# Constraints:

# n == position.length == speed.length.
# 1 <= n <= 1000
# 0 < target <= 1000
# 0 < speed[i] <= 100
# 0 <= position[i] < target
# All the values of position are unique.

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(position[i], speed[i]) for i in range(len(position))]
        pos_speed = sorted(pos_speed, key=lambda x: x[0], reverse=True)
        stack = []
        for car in pos_speed:
            if stack == []:
                stack.append(car)
            else:
                prev_car = stack[-1]
                if ((target-prev_car[0]) / prev_car[1]) >= ((target-car[0]) / car[1]): # collide
                    pass # ignore car behind as it arrives in same fleet
                else:
                    stack.append(car) # no collision, so new fleet
        return len(stack)


print(Solution().carFleet(target = 10, position = [1,4], speed = [3,2]))
print(Solution().carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))