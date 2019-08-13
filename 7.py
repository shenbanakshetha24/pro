chatr=int(input())
r=[]
dog=0
for h in range (0,chatr+1):
    dog=abs((2**h)-chatr)
    r.append(dog)
kall=min(r)
print(kall)
