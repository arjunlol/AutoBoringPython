
def commaList(listValues):
    spam = ''
    for i in range(len(listValues)-1):
        spam += str(listValues[i]) + ', '
    spam += 'and ' + str(listValues[len(listValues)-1])
    print(spam)

tipTop = ['apples','bananas','tofu','cats']
commaList(tipTop)
print(tipTop)
