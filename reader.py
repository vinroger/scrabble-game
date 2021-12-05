f = open('dict/words.csv', 'r')

easyWords = {}
mediumWords = {}
hardWords = {}
asianWords = {}
count = 0
for line in f:
    line = line.strip().split(',')
    if 'SPLITWORD' in line[0]:
        count += 1
        continue
    if count == 1:
        easyWords[line[0].replace(" ", "")] = [line[1], line[2]]
    elif count == 2:
        mediumWords[line[0].replace(" ", "")] = [line[1], line[2]]
    elif count == 3:
        hardWords[line[0].replace(" ", "")] = [line[1], line[2]]
    elif count == 4:
        asianWords[line[0].replace(" ", "")] = [line[1], line[2]]
    else:
        pass

list_question = []
list_description = []
list_category = []
f = open('difficulty.txt', 'r')
difficulty = f.read()
f.close()
dictUsed = {}
if difficulty == "easy":
    dictUsed = easyWords
elif difficulty == "medium":
    dictUsed = mediumWords
elif difficulty == "hard":
    dictUsed = hardWords
elif difficulty == "asian":
    dictUsed = asianWords
else:
    dictUsed = easyWords
for i in list(dictUsed.keys()):
    list_question.append(i)
for i in list(dictUsed.values()):
    list_description.append(i[0])
    list_category.append(i[1])
