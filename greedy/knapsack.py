# Item     Weight Value   Unit value
# 1	        10	   60	    6
# 2	        20	   100	    5
# 3	        30	   120	    4
# Knapsack capacity W=50
# idea: sort out based on unitvalue from high to low
class item:
    def __init__(self,index,weight,value):
        self.index = index
        self.weight = weight
        self.value = value
        self.unitvalue = value/weight
def knapsack(items,capacity):
    items.sort(key = lambda x:x.unitvalue,reverse = True) # sort out based on unit value
    tvalue = 0
    tweight = 0
    contents = []
    for item in items: # one by one
        if item.weight<=capacity:
            tvalue += item.value
            tweight += item.weight
            capacity -= item.weight
            contents.append((item.index,item.weight,item.value))
        else:
            f = capacity/item.weight
            tvalue+= item.unitvalue * capacity
            tweight+= capacity
            contents.append((item.index,capacity,item.unitvalue*capacity))
            break
    return tvalue,tweight,contents

# testing
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

# for i in range(len(weights)):
#     items = [item(i+1,weights[i],values[i])]
# bug: define items each loop, we need to create an empty list and append
items = []
for i in range(len(weights)):
    items.append(item(i+1, weights[i], values[i]))

tvalue,tweight,contents = knapsack(items,capacity)
print(f"Maximum value in knapsack: {tvalue}")
print(f"Total weight in knapsack: {tweight}")
print("Knapsack contains the following items:")
for index, weight, value in contents:
    print(f"  Item {index}: weight = {weight}, value = {value}")