f = open('dict/words.csv', 'r')

easyWords = {}
mediumWords = {}
hardWords = {}
count = 0
for line in f:
    line = line.strip().split(';')
    if 'SPLITWORD' in line[0]:
        count += 1
        continue
    if count == 1:
        easyWords[line[0]] = [line[1].strip(), line[2]]
    elif count == 2:
        mediumWords[line[0]] = [line[1].strip(), line[2]]
    elif count == 3:
        hardWords[line[0]] = [line[1].strip(), line[2]]
    else:
        pass

# print(easyWords)
# print(mediumWords)
# print(hardWords)

# for i in list(easyWords.keys()):
#     print(i)
