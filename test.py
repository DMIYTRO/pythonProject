import re


# read a text file

file = open('!_9100-2.txt', 'r', encoding="utf-8")
text = file.read()
file.close()

# find a number using regex
pattern = re.compile(r'[-(]\d+-\d+')
numbers = pattern.findall(text)


# write those numbers into a list
numbers_list = []
for number in numbers:
    numbers_list.append(str(number))


def find_repeats(numbers_list):
    """find repeats in a list and print them"""
    import collections
    numbers_dict = collections.Counter(numbers_list)
    for key, value in numbers_dict.items():
        if value > 1:
            print(key, value)
    return numbers_dict

oak = find_repeats(numbers_list)

'''new file txt to oak.txt'''
file = open('oak.txt', 'w', encoding="utf-8")
file.write(str(oak))
file.close()

