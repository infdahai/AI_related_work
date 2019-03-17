

import random
import numpy as np


def geneData(numPoints):
    """
    numPoints : the number of points
    x_sample : the initial x value
    y_sample : y value generated
    """

    x_sample = np.random.random(size=(numPoints,5))
    y_sample = np.random.randint(0,2,size=numPoints)
    return x_sample,y_sample


def GD(x, y, theta, alpha, m, numIterations):
    """
        Gradient Decrease Algorithm:
            x : the initial x value
            y : y value generated
            theta: initial theta 
            alpha : the learning rate
            m : the number of points
            numIterations :  the times of iterations about gradient decrease
    """

    xTrans = x.transpose()     # if you want to use X to multiply W , you shold transpose x firstly.
    i = 0
    eps = 0.01              # the threshold of cost
    cost = 1                # the cost value

    # Two discriminating conditions
    while i<numIterations and cost> eps:
        i += 1          # the times of iterations  adds 1
        hypothesis = np.dot(x,theta)        # compute W * x
        loss = hypothesis -y                
        cost = np.sum(loss**2)/(2*m)        # use square loss function
        print("Iteration %d | Cost: %f" % (i, cost))
        gradient = np.dot(xTrans,loss)/m    # compute the gradient according to math inference
        theta = theta - alpha*gradient         # update the theta 

    print(theta)
    return theta 

def SGD(x, y, theta, alpha, m, numIterations):
    """
        Stochastic Gradient Decrease Algorithm:
            x : the initial x value
            y : y value generated
            theta: initial theta 
            alpha : the learning rate
            m : the number of points
            numIterations :  the times of iterations about gradient decrease
    """
    xTrans = x.transpose()     # if you want to use X to multiply W , you shold transpose x firstly.
    i = 0
    eps = 0.01              # the threshold of cost
    cost = 1                # the cost value

    # Two discriminating conditions
    while i<numIterations and cost> eps:
        i += 1          # the times of iterations  adds 1
        hypothesis = np.dot(x,theta)        # compute W * x
        loss = hypothesis -y                
        cost = loss[random.randint(0,n)]**2/2        # use square loss function
        print("Iteration %d | Cost: %f" % (i, cost))

        random_index = random.randint(0,m-1)             # compute the gradient according to math inference ,
        gradient = np.dot(xTrans[:,random_index],loss[random_index])     #  just use the random gradient

        theta = theta - alpha*gradient         # update the theta 

    print(theta)
    return theta  


def miniBatchGD(x, y, theta, alpha, m, numIterations,batch = 10):
    """
        mini-Batch Gradient Decrease Algorithm:
            x : the initial x value
            y : y value generated
            theta: initial theta 
            alpha : the learning rate
            m : the number of points
            numIterations :  the times of iterations about gradient decrease
            batch : the quantity of loss elements in every cycle
    """
    xTrans = x.transpose()     # if you want to use X to multiply W , you shold transpose x firstly.
    i = 0
    eps = 0.01              # the threshold of cost
    cost = 1                # the cost value

    # Two discriminating conditions
    while i<numIterations and cost> eps:
        i += 1          # the times of iterations  adds 1
        hypothesis = np.dot(x,theta)        # compute W * x
        loss = hypothesis -y          
        cost = loss[random.randint(0,n)]**2/2        # use square loss function
       
        time = numIterations//m            # compute 
        mod = i//time                      # where the index begins and ends
        begin = mod*time 
        end  = begin+batch

        print("Iteration %d | Cost: %f" % (i, cost))
        gradient = np.dot(xTrans[:,begin:end],loss[begin:end])/batch    # compute the gradient according to math inference
                                                                        # its range in [begin,end]
        theta = theta - alpha*gradient         # update the theta 

    print(theta)
    return theta  

def MomentumGD(x, y, theta, alpha, m, numIterations,gamma = 0.5):
    """
        Momentum Gradient Decrease Algorithm:
                the algorithm is based on consideration to momentum and SGD algorithm.

            x : the initial x value
            y : y value generated
            theta: initial theta 
            alpha : the learning rate
            m : the number of points
            numIterations :  the times of iterations about gradient decrease
            gamma : the coefficient of updating momentum
    """
    xTrans = x.transpose()     # if you want to use X to multiply W , you shold transpose x firstly.
    i = 0
    eps = 0.01              # the threshold of cost
    cost = 1                # the cost value
    v = 1                   # set the initial value of v

    # Two discriminating conditions
    while i<numIterations and cost> eps:
        i += 1          # the times of iterations  adds 1
        hypothesis = np.dot(x,theta)        # compute W * x
        loss = hypothesis -y          

        cost = loss[random.randint(0,n)]**2/2        # use square loss function
        print("Iteration %d | Cost: %f" % (i, cost))


        random_index = random.randint(0,m-1)             # compute the gradient according to math inference ,   
        gradient = np.dot(xTrans[:,random_index],loss[random_index])     #  just use the random gradient
        v = gamma*v + alpha*gradient
        theta = theta - v         # update the theta 

    print(theta)
    return theta  



x,y = geneData(100)
m,n = np.shape(x)       #  m : the number of points , n : the dimension of x
numIterations = 1000
alpha =0.01             # the learning rate 

theta = np.ones(n)      # the initial theta  (1,..,1)


result = []
result.append(GD(x,y,theta[:],alpha,m,numIterations)) # use the slice of theta ,
                                            #to prevent from modifying the origin value of theta
result.append(SGD(x,y,theta,alpha,m,numIterations))     
result.append(miniBatchGD(x,y,theta,alpha,m,numIterations))
result.append(MomentumGD(x,y,theta,alpha,m,numIterations))                                    

print(result)


