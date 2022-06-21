dict = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'G':15}
n = input()
pow = len(n)
sum = 0
for i in n:
    sum+= int(dict[i])*16**(pow-1)
    pow = pow - 1
print(sum)
