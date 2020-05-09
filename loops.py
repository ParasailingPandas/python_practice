list1 = [1,2,3,4,5,6,7,8,8]
butt = 8

for val in list1:
    if val == butt:
        print(val)
        
list1 = [4,5,6,7]
print("method 1:")
for val in list1:
    print(val)

print("method 2:")
for i in range(2,len(list1)):
    print(list1[i])

range(4)