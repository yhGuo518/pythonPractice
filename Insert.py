lista=[15,18,25]
listb=[2,5]
posa=posb=0


lena=len(lista)
lenb=len(listb)


for a in range(0,lena):
    for b in range(posb,lenb):
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
