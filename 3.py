g1,g2=input().split()
n1=abs(len(g2)-len(g1))
for i in range(len(g1)):
 if(len(g2)==1 and g2[i] in g1):
  break
 if(g1[i]!=g2[i]):
  n1=n1+1
print(n1)
