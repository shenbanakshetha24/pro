n11=int(input())
b=list(map(int,input().split()))
c=0
for i in range(0,n11-2):
	for j in range(1,n11-1):
		for k in range(2,n11):
			if(b[i]<b[j] and b[j]<b[k]):
				c+=1
print(c)
