# pythonPractice

listb=[2,5,7,8,13];
lista=[1,2,4,9,15,18];
newlist=[];
posa=posb=0;


for a in range(posa,len(lista)):
    for b in range(posb,len(listb)):
        if lista[a]>= listb[b]:
            newlist.append(listb[b])
            posb=posb+1
        else:
            newlist.append(lista[a])
            posa=posa+1
            break

if posa<len(lista):
    for resta in range(posa,len(lista)):
        newlist.append(lista[resta])
else:
    for restb in range(posb,len(listb)):
        newlist.append(listb[restb])

print newlist

