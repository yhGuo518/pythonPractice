import os
import re
import codecs

fbasepath=r"D:\test\FrontendResult_base.xml"
baselist=[]
index=0
idline=[]

for line in codecs.open(fbasepath,'r','utf_16'):
	if(line.find("si id=")>=0):
		baselist.append(line)

fnewpath=r"D:\test\FrontendResult_new.xml"

newxml=codecs.open(fnewpath,'r+','utf_16').readlines()
for line in codecs.open(fnewpath,'r','utf_16'):
	index+=1
	if(line.find("si id=")>=0):
		idline.append(index)
		
for i in range(0,len(idline)):
	newxml[idline[i]-1]=baselist[i]

f=codecs.open(fnewpath,'r+','utf_16')
f.writelines(newxml)


		

	
		
