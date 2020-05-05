list1 = []
list2 = [1, 2, 3]

print(list1)
list1.append(0)
print(list1)

list1.append(list2)
print(list1)

list1.append(5)
list1.append(6)
list1.append(7)
print(list1)

print(list1[0])
print(list1[3])
print(list1[4])

list1.append("butt")
print(list1)

print(list1[1])

# print(list1[10])

list4 = [1, 2, 3, "butt", "pancakes", "ass", "dud", "poop", "penis"]
print(list4[3:8])
print(len(list4))
print(list4[0:9:2])
print(list4[1:9:2])
print(list4.index("butt"))

# Homeworks 
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
print(len(numbers))
print(numbers[0:100:2])