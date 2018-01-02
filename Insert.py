lista=[15,18,25]
listb=[2,5,19,30]
posa=posb=0


lenb=len(listb)


for a in range(0,len(lista)):
    for b in range(posb,len(listb)):
        if(lista[posa]>listb[posb]):
            lista.insert(posa,listb[posb])
            posb+=1
            posa+=1
        else:
            posa+=1
            break


if posb<lenb:
    for b in range(posb,lenb):
        lista.append(listb[b])

print lista
