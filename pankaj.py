from itertools import combinations
string,hb=map(int,input().split())
p=len(str(string))
S=list(combinations(str(string),p-hb))
S=(sorted(S))
x="".join(S[0])
print(x)
