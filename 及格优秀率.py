n=int(input())
grade=[]
a=0
b=0
for i in range(n):
    grade.append(int(input()))
    if grade[i]>=85:
       a+=1    #优秀个数
       b+=1    #及格个数
    elif grade[i]>=60:
        b+=1
print('{:2.0f}%'.format(b/n*100))  #优秀率
print('{:2.0f}%'.format(a/n*100))  #及格率
