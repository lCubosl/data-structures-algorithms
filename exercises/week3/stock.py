# You are given the price of a stock during a period of n days. You can buy the stock on any day and sell 
# the stock on the same day or any later day.

# Your task is to compute for each day the highest profit you could have achieved by selling the stock on 
# that day.

# For example, when the prices are [3,2,3,5,1,4], the desired answer is the list [0,0,1,3,0,3]. For 
# example, on the fourth day the maximum profit is 3, because you could have bought the stock at the 
# price 2 and sold it at the price 5.

# In a file stock.py, implement the function find_profits that takes a list of prices as a parameter, and 
# returns the list of profits.

# You must implement an efficient solution with a time complexity O(n). For example, you cannot afford to 
# go through all possible buying days for each selling day. Your solution should determine each profit 
# more efficiently.

# In the last test case of the following code template, the stock prices are [1,2,\dots,10^5]. Your 
# function should finish quickly in this test case too.

def find_profits(prices):
  n = len(prices)
  list = []
  
  if n == 0:
    return list
  
  min_price = prices[0]

  for num in range(n):
    min_price = min(min_price, prices[num])
    profit = prices[num] - min_price
    list.append(profit)
  
  return list

# print
print(find_profits([1, 2, 3, 4])) # [0, 1, 2, 3]
print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
print(find_profits([1, 1, 1, 1])) # [0, 0, 0, 0]
print(find_profits([2, 4, 1, 3])) # [0, 2, 0, 2]
print(find_profits([1, 1, 5, 1])) # [0, 0, 4, 0]
print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 1, 3, 0, 3]

prices = list(range(1, 10**5+1))
print(find_profits(prices)[:5]) # [0, 1, 2, 3, 4]