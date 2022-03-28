#pycharm
a=1
b=1
n=int(input())
for i in range(n-1):
    a,b=b,(a+b)%1007
print(a)
#IDLE
a=1
b=1
while True:
    try:
        n=int(input())
        for i in range(n-1):
            a,b=b,(a+b)%1007
        print(a)
    except:
        break