# Given a string made up of letters a, b, and/or c,
# switch the position of letters a and b (change a to b and vice versa).
# Leave any incidence of c untouched.

# Example:

# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(string):
    #your code here
    result = ''
    for letter in string:
        if letter == 'a':
            letter = 'b'
        elif letter == 'b':
            letter = 'a'
        result += letter
    return result

print(switcheroo("abc")) # "bac"

print(switcheroo('aaabcccbaaa')) #'bbbacccabbb'
print(switcheroo('ccccc')) #'ccccc'