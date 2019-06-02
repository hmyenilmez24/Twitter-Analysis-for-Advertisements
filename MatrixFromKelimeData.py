#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import operator
import re
from re import sub
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from os.path import isfile, join
from os import listdir
import numpy as np
import matplotlib.pylab as plt
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

UserStringArray=[] # dosyalardaki tüm line'ları tutuyor.
Users=[] # j dediğimiz user'ları tutuyor.

# cosine distance ile ilgili methodlar
def get_cosine_sim(*strs):
    '''from two strings, get cosine score
    example: get_cosine_sim("John Smith", "John T. Smith")'''
    vectors = [t for t in get_vectors(*strs)]
    return round(cosine_similarity(vectors)[0][1],8)

def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(analyzer = "word",
                                 tokenizer = None,
                                 preprocessor = None,
                                 stop_words = None,
                                 max_features = 5000,
                                 lowercase=True,
                                 token_pattern = r"(?u)\b\w+\b")
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()

# klasördeki tüm user dosyalarını tek tek tarasın diye onlyfiles listesine atıyor.
onlyfiles = [f for f in listdir("/Users/mertyenilmez/Desktop/senior/KelimeData") if isfile(join("/Users/mertyenilmez/Desktop/senior/KelimeData", f))]

# tek tek tarama işlemi başlıyor.
for j in onlyfiles:
    
    # user dosyalarının sadece kelime hallerini teker teker açıyor.
    with open("/Users/mertyenilmez/Desktop/senior/KelimeData/"+j, encoding='utf-8',errors="ignore") as f:
        UserStringArray.append(str(f.read()))
        Users.append(j)



#print (get_cosine_sim(UserStringArray[0], UserStringArray[1]))
#print (Users[1], UserStringArray[1])
print ("******************************")
# Similarity Matrix'ini dolduruyor.
i=0
Matrix = np.zeros((len(Users),len(Users)))
similarity=[]
for y in range(len(Users)):
    similarity[:] = []
    for x in range(len(Users)):
        similarity.append(get_cosine_sim(UserStringArray[i], UserStringArray[x]))
    i=i+1
    Matrix[y:y+1] = np.array(similarity)
print (Matrix)
print ("******************************")
df = pd.DataFrame(Matrix)
df.to_csv('/Users/mertyenilmez/Desktop/senior/similarityMatrix.csv', index=False)
print ("******************************")

for x in range(len(Users)):
    print(Users[0],Users[x],get_cosine_sim(UserStringArray[0], UserStringArray[x]))
for x in range(len(Users)):
    print(x,' ',Users[x])


with open('/Users/mertyenilmez/Desktop/senior/similarityMatrix.txt', 'a') as the_file:
    for x in range(len(Users)):
        the_file.write(str(x) +' '+ str(Users[x]) +'\n')


