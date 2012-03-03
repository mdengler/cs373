# CS 373 Unit 2.12: Evaluate Gaussian

import math

def gaussian(mean, variance):
    """variance is sigma-squared"""
    def f(x):
        decay = 1 / math.sqrt(2. * math.pi * variance)
        exponent = -((x - mean) * (x - mean)) / (2. * variance)
        return decay * math.exp(exponent)
    return f

mean = 10.
variance = 4.
x = 8.
f = gaussian(mean, variance)
print f(x)
# answer is 0.12098536226


