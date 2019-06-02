#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import operator
import re
from re import sub
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from os import listdir
from os.path import isfile, join

r = "Mühendislik Fakültesi - Makine Mühendisliği Bölümü Ar Gör Kadrosu Nihai Değerlendirme Sonuçları Mühendislik Fakültesi Makine Mühendisliği Bölümü Ar Gör Kadrosu Nihai Değerlendirme Sonuçlarını PDF olarak görüntülemek için tıklayınız"
totalcosine = 0.0
dictcosine =	{}

UserStringArray=[] # dosyalardaki tüm line'ları tutuyor.
Users=[] # j dediğimiz user'ları tutuyor.
similarity=[]

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
print(Users)

#for x in range(len(Users)):
#    similarity.append(get_cosine_sim(UserStringArray[i], UserStringArray[x]))
for x in range(len(Users)):
    similarity.append(get_cosine_sim(r, UserStringArray[x]))

print(similarity)
df = pd.DataFrame(similarity)
df.to_csv('/Users/mertyenilmez/Desktop/senior/AdvertisementSimilarity.csv', index=False)
