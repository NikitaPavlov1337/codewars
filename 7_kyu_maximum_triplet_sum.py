# # Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .
# Notes :
# Array/list size is at least 3 .
# Array/list numbers could be a mixture of positives , negatives and zeros .
# Repetition of numbers in the array/list could occur , So (duplications are not included when summing).

# 1- maxTriSum ({3,2,6,8,2,3}) ==> return (17)

def max_tri_sum(numbers):
    unique = list(set(numbers))
    unique.sort()
    print(unique)
    return sum(unique[-3::])

#
print(max_tri_sum([3,2,6,8,2,3]))


#BEST PRATIC

# def max_tri_sum(numbers):
#     return sum(sorted(set(numbers))[-3:])