'''n=0
while n<=100:
    print n
    n=n+3
print "exit"
print "--------------------"'''
num=[12,34,467,421,54,23,56,99]
oushu=[]
jishu=[]
aa=len(num)
print(num)
print (aa)
while aa > 0 :
    num = num.pop()
    print(num)
    if (num) % 2 == 0 :
        oushu.append(num)
    else:
        jishu.append(num)
print (oushu)
print (jishu)