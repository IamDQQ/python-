n=2021041820210418
num=0
docker=set()
for i in range(1,int(n**0.5)+1):
     if n%i==0:
        docker.add(i)
        docker.add(n//i)
for i in docker:
  for j in docker:
     for k in docker:
         if  n==i*j*k:
             num+=1
print(num)


