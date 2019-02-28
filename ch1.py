# Assignment:
#  Write a program that couns to 100 skipping all odd numbers, printing each
#  value on after another (use the end= attribute for calls to print())

r = range (1,100,2)
#print r
for n in range (1, 100, 2):
    print (n, end=' ')
