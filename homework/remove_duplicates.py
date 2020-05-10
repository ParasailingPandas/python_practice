# Given a sorted array nums, remove the duplicates in-place such 
# that each element appear only once and return the new length.

# Examples
# - remove_duplicates([1,1,2,2,3,3,4,5]) -> 5
# - remove_duplicates([1,1,2,2]) -> 2

def remove_duplicates(list1):
    a = 0 
    while a < len(list1) - 1:
        b = a + 1
        
        if list1[a] == list1[b]:
            list1.remove(list1[b])

        a = a + 1
       
    return len(list1)

print(remove_duplicates([1,1,2,2,3,3,4,5]))
print(remove_duplicates([1,1,2,2]))
