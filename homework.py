# Homework 1 - print even numbers within this list 
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
print(len(numbers))
print(numbers[0:100:2])

# Homework 2 - print TRUE if 3 numbers in list can be added to produce sumval
list1 = [1,2,3,4,5,6]
sumval = 12
for spot1 in list1:
    for spot2 in list1:
        for spot3 in list1:
            if spot1 + spot2 + spot3 == sumval and spot1 != spot2 and spot1 != spot3 and spot2 != spot3: 
                print("TRUE")
            else:
                print("FALSE")
