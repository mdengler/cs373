# CS 373 Unit 2.5: Bonus Question: Coconuts 4

#Write a program that will find the initial number
#of coconuts. 

def f(n):
    return (n-1) / 5.0 * 4

def f6(n):
    for i in range(6):
        n = f(n)
    return n 

def is_int(n):
    return abs(n-int(n)) < 0.0000001
   
# Enter code here.
n = 1
while not is_int(f6(float(n))):   # doesn't need to be float, because f(n) already forces float division
    n += 1

print n
