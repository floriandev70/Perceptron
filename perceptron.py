# import libraries
import numpy as np

# create Perceptron class 
class Perceptron:
    type = 'Real perceptron with inputs x1, x2 and the heavyside activation function.'
    
    # instantiation
    def __init__(self, W=np.array([0.,0.,0.])):
        #weight vector (w0 w1 w2) with w0 = bias b
        self.W = W
    
    # activation function fa(x) = step function
    def fa(self, x):
        y = 0 if (x < 0) else 1
        return y
    
    # output function f(X) = y with X = input vector x0=?, x1, x2
    def f(self, X):
        # create the weighted sum of all inputs 
        sum = np.dot(X, self.W)
        # return y = fa(sum)
        return self.fa(sum)
    
    # hyperplane function fh(x)
    def fh(self,x):
        # y = x2 = -w1/w2 * x1 - b/w2 for w2 <> 0!
        if self.W[2] != 0:
            y = ((-self.W[1] / self.W[2] * x) - self.W[0] / self.W[2])
        else:
            y = -0.
        return y
    
    # learn function
    def learn(self, epochs, features, labels):
        
        # number of false classifications
        misclassified_ = []
        
        # set weights to zero + 1 weight for bias b => (0 0 0)
        self.W = np.array([0.,0.,0.])
        print('init weights', self.W)
        
        # learning loop
        for epoch in range(epochs):
            misclassified = 0
            # in each epoch run through all rows of data
            for x, label in zip(features, labels):
                x = np.insert(x,0,1.) # x0 = 1

                y = np.dot(w, x.transpose())

                target = 1.0 if (y > 0) else 0.0

                delta = (label.item(0,0) - target)

                if(delta): # misclassified
                    misclassified += 1
                    self.W += (delta * x) # weights = weights + (delta * x)
                    print('------------------')
                    print('epoch:',epoch)
                    print('x:',x)
                    print('y:',y)
                    print('target:',target)
                    print('delta:',delta)
                    print('adjusted w:',w)

            misclassified_.append(misclassified)
        return misclassified_
