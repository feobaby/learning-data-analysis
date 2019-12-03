import numpy as np

# array
array_a = np.array([1,2,3,4,5])
print(array_a)

print([1,2,3,4,5, 'derrick'])
print(array_a.shape) #one dimensional array

#multi-dimensional array
array_b = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(array_b)
print(array_b.shape)

# 3x3
# 4x4
seq_a =[1,2,3]
seq_b = [4,5,6]
seq_c = [7,8,9]
seq_d = [10.5,11.5,12.5]

array_abc = np.array([seq_a,seq_b,seq_c,seq_d])
print(array_abc)

array_c = np.array([[1,2,3],[4,5,6]])
print(array_c.shape)
print(array_c.size) #no of elements in the array

array_d = array_c.reshape(3,2) #to change rows and shapes format #transpose
#OR 
array_d = array_c.T
print(array_d)

# indexing
print(array_d[0]) # row
print(array_d[:,1]) # column
print(array_d[0,0]) # a specific value

array_e = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])


array_f = array_e.reshape(2,8)
print(array_f)

array_g = array_e.T # to transpose the values
print(array_g)

print(array_g[0],array_g[1]) # return two rows
print(array_e[0, -1]) # the row and the last value on the row

# using -ve indexing
print(array_e[-1,-1]) # last row and the last value in the row; also [3, -1]
print(array_e[:,-3]) # second column

# data types
array_h = np.array([[1,2,3],[4,5,6]], dtype=float)
print(array_h)

# create an array/matric of 3 x 3 numbers all in 0
array_i = np.zeros((3,3))
print(array_i)

# create an array/matric of 3 x 3 numbers all in 1
array_j = np.ones((3,3))
print(array_j)

# create an array/matric of 3 x 3 numbers all in 5
array_k = np.full((3,3),5)
print(array_k)

# create an array of 3 x 4 random numbers
array_l = np.random.random((3,4))
print(array_l)

# assign it to a int data type
array_m = np.array([32766,32767,32678], dtype=np.int16)
print(array_m)

# unsigned int data types only take +ve values
array_n = np.array([-1,0,1], dtype=np.uint16)
print(array_n)


# advanced indexing
row_1 =[1,2,3,4,5]
row_2 =[6,7,8,9,10]
row_3=[11,12,13,14,15]
row_4=[16,17,18,19,20]
row_5=[21,22,23,24,25]

test_data = np.array([row_1, row_2, row_3, row_4,row_5])
print(test_data)

#slice 
print(test_data[:,2:4:1]) #start:ending value :step size
# -ve index
print("------")

print(test_data[:,-2:-4:-1])

print("------")
# boolean
greater_than_five = test_data > 5
print(greater_than_five)
print(test_data[greater_than_five]) # print all the values that returned true against the > 5 condition

print("------")
# where
drop_under_5_array = np.where(test_data > 5, test_data, 0)
print(drop_under_5_array)

# logical AND
print("-------")
drop_under_5_array_and_over_20 = np.logical_and(test_data >5, test_data <20)
print(drop_under_5_array_and_over_20)
print(test_data[drop_under_5_array_and_over_20]) # return a one dimensional array that retuen the values > 5 and < 20 and not a multi-dimensional matrix
print("-------")
array_o = np.arange(0,100,5)
print(array_o)
print(array_o.size)

array_o_reshape = array_o.reshape(4,5)
print(array_o_reshape)

# -ve indexing
print(array_o_reshape[:,-1])
print("-----------")
 # boolean indexing 
 
array_o_above_50 = array_o_reshape[array_o_reshape >= 50]
print(array_o_above_50)

# python slice

print(array_o_above_50[0:len(array_o_above_50):2])


# slice of a row
print(array_o_reshape[:, 0:5:2])

print(np.where(array_o_reshape > 50, array_o_reshape, -1)) # when this condition returns false, add -1
print(np.where(array_o_reshape > 50, array_o_reshape*2, -1)) # when this condition returns false, add -1 and multiply the True values by 2

print("------------------")

# Array Math

array_p = np.array([[1,2],[3,4]])
array_q = np.array([[2,2],[6,6]])

# single array operations
print(array_p.sum(axis=1)) # row = axis=0, column = axis=1
print(array_p.cumsum())
print(array_p.prod())
print(array_p.cumprod())

 # operations across arrays

print(array_p + array_q)
print(array_p - array_q)
print(array_p * array_q)
print(array_p / array_q)

print(np.dot(array_p, array_q))

print("----------------")

array_r = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_s = np.array([[2,2,2],[3,4,5],[6,7,8]])
print(array_r)
print(array_s)

print(array_r.sum(axis=0))
print(array_r.ptp(axis=1)) # highest no - lowest no

print(array_r.min())
print(array_r.max())
print(array_r.mean())

print(np.power(array_r, array_s))
array_t = np.array([[1,1,1],[2,2,2],[3,3,3]])
print(array_r + array_s + array_t)
print(array_r / array_s / array_t)

# Broadcasting

array_u = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3]])
array_v = np.array([0,1,2,3])
array_w = np.array([[1],[2],[3]])
array_x = np.array([[0,1,2,3],[0,1,2,3],[0,1,2,3]])
print(array_u + array_v)
print(array_u + array_x)
print(array_u + array_w)

print("---------------")
# match rows and columns
array_y = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_z = np.array([3,2,1])
print(array_y + array_z)

array_ab = np.array([[3],[2],[1]])
print(array_y + array_ab)

