string="sv#2306SV"
pwd=''
for letter in string:
    pwd+=chr(ord(letter)+1)
print(pwd,file=open("pwd.txt","w"))
with open("pwd.txt","r") as source:
    test = source.read()
    print(test)
    print(pwd==test[:-1])
