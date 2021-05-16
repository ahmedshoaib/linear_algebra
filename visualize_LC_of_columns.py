#visulaize linear combinations of columns 

import numpy as np, matplotlib.pyplot as plt
import sys, pdb
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('seaborn-whitegrid')
#ax = plt.axes(projection='3d')


#Row picture  - 2

fig = plt.figure()
ax = plt.axes()

x = np.linspace(-5, 5, 1000)
ax.plot(x, 2*x)
ax.plot(x,(3+x)/2)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.title("Row picture of LE in 2 var")
plt.show()


#column picture

col1 = np.array([0, 0, 0, 2, -1, 0])  #[U,V,W,X,Y,z]
col2 = np.array([ 0, 0, 0, -1, 2, 0])
lc=[]
#linear combinations of col1 and col2  -> plane-like => all linear combinations-> x-y plane
#for x in range(-100,100):
#	for y in range(-100,100):
#		lc.append((x*col1) + (y*col2))
lc.append(col1)
lc.append(col2)


soa = np.array(lc)

X, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#print(X,Y,Z,U, V, W)
ax.scatter3D(U,V,W)
#ax.quiver(X,Y,Z,U,V,W)
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([0, 1])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Col picture/lc of LE in 2 var")
plt.show()




#3eqn, 3var

#Row
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = 2*Y - X + 1

#similarly set other two rows
#pdb.set_trace()
ax.contour3D(X, Y, Z, 150, cmap='viridis')



ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.title("Row picture of LE in 3 var")
plt.show()



#Column picture


col1 = np.array([0, 0, 0, 2, -1, 0])  #[U,V,W,X,Y,z]  - X
col2 = np.array([ 0, 0, 0, -1, 2, -3])  #- y
col3 = np.array([ 0, 0, 0, 0, -1, 4])  #z
lc=[]
#linear combinations of col1 and col2  -> plane-like => all linear combinations-> x-y plane
for x in range(-10,10):
	for y in range(-10,10):
		for z in range(-10,10):
			lc.append((x*col1) + (y*col2) +(z*col3))
''' # View all involved vectors
lc.append(col1)
lc.append(col2)
lc.append(col3)
'''

soa = np.array(lc)

X, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#print(X,Y,Z,U, V, W)
ax.scatter3D(U,V,W)
#ax.quiver(X,Y,Z,U,V,W) #view involoved vectors
ax.set_xlim([-40, 40])
ax.set_ylim([-40, 40])
ax.set_zlim([-40, 40])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Col picture/lc of LE in 3 var")
plt.show()

