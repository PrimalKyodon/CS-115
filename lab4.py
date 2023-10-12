####################################################################
#       Name: Aaren Patel
#       Date: 10/6/22
#       CS115 Lab 4
#       I pledge my honor that I have abided by the Stevens Honor System.
#
####################################################################

def knapsack(capacity, itemList):
        '''outputs the maximum value of the knapsack filled with items from itemList without going over the capcity'''
        if itemList == []:
                return [0, []]
        if itemList[0][0]>capacity:
                return knapsack(capacity, itemList[1:])
        use = knapsack(capacity-itemList[0][0], itemList[1:])
        use[0] = itemList[0][1] + use[0]
        use[1] = [itemList[0]] + use[1]
        lose = knapsack(capacity, itemList[1:])
        if use[0] > lose[0]:
                return use
        return lose
