from string import ascii_letters
from collections import defaultdict

filenames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

def extract_words(filename):
    f = open(filename + '.txt', 'r')
    text = f.read()
    newtext = ''
    for i in text:
        if i in ascii_letters + ' \n\t':
            newtext += i
    newtext = newtext.lower().split()
    d = defaultdict(int)
    for word in newtext:
        d[word] += 1
    return d

# Higher score, higher similarity
def compute_similarity(wdict1, wdict2):
    s = 0
    for k in wdict1:
        if k in wdict2:
            s += 1#. / wdict2[k]
    return s

def match():
    words = {n: extract_words(n) for n in filenames}
    pairs = ''
    for name in filenames[:]:
        if name in filenames:
            filenames.remove(name)
            distancelist = [(n, compute_similarity(words[name], words[n]))
                            for n in filenames]
            # print sorted(distancelist, key = lambda x: x[1])
            chosen, _ = max(distancelist, key = lambda x: x[1])
            filenames.remove(chosen)
            pairs += "{0}.txt,{1}.txt\n".format(name, chosen)
    print pairs