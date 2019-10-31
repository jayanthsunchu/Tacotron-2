import json
import os
import csv
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

with open('feed.json') as fr: 
  data = json.load(fr)
  list_of = os.listdir('/home/ubuntu/jay') 
  with open('metadata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['filename', 'text'])
    for line in data:
      if line['filename']+'.wav' in list_of:
        writer.writerow([line['filename'],transliterate(line['text'],sanscript.TELUGU,sanscript.HK)])  
