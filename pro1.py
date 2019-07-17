v1=int(input())
v2=[]
v3=[]
for i in range(v1):
  v3=input()
  v2.append(v3)
hb=[]
for i in zip(*v2):
  if(i.count(i[0])==len(i)):
    hb.append(i[0])
  else:
    break
print(''.join(hb))
