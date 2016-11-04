#Regex
import re,io
# python doesnt like the files encoding
with  io.open("501analogies.txt", encoding='utf-8') as f:
    text = f.read()
    # formatting text
    text = text.replace("\n"," ")
    text = text.replace("501"," ")
    text = text.replace("Word"," ")
    text = text.replace("Analogy"," ")
    text = text.replace("Questions"," ")
    #creating a regex for non relevent numbers (ones without a .)
    p = re.compile('\d+\s+')
    # taking out all non relevent numbers
    text = re.sub(p, "", text)
    qa = {}
    #splitting on question/answer number
    b = re.split('(\d+\.)',text)
    #goes through the split string
    for i in range(len(b)):
        # if there is a relevent number (question or answer number)
        if re.match("\d+", b[i]):
            #get the number found
            num = re.findall("\d+", b[i])[0]  
            #get the question or answers text
            txt = b[i+1]
            # if the question is in the dictionary, append the answer to the question
            if(num in qa.keys()):
                
                txt2 = re.findall("[a-zA-Z]+\.",txt)
                if len(txt2) > 0:
                    qa[num] = qa[num] + txt2[0]
            else:
                #otherwise key = num, value = text
                
                qa [num] = txt
    #test       
    print(qa["54"])
