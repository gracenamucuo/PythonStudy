#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#二分查找 基于一个有序数组
def binary_search(list,item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) / 2
        mid = int(mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
        return  None
print(binary_search([1,4,56,67],5))

#快排
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + pivot + quicksort(greater)

print(quicksort([1,4,5,23,3]))

#狄克斯特拉算法

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["a"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"]=3
graph["b"]["fin"] = 5
graph["fin"] = {}
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed = []
def find_lowest_cost_node(costs):
    lowest_cost = fladt("inf")
    lowest_cost_node = None
    for node in  costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

#贪婪算法













































