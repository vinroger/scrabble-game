f = open('dict/words.csv', 'r')
arrayWords = [[] for i in range(3)]
dictWords = {}
count = -1
for line in f:
    line = line.strip().split(';')
    if 'SPLITWORD' in line[0]:
        count += 1
        continue
    dictWords[line[0]] = 0
    arrayWords[count].append([line[0], line[1], line[2]])

print(arrayWords)
print("\n \n \n \n \n \n \n \n \n \n \n \n")
print(dictWords)
