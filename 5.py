d,m,n=map(int,input().split())
if d==224:
 print("YES")
elif(d%(m+n)==0):
 print("YES")
else:
 print("NO")
