import pickle
import numpy as np
with open('badlist.txt') as fp:
    
    line=fp.readline()
    line=line.lower()
    line = line[0:-1]
    c=ord(line[0:1])
    vocab=[]
    for i in range (26):
            vocab.append([])
	
    #print(str(c-97))
    vocab[c-97].append(line)
    #print('h') 
    while True:
        line=fp.readline()
        line = line.lower() 
        line = line[0:-1]
        #print(line)
        #break
        if not line:
                break
        elif line!='\n':
                
                m=ord(line[0:1])
        #print('m')
                if m!=c :
            
                    c=m
            
                    #print(str(c-97))
            
                vocab[c-97].append(line)
        

np.save('bad',vocab)


with open('goodlist.txt') as fp:
    
    line=fp.readline()
    line=line.lower()
    line = line[0:-1]
    c=ord(line[0:1])
    vocab=[]
    for i in range (26):
            vocab.append([])
	
    #print(str(c-97))
    vocab[c-97].append(line)
    #print('h') 
    while True:
        line=fp.readline()
        line = line.lower()
        line = line[0:-1]
        if not line:
                break
        elif line!='\n':
                
                m=ord(line[0:1])
        #print('m')
                if m!=c :
            
                    c=m
            
                    #print(str(c-97))
            
                vocab[c-97].append(line)
        

np.save('good',vocab)
    

        
            
with open('spplist.txt') as fp:
    
    line=fp.readline()
    line=line.lower()
    line = line[0:-1]
    c=ord(line[0:1])
    vocab=[]
    for i in range (26):
            vocab.append([])
	
    #print(str(c-97))
    vocab[c-97].append(line)
    #print('h') 
    while True:
        line=fp.readline()
        line=line.lower()
        line = line[0:-1]
        #print(line)
        if not line:
                break
        elif line!='\n':
                
                m=ord(line[0:1])
        #print('m')
                if m!=c :
            
                    c=m
            
                    #print(str(c-97))
            
                vocab[c-97].append(line)
        

np.save('spp',vocab)            
        
        

with open('tpplist.txt') as fp:
    
    line=fp.readline()
    line=line.lower()
    line = line[0:-1]
    c=ord(line[0:1])
    vocab=[]
    for i in range (26):
            vocab.append([])
	
    #print(str(c-97))
    vocab[c-97].append(line)
    #print('h') 
    while True:
        line=fp.readline()
        line = line.lower()
        line = line[0:-1]
        #print(line)
        #break
        if not line:
                break
        elif line!='\n':
                
                m=ord(line[0:1])
        #print('m')
                if m!=c :
            
                    c=m
            
                    #print(str(c-97))
            
                vocab[c-97].append(line)
        

np.save('tpp',vocab)
