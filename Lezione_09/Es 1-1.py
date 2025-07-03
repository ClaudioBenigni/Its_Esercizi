import re 

text:int = "169487103294"
result= re.match(r'[0-9]+', text)
print(result)