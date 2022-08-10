import os

## Move into the directory where the database is.
os.chdir('C:/Users/1kupe/PycharmProjects/pythonProject/')

open_file = open('!_9100-2.txt', 'r', encoding="utf-8")
line = open_file.readline()
name = line.strip()

candidateDict = {}
print(candidateDict)


def find_duplicate():
    for name in open_file:
        if name in candidateDict:
            candidateDict[name] += 1
        else:
            candidateDict[name] = 1


find_duplicate()

for name in candidateDict:
    if candidateDict[name] > 1:
        print(name)
print(name)
open_file.close()
