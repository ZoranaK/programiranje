# -*- coding: utf-8 -*-


recnik={"grub":{"sinonimi":["neblag","nasilan"],"antonimi":["nezan","blag"]},"lep":{"sinonimi":["divan","bajan"],"antonimi":["ruzan","nelep"]}, "smesan":{"sinonimi":["zanimljiv","duhovit"], "antonimi":["nesmesan","nezanimljiv"]}}

print(recnik["grub"]["sinonimi"])
print(recnik["lep"]["sinonimi"])
print(recnik["smesan"]["sinonimi"])


print(recnik["grub"]["antonimi"])
print(recnik["lep"]["antonimi"])
print(recnik["smesan"]["antonimi"])

for rec in recnik.keys():
     
     print("rec: ", rec) 
     sin = "sinonimi: "
     ant = "antonimi: "
 
     for sinonim in recnik[rec]["sinonimi"]:
         sin += sinonim + ", "
     print(sin[:-2])
 
     for antonim in recnik[rec]["antonimi"]:
         ant += antonim + ", "    
     print(ant[:-2] + "\n") 
































