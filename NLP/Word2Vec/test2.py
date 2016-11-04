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
    s = "3. hello 4. hi 6. nah 11. hooo 3. a"
    b = re.split('(\d+\.)',text)
    
    for i in range(len(b)):
        if re.match("\d+", b[i]):
            num = re.findall("\d+", b[i])[0]  
            txt = b[i+1]
            if(num in qa.keys()):
                qa[num] = qa[num] + txt
            else:
                qa [num] = txt
                #print(num)
                #print(txt)
    print(qa["54"])
           

            
   # print(text)