n=int(input())
t1=[]
for i in range(n):
    it=input()
    t1.append(it)
q=tuple(t1)
print(q[0],end=" ")
print(q[n-1])
