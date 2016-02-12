from math import exp, sqrt, pi
import random

def gaussian_density(x,mu,sigma):
    return exp(-(x-mu)**2/(2*sigma**2))/(sigma*sqrt(2*pi))

def mcmc(f,q,theta_k):
    theta_prime = q(0,1)

    r = random.random()

    theta_k_plus_one = theta_k

    if (f(theta_prime,2,sqrt(2))/f(theta_k,2,sqrt(2))>r):
        theta_k_plus_one = theta_prime

    return theta_k_plus_one

theta = 0
for i in range(10**4):
    theta = mcmc(gaussian_density,random.gauss,theta)
    print theta