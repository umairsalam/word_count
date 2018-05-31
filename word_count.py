import collections

# hi = 'hello' + ' world!'
#
#
# print('\n\n\n' + hi)
#
# hi2 = hi.strip('h')
# print('\n\n\n' + hi2 + '\n\n\n')
#
# sentence = "Let\'s split the words"
# print(sentence)
# splitsentence = sentence.split(' ')
# print(splitsentence)
#
# mylist = ['Umair', 'Usama', 'Sohaib', 'Hafsa', 'Noaman']
# x = mylist[3]
# print(x)
#
# mynewlist = [i**2 for i in range (1, 11)]
# print(mynewlist)
#
# myshortlist = [i for i in range (0, 6)]
# print(myshortlist)
#
# myevenlist = [i for i in range (0, 21, 2)]
# print(myevenlist)
#
# myalphadict = {i : chr(i) for i in range (65, 90)}
# print(myalphadict)


def readFile():
    duafile=open('/Users/umairsalam/Desktop/Python/word_cloud/dua.txt')
    for line in duafile:
        print(line)
    return line


def wordCount(text, word):
    splitText = text.split()
    count = 0
    for value in splitText:
        if value == word:
            count = count + 1

    print('The frequency of the word {} is {}.'.format(word, count))

# inputText = input('Input the text string: ')
# inputWord = input('What word do you want to search for?\n\n')

mytext = readFile()
wordCount(mytext, 'Allah')

