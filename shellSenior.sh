#!/bin/bash
python3 /Users/mertyenilmez/Desktop/senior/TweetCorpusForCorpusDataFolder.py

python3 /Users/mertyenilmez/Desktop/senior/TweetCorpusForKelimeFolder.py

cat /Users/mertyenilmez/Desktop/senior/KelimeData/* > /Users/mertyenilmez/Desktop/senior/kelimeDataBirleşik.txt

python3 /Users/mertyenilmez/Desktop/senior/fromKelimeDataBilesiktoDictionary.py

python3 /Users/mertyenilmez/Desktop/senior/cosineBetweenUserToAdv.py

sed -i '' 1d /Users/mertyenilmez/Desktop/senior/AdvertisementSimilarity.csv

python3 /Users/mertyenilmez/Desktop/senior/MatrixFromKelimeData.py

sed -i '' 1d /Users/mertyenilmez/Desktop/senior/similarityMatrix.csv

python3 /Users/mertyenilmez/Desktop/senior/CosineFromMatrix.py

sed -i '' 1d /Users/mertyenilmez/Desktop/senior/ZippedSimilarityUserAdvertisementClusters.csv

ruby -rcsv -e 'puts CSV.parse(STDIN).transpose.map &:to_csv' < /Users/mertyenilmez/Desktop/senior/ZippedSimilarityUserAdvertisementClusters.csv > /Users/mertyenilmez/Desktop/senior/transpose.csv






