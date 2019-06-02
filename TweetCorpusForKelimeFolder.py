# -*- coding: utf-8 -*-

import re
from re import sub
from io import open
from os.path import isfile, join
from os import listdir

lineSplit=[] # line'ı kelimelere böldüğümüz zaman o seferlik line'ın kelimelerini tutuyor.
dictionaryArray=[] # line'ı kelimelere böldüğümüzdeki çıkan tüm kelimeleri dictionary için tutuyor.
str1 =""
# klasördeki tüm user dosyalarını tek tek tarasın diye onlyfiles listesine atıyor.
# klasördeki tüm user dosyalarını tek tek tarasın diye onlyfiles listesine atıyor.
onlyfiles = [f for f in listdir("/Users/mertyenilmez/Desktop/senior/CorpusData") if isfile(join("/Users/mertyenilmez/Desktop/senior/CorpusData", f))]


# tek tek tarama işlemi başlıyor.
for i in onlyfiles:
    with open("/Users/mertyenilmez/Desktop/senior/CorpusData/"+i, encoding='utf-8',errors="ignore") as f:

        delete_list = ["<t=T>", "<t=RT>", "</t>", "@", "#"]
        for line in f:
            for word in delete_list:
                line = line.replace(word, "")
                print(line)
#        temp = f.read().replace("<t=T>", "")
#        temp = f.read().replace("<t=RT>", "")
#        temp = f.read().replace("</t>", "")



            with open('/Users/mertyenilmez/Desktop/senior/KelimeData/'+i, 'a') as the_file:
                the_file.write(line)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
