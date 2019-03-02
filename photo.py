import numpy
file=open("e_shiny_selfies.txt","r")
l=file.readline()
r=[int (n) for n in l.split()]
row=r[0]
#print(row)
a=list(file);l=[]
for i in a:
    i=i.split()
    l.append(i)
o=[l[i][0] for i in range(len(l))]
n_tags=[l[i][1] for i in range(len(l))]
tags=l;
for i in range(len(tags)):
    del tags[i][0];
    del tags[i][0];
d=dict()
dv=dict()
for i in range(row):
    tags[i].sort()
    if(o[i]=='H'):
        d[i]=tags[i]
    elif(o[i]=='V'):
        dv[i]=tags[i]
    else:
        pass
l1=sorted(d.values())
l2=sorted(dv.values())
print(l2)
res=[];resv=[]
for i in l1:
    for j in d.keys():
        if(i==d[j] and j not in res):
            res.append(j)
        else:
            pass
for i in l2:
    for j in dv.keys():
        if(i==dv[j] and j not in resv):
            resv.append(j)
resv2=[]            
for i in range(0,len(resv)-1,2):
    resv2.append(str(resv[i])+" "+str(resv[i+1]))
final=[]
final.append(len(res)+len(resv2))
final.extend(res)
final.extend(resv2)
print(final)
numpy.savetxt("e.txt",final,fmt="%s")
print("\n\nDONE\n\n")

