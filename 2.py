hh,pp=input().strip().split()
pp=int(pp)
k=0
while k<len(hh)-1 and pp:
 if(hh[k]>hh[k+1]):
 pp-=1
 hh=hh[:k]+hh[k+1:]
 if(k!=0):
  k-=1
 else:
  k+=1
lk=hh[:len(hh)-jj]
print(lk)
