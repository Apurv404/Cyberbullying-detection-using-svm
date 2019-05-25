import pandas as pd
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import precision_recall_fscore_support

bankdata = pd.read_csv("features1.tsv",sep='\t')
bankdata.shape
bankdata.head()
X = bankdata.drop('Insult',axis=1)  
y = bankdata['Insult']
  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

svclassifier = SVC(C=1.0,kernel='rbf')  
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)

print("Accuracy = ",metrics.accuracy_score(y_test,y_pred))
print(precision_recall_fscore_support(y_test, y_pred, average='binary'))
print(precision_recall_fscore_support(y_test, y_pred, average='micro'))
print(precision_recall_fscore_support(y_test, y_pred, average='macro'))
print(precision_recall_fscore_support(y_test, y_pred, average='weighted'))
