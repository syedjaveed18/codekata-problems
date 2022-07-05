L,R = map(int,input().split())
sum = 0
if L%2 == 0:
    start = L+1
else:
    start = L
    
for i in range(start,R+1,2):
    sum = sum + i
    
print(sum)
