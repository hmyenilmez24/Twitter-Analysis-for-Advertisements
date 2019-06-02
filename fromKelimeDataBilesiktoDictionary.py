# -*- coding: utf-8 -*-

import re
from re import sub
import linecache
import json
import itertools

userList=[] # user'ları tutuyor.
dictionary={} # her kelimeye ayrı id vericek şekilde kelimeleri tutuyor
lineSplit=[] # line'ı kelimelere böldüğümüz zaman o seferlik line'ın kelimelerini tutuyor.
dictionaryArray=[] # line'ı kelimelere böldüğümüzdeki çıkan tüm kelimeleri dictionary için tutuyor.


# line'ı sadece tweetleri alıcak şekle getiriyor.
f = open("/Users/mertyenilmez/Desktop/senior/kelimeDataBirleşik.txt", encoding="utf-8")
for line in f:

    if (line[:8] == '<USERID>'):
        line = line[:0]

# line'daki # ve @ ile başlamayan tüm kelimeleri ayırıp array'e ekliyor atıyor.
    lineSplit = line.split()
    for i in lineSplit:
        if not i in dictionaryArray:
            dictionaryArray.append(i)

# array'i dictionary'e ekliyor
for i in range (len(dictionaryArray)):
    dictionary[i] = dictionaryArray[i]

# dictionary'i exampleDictionary.txt dosyasına yazdırıyor.
with open('/Users/mertyenilmez/Desktop/senior/exampleDictionary.txt', 'w', encoding='utf-8') as f:
    f.write(json.dumps(dictionary, ensure_ascii=False))

