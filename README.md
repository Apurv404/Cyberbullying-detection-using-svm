# Cyberbullying-detection-using-svm
In this project we have used dataset of wikipedia blogpost having binary labels.  TFIDF is used for feature extraction and SVM as binary classifier. 
In the *prj.py* preprocessing is done and then TfidfVectorizer is used to create vectors.
bad word value,good word value,third person pronoun value,first person pronoun value,good word count,bad word count,tpp count,spp count are the features used.
*svm.py* implements SVC.
*con_dict.py* is used to create list of bad,good,tpp,spp words.
Accuracy=92.98%
Precision=79.2
Recall=52.2
F1 meature=63.7

Link for wikipedia dataset
https://figshare.com/articles/Wikipedia_Talk_Labels_Personal_Attacks/4054689
