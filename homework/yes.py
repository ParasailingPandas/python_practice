list1 = [0, 2, 4]
list2 = [1, 3, 5]

list1.append(list2[0])
list1.append(list2[1])
list1.append(list2[2])
print(list1)

# list1.sort()
# print(list1)

for spot1 in list1:
    for spot2 in list1:
        for spot3 in list1:
            for spot4 in list1:
                for spot5 in list1:
                    for spot6 in list1:
                        if spot1 < spot2 < spot3 < spot4 < spot5 < spot6: 
                            mergedlist = [spot1, spot2, spot3, spot4, spot5, spot6]
                            print(mergedlist)