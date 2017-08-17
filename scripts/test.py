import os

for i in range(10):
    d=str(i)
    os.makedirs(d)
    for j in range(4):
        with open(d+'/'+str(j),'w') as f:
            f.write('hello')