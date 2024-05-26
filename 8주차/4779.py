def cut_line(a,n):
    if n==1:
        return
    for i in range(a+n//3, a+(n//3)*2):
        result[i]=' '
    cut_line(a,n//3)
    cut_line(a+n//3*2, n//3)
import sys
while True:
    try :
        n=int(sys.stdin.readline())
        result=['-']*(3**n)
        cut_line(0,3**n)
        print(''.join(result))
    except:
        break
