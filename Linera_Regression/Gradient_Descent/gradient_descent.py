import numpy as np
from matplotlib import pyplot as plt

n=5

x=np.array([1,2,3,4,5])
y=np.array([5,8,11,14,17])

m=0
c=0
learning_rate=0.01

for i in range(1,101):

    y_predicted=m*x+c

    #calculate cost function
    cost =(1/n) * sum([value ** 2 for value in (y-y_predicted)])

    #plot after each iteration cost against m
    plt.scatter(m,cost)


    #caculate gradients
    dm=-(2/n) * sum(x*(y-y_predicted))
    dc=-(2/n) * sum(y-y_predicted)

    #update parameter
    m=m-learning_rate*dm
    c=c-learning_rate*dc

    print("m {},c{},cost {} iteration{}".format(m,c,cost,i))

plt.show()
