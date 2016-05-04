scores = [60, 73, 81, 95, 34]
n = 0
total = 0
nn=0
totalxx=0
totalxxx=0

for x in scores:
    n += 1
    total += x
    nn=x**2
    totalxx += nn
avg = total / n
nnn=0
for x in scores:
    n +=1
    nnn=(avg-x)**2
    totalxxx+=nnn
    
print('total ' + str(total))
print('average ' + str(avg))
print('平方和 '+str(totalxx))
print('變異數 '+str(totalxxx))
