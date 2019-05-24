# http://www.pythonchallenge.com/pc/def/map.html
import string

str = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
alphabetList = list(string.ascii_lowercase)
alphabetDict = {}
i = 0
tempDict = {''}
for letter in alphabetList:
    i += 1
    key = alphabetDict[i-2]
    alphabetDict[key] = letter

for char in str:
    print(char)
