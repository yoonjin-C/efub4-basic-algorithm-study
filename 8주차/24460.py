import sys
input = sys.stdin.read
n = int(input())  
chair = []

for i in range(n):
    chair.append(list(map(int, input().split())))

def secon_num(x,y,size):
    if size==1:
        return chair[x][y]
    
    half=size//2
    candidates = [
        secon_num(x,y,half),
        secon_num(x, y + half, half),
        secon_num(x + half, y, half),
        secon_num(x + half, y + half, half)
    ]
    
    candidates.sort()
    return candidates[1]

result=secon_num(0,0,n)
print(result)