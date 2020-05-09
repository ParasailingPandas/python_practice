# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Examples
# - hotSinglesInYourArea([0,0,1,1,4,4,5,7,6,7,5]) -> returns 6
# - hotSinglesInYourArea([56,78,43,56,43]) -> returns 78
# - hotSinglesInYourArea([0,9,0,9]) -> returns "None"

#No sorting 
def hotSinglesInYourArea(list1):
    for a in list1:
        count_a = list1.index(a)
        count_b = count_a + 1
        for b in range(count_b,len(list1)): 
            if a == list1[b] and list1.index(a) != b:
                break
            elif b == len(list1) - 1:
                return a 

print(hotSinglesInYourArea([0,0,1,1,4,4,5,7,6,7,5]))
print(hotSinglesInYourArea([56,78,43,56,43]))
print(hotSinglesInYourArea([0,9,0,9]))