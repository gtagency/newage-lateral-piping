#Regex
import re
with  open("analogy.txt") as f:
    text = f.read()
    p = re.compile('\d+')
    