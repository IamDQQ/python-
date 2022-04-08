points=[x,y for x in range(20) for y in range(21)]
docker=set()
for i in range(len(points)):
    x1,y1=points[i][0],points[i][1]
    for j in range(len(points))
    x2,y2=points[j][0],points[j][1]

    if x1==x2:
        continue
    k=(y2-y1)/(x2-x1)
    b=(x1*y2-x2*y1)/(x2-x1)
    if (k,b) not in docker:
    docker.add(k,b)
print(len(docker)+20)


