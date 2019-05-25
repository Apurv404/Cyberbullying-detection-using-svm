# Cyberbullying-detection-using-SVM
In this project, I have to classify the bullying and non-bullying comments. I have used the dataset of Wikipedia blog post having binary labels. If a comment is bullying the label will be 1 else 0.

# Preprocessing
In this stage, I have to remove brackets, resolve contractions and also have to remove stop words. I am using first and third person pronoun as features hence some traditional stop words will be useful in feature creation hence I had to create my own stop words list.  

# FEATURE EXTRACTION
For the extraction of features, TFIDF is used. TFIDF vectorizer will create its own dictionary and each word in the dictionary will be given a TFIDF value. I am also using static dictionaries for bad words, good words, second-person pronoun, and third-person pronoun. I am going through each and every word of comment and keeping the summation of TFIDF values of each type of word (bad, good, second-person pronoun and third-person pronoun).In this way, features for each comment are created.
I have used bad word value, good word value, third-person pronoun value, second-person pronoun value, good word count, bad word count, tpp count,spp count as features.

# Classification
The SVM classifier is used for classification. Feature vectors are sent to SVM with 80-20 test-train ratio.

*prj.py* preprocessing and feature extraction.
*svm.py* implements SVC.
*con_dict.py* is used to create list of bad,good,tpp,spp words.
Accuracy=92.98%
Precision=79.2
Recall=52.2
F1 measure=63.7

Link for Wikipedia dataset
https://figshare.com/articles/Wikipedia_Talk_Labels_Personal_Attacks/4054689
