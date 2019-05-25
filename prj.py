import re, string, unicodedata
import pandas as pd
import nltk
import scipy.sparse
from nltk.corpus import PlaintextCorpusReader
import contractions #converts didn't into did not
import inflect #used for generation pulrals,singulars,CONVERTING NUMBERS TO WORDS
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer
import operator
from nltk.tokenize import sent_tokenize,word_tokenize 
import pickle
import numpy as np
import csv
import time
from sklearn.cluster import KMeans


data=[]
data1=[]

comments = pd.read_csv('attack_annotated_comments.tsv',sep = '\t', index_col = 0)
annotations = pd.read_csv('attack_annotations.tsv',sep = '\t')

len(annotations['rev_id'].unique())

# labels a comment as an atack if the majority of annoatators did so
labels = annotations.groupby('rev_id')['attack'].mean() > 0.5

# join labels and comments
comments['attack'] = labels

# remove newline and tab tokens
comments['comment'] = comments['comment'].apply(lambda x: x.replace("NEWLINE_TOKEN", " "))
comments['comment'] = comments['comment'].apply(lambda x: x.replace("TAB_TOKEN", " "))


data2=comments['comment']
data=data2.tolist()
for i in range (0,len(data)):
    data[i] = data[i].lower()

data2=comments['attack']
data1=data2.tolist()

sentences = data

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)

def denoise_text(text):
    text = remove_between_square_brackets(text)
    text = replace_contractions(text)

    return text

for i in range (0,len(sentences)):
    sentences[i] = denoise_text(sentences[i])

words=[]
for i in range(0,len(sentences)):
    words.append(nltk.word_tokenize(sentences[i]))

stopWords=[ "won't", 'y', 's', 'hasn', 'how',  'not', 'up', 'won', "it's", 'its', 'no', 'most', 'shouldn', 'both', 'doesn', 'an', 'there', 'off', 'during', "should've", "hasn't", 'hadn', 'is',  'these', 'through', 'itself', 'aren', 'who', 'was', 'should', 'having', 'did', 'of', 'a', 'each', "wasn't", 'once', 'some',  "shan't",  'such', 'at', 'does', 'are', 'weren', 'their', 'then', 'which',  'had',  'own', 'ma', 'any', 'that', "isn't", 'again', 'needn', 'below', 'as', 'doing', 'for', 'further', 'whom', 'when', 'haven', "needn't", 'wouldn', 'into', "didn't", 'the', "doesn't", "mightn't", 'didn', 'just', 've', 'to', 'has', 'or', 'ours', 'about', 'on',  'wasn', 'by',  'where', 'more', "weren't", 'll', 'am', 'and', 'being', 'why', 'our',  'out', "couldn't", 'it', 'what', 'until', 're', 'other', "aren't", 'can', "haven't", 'ourselves', 'been', 'before', 'nor',  "don't", 'shan',   'over', 'above', 'while', "mustn't", 'same', 'than', 'few', "that'll", 'be',  'm', 'd', 'in', 'too' , 'will', 'isn', 'from', 'my', "you'd", 'against', 'ain', 'under', 'o', 'very', 'were', 'but', 'now', 'with', 'mightn', 'do', 'all', 'only',  'because', 'between', 'here', 'theirs',  'so', 'couldn', 't', 'if', 'have', 'mustn', 'those', "wouldn't", 'after', "hadn't", 'down', "shouldn't", 'this', 'don']

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    sentences2 =[]
    stop_words =[]
    special_char =[' ','"','.','#','@','!','%','^','&','*','(',')',',','_','-','+','{','}','[',']',':',';',"'",'|','/','>','<','?',"''","=",'""','``']
    for i in range(0,len(words)):
        sent_tokens =[]
        str1=""
        sent_tokens=(nltk.word_tokenize(words[i]))
        new_words = []
        for j in range(0,len(sent_tokens)) :
            if sent_tokens[j] not in stopWords and sent_tokens[j] not in special_char:
                new_words.append(sent_tokens[j])
            else :
                stop_words.append(sent_tokens[j])
        str1 = " ".join(str(x) for x in new_words)
        sentences2.append(str1)
    return sentences2

words=remove_stopwords(sentences)

vocabulary = set()
for doc in words:          #sentences - words
    vocabulary.update(doc.split())

vocabulary = list(vocabulary)
word_index = {w: idx for idx, w in enumerate(vocabulary)}

vect = TfidfVectorizer(vocabulary=vocabulary)
res = vect.fit_transform(words)   

vocab_bad=np.load('bad.npy')
vocab_good=np.load('good.npy')
vocab_spp=np.load('spp.npy')
vocab_tpp=np.load('tpp.npy')

mat1 = [["Bad","Good","SPP","TPP","BADC","GOODC","SPPC","TPPC","Insult"]]

for i in range (0,len(words)):
    sent3 = words[i]
    sent3 = sent3.split()
    tf=0
    badc=0
    bad_val=0
    goodc=0
    good_val=0
    sppc=0
    spp_val=0
    tppc=0
    tpp_val=0
    for wrd in sent3:
        wrd=wrd.lower()
        n=ord(wrd[0:1])
        ind = (vect.vocabulary_)[wrd]
        tf=tf+res[i,ind]
                
        if n<97 or n>122:
            continue
        search=vocab_bad[n-97]#bad list
        search1=vocab_good[n-97]
        search2=vocab_spp[n-97]
        search3=vocab_tpp[n-97]
        flag = 0
        for w in search3:
            if w==wrd:
                tppc=tppc+1
                ind = (vect.vocabulary_)[wrd]
                tpp_val=tpp_val+res[i,ind]
                flag=1
                break
        if flag != 1:
            for w in search2:
                if w==wrd:
                    sppc=sppc+1
                    ind = (vect.vocabulary_)[wrd]
                    spp_val=spp_val+res[i,ind]
                    flag=1
                    break
			

        if flag != 1:
            for w in search1:
                if w==wrd:
                    goodc=goodc+1
                    ind = (vect.vocabulary_)[wrd]
                    good_val=good_val+res[i,ind]
                    flag=1
                    break
            
        if flag != 1:
            for w in search:
                if w==wrd:
                    badc=badc+1
                    ind = (vect.vocabulary_)[wrd]
                    bad_val=bad_val+res[i,ind]
                    flag=1
                    break

    
        
    mat=[bad_val,good_val,spp_val,tpp_val,badc,goodc,sppc,tppc,data1[i]]
    mat1.append(mat)


with open('features1.tsv', 'w',newline='') as csvFile:
    writer = csv.writer(csvFile,delimiter='\t')
    writer.writerows(mat1)
    csvFile.close()
