import numpy as np

n , m = input().split()
n = int(n)
m = int(m)
special = 0

arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
    
avamel = [1]
for i in range(2,n//2+1):
    if n%i == 0:
        avamel.append(i)
avamel.append(n)

for i in avamel:
    mat = np.array(arr).reshape(i,n//i)
    sum_row = np.sum(mat, axis=1)
    sum_col = np.sum(mat, axis=0)
    for i in range(len(sum_row)):
        sum_row[i] = sum_row[i]%m + 1
    for i in range(len(sum_col)):
        sum_col[i] = sum_col[i]%m + 1   
    
    special += np.max(sum_col)*np.min(sum_row)
    
print(special)
    
    