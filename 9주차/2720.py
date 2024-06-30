t=int(input())
for _ in range(t):
    c=int(input())
    q=c//25
    d=c%25//10
    n=c%25%10//5
    p=c%25%10%5//1
    print(q, d, n, p)