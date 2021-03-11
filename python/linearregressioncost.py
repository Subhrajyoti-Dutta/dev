#import numpy_own as npo
import numpy as np

def linearRegCostFunction(X, y, theta, lamb):
    y = np.array(y)
    X = np.array(X)
    theta = np.array(theta)

    m = np.shape(y)[1]

    J = 0
    grad = np.zeros(theta.shape)


#=================================================================#
    diff = np.matmul(X,theta) - y
    theta_sq = theta ** 2
    J += np.sum(diff ** 2,axis=0)/(2*m) + lamb/(2*m) * np.sum(theta_sq)
    sum_grad = np.sum(diff * X,axis=0)
    print(sum_grad.T )
    print(sum_grad)
    grad += 1/m*np.transpose(sum_grad) 
    grad += lamb/m * np.ones((theta.shape[0]-1,1)) * theta[1:]

#=================================================================#
    grad = np.ravel(grad.T)
    return [J,grad]




if __name__ == "__main__":
    X =[[1, 8, 1, 6],
        [1, 3, 5, 7],
        [1, 4, 9, 2]]

    y =[[7],
        [6],
        [5]]

    theta =[[0.1],
            [0.2],
            [0.3],
            [0.4]]

    lamb = 0


    #s = np.array(theta)
    result = linearRegCostFunction(X,y,theta,lamb)
    print(result)