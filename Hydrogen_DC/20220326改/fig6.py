import numpy as np
import tensorflow as tf

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(34, 3, input_length=1))
# The model will take as input an integer matrix of size (batch,
# input_length), and the largest integer (i.e. word index) in the input
# should be no larger than 999 (vocabulary size).
# Now model.output_shape is (None, 10, 64), where `None` is the batch
# dimension.
input_array = np.zeros((34,1))
for i in range(34):
    input_array[i,0]= i
model.compile('rmsprop', 'mse')
output_array = model.predict(input_array)
output_array.resize(35,3)
output_array = abs(output_array)
output_array *= 18
# In[]
import matplotlib.pyplot as plt



fig = plt.figure(dpi=800)
ax = fig.add_subplot(projection='3d')

i=0
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=1
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='green')

i=2
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=3
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=4
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=5
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=6
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=7
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=8
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=9
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=10
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=11
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=12
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=13
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=14
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=15
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=16
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=17
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=18
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=19
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=20
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=21
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=22
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=23
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=24
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=25
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=26
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=27
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=28
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g')

i=29
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='g',label='area 3')

i=30
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange')

i=31
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r')

i=32
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='orange',label='area 2')

i=33
x,y,z=output_array[i,0],output_array[i,1],output_array[i,2]
ax.scatter(x, y, z, marker='o',color='r',label='area 1')







ax.legend()
ax.set_xlabel('1-st dimension')
ax.set_ylabel('2-nd dimension')
ax.set_zlabel('3-rd dimension')

plt.savefig('fig6.png',pad_inches = 0,bbox_inches='tight') #保存为svg格式矢量图