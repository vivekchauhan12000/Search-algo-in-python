A = [12,7,3,4,0]
for i in range(len(A)):
    min_= i
    for j in range(i+1, len(A)):
        if A[min_] > A[j]:
            min_ = j
    #swap
    A[i], A[min_] = A[min_], A[i]

x=A[0]
print(x)    