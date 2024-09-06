m,n = list(map(int,input().split()))

mylist = []
for i in range(n):
    y = int(input())
    mylist.append(y)

x = sum(mylist)

if m > x:
    print(m-x)
else:
    print(-1)    