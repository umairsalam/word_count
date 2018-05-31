from collections import Counter


# find the most common words in a text
# take care if punctuation and upper/lower case

def create(t):
    t = dict(Counter(t.replace(',', '').replace('.', '').lower().split()))
    return t


def eliminate(t):
    selectedKeys = list()
    for (key, value) in t.items():
        if len(key) < 4:
            selectedKeys.append(key)

    for key in selectedKeys:
        if key in t:
            del t[key]
    s = t
    return s

def findstopwords(t):
   # t = dict(Counter(t.replace(',', '').replace('.', '').lower().split()))
    stopwords = dict(Counter(t.replace(',', '').replace('.', '').lower().split()))
    return stopwords

def eliminatestopwords(sw):
    selectedKeys = list()
    for (key, value) in sw.items():
        if len(key) < 4:
            selectedKeys.append(key)

    for key in selectedKeys:
        if key in sw:
            del sw[key]
    s = sw
    return s

def readFile():
    textfile=open('/Users/umairsalam/Desktop/Python/word_cloud/98-0.txt')
    doctext = textfile.read()
    # for line in duafile:
    #     print(line)
    return doctext
    textfile.close()

def readStopfile():
    stopfile=open('/Users/umairsalam/Desktop/Python/word_cloud/stopwords.txt')
    stoptext = stopfile.read()
    # print("\n\n----stop words lines----\n\n")
    # for line in stopfile:
    #     print(line)
    return stoptext
    stopfile.close()

#v = "The string module contains a number of useful constants and classes, as well as some deprecated legacy functions that are also available as methods on strings. In addition, Python’s built-in string classes support the sequence type methods described in the Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange section, and also the string-specific methods described in the String Methodssection. To output formatted strings use template strings or the % operator described in the String Formatting Operationssection. Also, see the re module for string functions based on regular expressions."

t = create(readFile())

sw = findstopwords(readStopfile())

y = Counter(sw)
mc = y.most_common(10000)
print("\n\n----stop words----\n\n")
print(mc)

newu = eliminatestopwords(sw)
y = Counter(newu)
print("\n\n----3nd last one-----\n\n")
mc = y.most_common(4)

# the three most common words
x = Counter(t)
mc = x.most_common(10)
print("\n\n----2nd last one-----\n\n")
print(mc)

# most common words with > 3 letters
u = eliminate(t)
x = Counter(u)
mc = x.most_common(4)
print("\n\n-----last one----\n\n")
print(mc)