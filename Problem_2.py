from math import exp, sqrt, pi
import random

def gaussian_density(x,mu,sigma):
    return exp(-(x-mu)**2/(2*sigma**2))/(sigma*sqrt(2*pi))+exp(-(x-5*mu)**2/(2*(sigma/3)**2))/((sigma/3)*sqrt(2*pi))

def next_sample(f,q,theta_k):
    theta_prime = q(theta_k,1)

    r = random.random()

    theta_k_plus_one = theta_k

    if ((f(theta_prime,2,sqrt(2))/f(theta_k,2,sqrt(2)))>r):
        theta_k_plus_one = theta_prime

    return theta_k_plus_one


random.seed(3.14)
thetas = []
theta = 0
thetas.append(theta)
for i in range(10**5):
    theta = next_sample(gaussian_density,random.gauss,theta)
    thetas.append(theta)

import matplotlib.pyplot as plt
import numpy as np

N=50
plt.hist(thetas,normed=True,histtype='step',bins=N)
x=np.linspace(min(thetas),max(thetas),num=N)

y=[]
for xx in x:
    y.append(gaussian_density(xx,2,sqrt(2)))

plt.plot(x,y)
plt.show()