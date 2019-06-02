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



from scipy.cluster.hierarchy import fcluster



from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from numpy import genfromtxt

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


Matrix = genfromtxt('/Users/mertyenilmez/Desktop/senior/similarityMatrix.csv', delimiter=',')

y = pdist(Matrix)

listUserNames=[]

# agglomerative clustering
cluster = AgglomerativeClustering(affinity='euclidean', n_clusters=6, linkage='ward').fit(Matrix)
print(squareform(y))
plt.scatter(Matrix[:, 0],Matrix[:, 1], c=cluster.labels_, cmap='gist_rainbow')
#print(cluster.labels_)
listClusterInfo=cluster.labels_ #hangi cluster da oldukları bilgisi
plt.show()
#print(type(cluster.labels_))

ListsimilarityInfo = genfromtxt('/Users/mertyenilmez/Desktop/senior/AdvertisementSimilarity.csv', delimiter=',')
f = open("/Users/mertyenilmez/Desktop/senior/similarityMatrix.txt", encoding="utf-8")
for line in f:
    lineSplit = line.split()
    listUserNames.append(lineSplit[1][1:-4])
#print(listUserNames)


# listUserNames
# listClusterInfo
listClusterInfo_s, ListsimilarityInfo_s, listUserNames_s, = map(list, zip(*sorted(zip(listClusterInfo, ListsimilarityInfo, listUserNames), reverse=True)))

print(len(listClusterInfo_s))
print(len(listUserNames_s))
print(len(ListsimilarityInfo_s))

#zip(listClusterInfo, ListsimilarityInfo, listUserNames)

df = pd.DataFrame(zip(*sorted(zip(listClusterInfo, ListsimilarityInfo, listUserNames), reverse=True)))
df.to_csv('/Users/mertyenilmez/Desktop/senior/ZippedSimilarityUserAdvertisementClusters.csv', index=False)


# dendrogram
plt.figure(figsize=(8, 6))
plt.title("User Dendograms")
plt.xlabel('USERS')
plt.ylabel('SIMILARITY')
dend = shc.dendrogram(shc.linkage(Matrix, method='ward'))
plt.show()
