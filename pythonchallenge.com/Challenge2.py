# http://www.pythonchallenge.com/pc/def/map.html
import string

str = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
alphabetList = list(string.ascii_lowercase)
result = ""

# Method 1

# get index of g
# reduce the index by 2
# get the value for the reduced index
for char in str:
    # print(char)
    if char in alphabetList:
        index = alphabetList.index(char)
        if (index + 3) <= alphabetList.__len__():
            result = result + alphabetList[index + 2]
        else:
            result = result + alphabetList[- index + 2]
    else:
        result = result + char

print(result)

# Method 2
transtab = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
# str = 'now apply on the url'
print(str.translate(transtab))
