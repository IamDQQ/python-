#IDLE 里的写法
while True:
    try:
        x,y=map(int,input().split())
        print(sum([x,y]))
    except:
        break
#pycharm
x=int(input())
y=int(input())
print(x+y)