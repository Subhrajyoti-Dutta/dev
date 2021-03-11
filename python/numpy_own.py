import numpy as np

def map_numpy(func,np_array,*arg):
    return np.vectorize(func)(np_array,*arg)

def ver_join(x1,x2):
    return np.concatenate((x1,x2),axis=0)

def hor_join(x1,x2):
    return np.concatenate((x1,x2),axis=1)

def col_sum(x1):
    return np.sum(x1,axis = 0)

def row_sum(x2):
    return np.sum(x1,axis = 1)



if __name__=="__main__":
    arr = np.array([
        [1, 5],
        [2, 6],
        [3, 7],
        [4, 8]
        ])
    arr2 = np.array([2,3,4,5])

    print(np.matmul(arr2,arr))