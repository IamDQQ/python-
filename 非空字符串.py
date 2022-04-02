ls='0100110001010001'
#ls='aaab'
length=len(ls)
l=[]
for i in range(length):
    for j in range(1,length+1):
        if j>i:
            if ls[i:j] in l:
                continue
            else:
                l.append(ls[i:j])
print(len(l))