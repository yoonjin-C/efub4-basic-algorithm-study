n=int(input())
chicken=list(map(int,input().split()))
k=int(input())
l=n//2
while(True):
    for i in range (0, n, n//l): #배열을 n/l개씩 묶어서 순회
        chicken[i:i+n//l]=sorted(chicken[i:i+n//l])
    if l==k:
        break
    l=l//2

for _ in chicken:
    print(_, end=' ')