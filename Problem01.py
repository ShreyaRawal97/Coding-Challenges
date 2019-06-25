"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

k = 14
list = [10, 15, 3, 7, 7]

s = set(list)
def sum_exists(list, k):
    return bool({k - i for i in list} & s)

print(sum_exists(list, k))
#the run time of this program is O(n)
