__author__ = 'd062787'
import codecs
import sys,os

def find_lang(line):
    pos=-1
    out = []
    try:
        pos = line.index("\t")
    except (ValueError,UnboundLocalError):
        sys.stdout.write(repr(line))
    if pos != -1:
        out.append(line[(pos+1):-1])
        out.append(line[:pos])
        return out
    else:
        return " "

f1 = codecs.open("./DSLCC-v2/DSLCC-v2.1/train.txt", encoding='utf-8')
langDict = {}

for line in f1:
    res = find_lang(line)
    lang = res[0]
    sent = res[1]
    if not(langDict.has_key(lang)):
        langDict[lang] = []
    langDict[lang].append(sent)


print langDict.keys()
for i in langDict.iterkeys():
    directory = "./corpus/domain/" + i
    if not os.path.exists(directory):
        os.makedirs(directory)
    f2 = codecs.open("./corpus/domain/" + i + "/out.txt", encoding='utf-8', mode='w+')
    f2.write('\n'.join(langDict.get(i)))