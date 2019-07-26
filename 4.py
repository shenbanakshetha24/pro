df,gh=map(str,input().split())
i=0
if len(df)>len(gh):
 df,gh=gh,df
j=0
while j<len(df):
 i+=(ord(gh[j])-ord(df[j]))
 j+=1
for j in range(j,len(gh)):
 i+=ord(gh[j])-ord('a')+1
print(i)
