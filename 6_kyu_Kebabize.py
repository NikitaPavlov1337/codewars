# Modify the kebabize function so that it converts a camel case string into a kebab case.

# kebabize('camelsHaveThreeHumps') // camels-have-three-humps
# kebabize('camelsHave3Humps') // camels-have-humps
import re

def kebabize(string):
    list1 = []
    for i in string:
        for j in i:
            if j.isalpha():
                list1.append(j)
    string = ''.join(list1)
    list2 = re.sub( r"([A-Z])", r" \1", string).split()
    string = '-'.join(list2).lower()

    return string

# print(kebabize('myCamelCasedString'))
print(kebabize('myCamelHas3Humps'))

