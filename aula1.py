import re


# findall search sub
# compile

string = 'Este é um teste de expressões regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string, count=1))

regexp = re.compile(r'teste')
regexp.search(string)
regexp.findall(string)

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))