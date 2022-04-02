for i in range(100,1000):
    x=i//100 #百位
    y=i%100//10#十位
    z=i%10#个位
    if sum([pow(x,3),pow(y,3),pow(z,3)])==i#百位，十位，个位的立方和 等于数字本身
        print(i)