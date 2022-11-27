
X=[[12,9],
   [7,3],
   [5,6]]

result=[[0,0,0],
        [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i]=X[i][j]
        
for r in result:
    print(r)
    
#List Comprehension

X=[[12,9],
   [7,3],
   [5,6]]

result=[[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
for r in result:
    print(r)
