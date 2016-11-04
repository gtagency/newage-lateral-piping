#Regex
import re,io
with  io.open("501analogies.txt", encoding='utf-8') as f:
  
    text = f.read()
    
    text = text.replace("\n"," ")
    text = text.replace("501"," ")
    text = text.replace("Word"," ")
    text = text.replace("Analogy"," ")
    text = text.replace("Questions"," ")
    p = re.compile('\d+\s+')
    text = re.sub(p, "", text)
    qa = {}
    s = "3. hello 4. hi 6. nah"
    text = re.split('\d+\.',text)
    print(text)