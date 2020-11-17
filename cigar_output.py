#!/usr/bin/python
# -*- coding : utf-8 -*-

import sys, re

cigar = input(str("Entrer une valeur de cigar :"))
# exemple cigar 3M1I3M1D5M
# autre exemple 312M41I38M1D669M

ext = re.findall('\w',cigar) # re fonction, donne une liste chaque éléments individualisés
#print (ext)

value=[]
key=[]
val=""

for i in range (0,len(ext)) :
    if (ext[i]=='M' or ext[i]=='D' or ext[i]=='I' or ext[i]=='S' or ext[i]=='H' 
                    or ext[i]=="=" or ext[i]=='X'or ext[i]=='N'or ext[i]=='P') :
        key.append(ext[i])
        value.append(val)
        val=""
    else :
        val=""+val+ext[i]

value = [int(i) for i in value]

print (key)     # = ['M',...]
print (value)   # = [3, ...]

#for i in range (0, len(key)):
    #print (value[i],key[i])

dico={k:v for k,v in zip(key,value)}

print(len(key))
dico2={}
n=0
for i in key:
    if i not in dico2.keys():
        dico2[key[i]]=value[n]
    else:
        dico2[key[i]]+=value[n]
n=+1


print (dico)
print (dico2)

