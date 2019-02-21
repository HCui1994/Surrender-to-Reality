import numpy as np

x = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
y = np.array([1,2,3,4,5,6,7,8,9]).reshape(3, 3)

n,d = x.shape
m,d = y.shape
dist = np.zeros((n,m))
for i in range(n):
    for j in range(m):
        for k in range(d):
            dist[i,j] += (x[i,k]-y[j,k]) ** 2


print(np.dot(x.T, x) - 2 * np.dot(x.T, y) + np.dot(y.T, y))


print(dist)
