# -*- coding: utf-8 -*-

import re
from re import sub
from io import open
from os.path import isfile, join
from os import listdir

# klasördeki tüm user dosyalarını tek tek tarasın diye onlyfiles listesine atıyor.
onlyfiles = [f for f in listdir("/Users/mertyenilmez/Desktop/senior/rowData") if isfile(join("/Users/mertyenilmez/Desktop/senior/rowData", f))]

# tek tek tarama işlemi başlıyor.
for i in onlyfiles:
    with open("/Users/mertyenilmez/Desktop/senior/rowData/"+i, encoding='utf-8',errors="ignore") as f:
        contents = f.read()
        f.close()
    with open("/Users/mertyenilmez/Desktop/senior/rowData/"+i, encoding='utf-8',errors="ignore") as f:
        for line in f:
            
# Buralarda data emojilerden, linklerden, büyük harflerden taglardan vs. temizleniyor.
# ve her line '<t=RT>' + line + '</t>' şekline getiriliyor.
            if line[:1] != '<':
                line = re.split('\\bTweet number\\b',line)[-1]
                line = sub(pattern=r"\d", repl=r"", string=line)
                if line[:2] == ' :':
                    line = line[2:]
                elif line[:1] == ":":
                    line = line[1:]

        
                emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"
                u"\U0001F300-\U0001F5FF"
                u"\U0001F680-\U0001F6FF"
                u"\U0001F1E0-\U0001F1FF"
                u"\U0001F1F2-\U0001F1F4"
                u"\U0001F1E6-\U0001F1FF"
                u"\U0001F600-\U0001F64F"
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u"\U0001F1F2"
                u"\U0001F1F4"
                u"\U0001F620"
                u"\u200d"
                u"\u2640-\u2642"
                "]+", flags=re.UNICODE)
        
                line = emoji_pattern.sub(r'', line)
                
                line = re.sub(r"http\S+", '', line)
                
                line = ''.join(c for c in line if c.isalnum() or c in '@ #')
                
                line = line.lower()
                
                               
                if line[:2] == 'rt':
                    line = line[3:]
                    line = ('\n'.join(['<t=RT>' + line + '</t>']))
                elif line[:1] == '':
                    line=line
                else:
                    line = ('\n'.join(['<t=T>' + line + '</t>']))

            
            print (line)
            
# Temizlenen veriler CorpusData klasöründe herkesin adının aynı olduğu txt dosyalarına yazdırılıyor.

            with open('/Users/mertyenilmez/Desktop/senior/CorpusData/'+i, 'a') as the_file:
                the_file.write(line +'\n')

        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
