
X=[[12,9,3],
   [4,5,6],
   [7,8,3]]

Y=[[6,8,1,3],
   [5,7,3,4],
   [0,6,9,1]]

result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]+=X[i][k]*Y[k][j]

for r in result:
    print(r)