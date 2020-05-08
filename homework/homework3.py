# Given two lists in ascending order, return a combined list also in ascending order

# Examples
# - mergeStortedLists([0,2,4],[1,3,5]) -> [0,1,2,3,4,5]
# - mergeStortedLists([-3,-2,0],[-10,0,5]) -> [-10,-3,-2,0,0,5]

# def mergeStortedLists(list1, list2):
#    list1.append(list2[0])
#    list1.append(list2[1])
#    list1.append(list2[2])
#    for spot1 in list1:
#        for spot2 in list1:
#            for spot3 in list1:
#                for spot4 in list1:
#                    for spot5 in list1:
#                        for spot6 in list1:
#                            if spot1 < spot2 < spot3 < spot4 < spot5 < spot6 or spot1 < spot2 < spot3 < spot4 <= spot5 < spot6:
#                                mergeStortedLists = [spot1, spot2, spot3, spot4, spot5, spot6]
#                                return mergeStortedLists

# print(mergeStortedLists([0,2,4],[1,3,5]))
# print(mergeStortedLists([-3,-2,0],[-10,0,5]))


def mergesortedlists(list1, list2):
    for val in list2:
        list1.append(val)
    list3 = []
    for val1 in list1:
        val1 = min(list1)
        list3.append(val1)
        list1.remove(val1)
        # for val2 in list1: 
        #     if val1 < val2: 
        #      list3.append(val1) 
    return list3 

print(mergesortedlists([0,2,4],[1,3,5]))
print(mergesortedlists([-3,-2,0],[-10,0,5]))