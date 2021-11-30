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
        easyWords[line[0]] = [line[1].replace(" ", ""), line[2]]
    elif count == 2:
        mediumWords[line[0]] = [line[1].replace(" ", ""), line[2]]
    elif count == 3:
        hardWords[line[0]] = [line[1].replace(" ", ""), line[2]]
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
else:
    dictUsed = easyWords
for i in list(dictUsed.keys()):
    list_question.append(i)
for i in list(dictUsed.values()):
    list_description.append(i[0])
    list_category.append(i[1])


class wordDatabase():
    def __init__(self):
        self.question = list_question
        self.description = list_description
        self.category = list_category

    def getQuestion(self):
        return self.question

    def getDescription(self):
        return self.description

    def getCategory(self):
        return self.category

    def setQuestion(self, new):
        self.question = new

    def setDescription(self, new):
        self.description = new

    def setCategory(self, new):
        self.category = new


# print(easyWords)
# print(mediumWords)
# print(hardWords)

# for i in list(easyWords.keys()):
#     print(i)
