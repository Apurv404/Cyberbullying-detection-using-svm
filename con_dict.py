import numpy as np

vocab =[]
def dictionary(fileName):
        vocab.clear()
        with open(fileName) as fp:
                
                line=fp.readline()
                line=line.lower()
                line = line[0:-1]
                c=ord(line[0:1])
                for i in range (26):
                        vocab.append([])
                vocab[c-97].append(line)
                while True:
                        line=fp.readline()
                        line = line.lower() 
                        line = line[0:-1]
                        if not line:
                                break
                        elif line!='\n':
                                m=ord(line[0:1])
                                if m!=c :
                                        c=m
                                vocab[c-97].append(line)
                        

dictionary('badlist.txt')
print(vocab)
np.save('bad',vocab)

dictionary('goodlist.txt')
print(vocab)
np.save('good',vocab)

dictionary('spplist.txt')
print(vocab)
np.save('spp',vocab)

dictionary('tpplist.txt')
print(vocab)
np.save('tpp',vocab)
