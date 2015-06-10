import codecs,sys
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

f1 = codecs.open(sys.argv[1], encoding='utf-8', mode='r')
f2 = codecs.open(sys.argv[2], encoding='utf-8', mode='r')

y_true = []
y_pred = []

for line in f1:
    y_true.append(line.strip())

for line in f2:
    y_pred.append(line.strip())


print accuracy_score(y_true, y_pred, normalize=False)
print accuracy_score(y_true, y_pred)
print confusion_matrix(y_true, y_pred)
print(classification_report(y_true, y_pred))