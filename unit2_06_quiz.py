# CS 373 Unit 2.6: Bonus Question: Coconuts 5

"""
Answer is 2499:

From the output of my program to solve #2:

n = 15621 can work so far, taking 1/5 (3124) of n minus one and seeing if the result, 12496, can work
n = 12496 can work so far, taking 1/5 (2499) of n minus one and seeing if the result, 9996, can work
n = 9996 can work so far, taking 1/5 (1999) of n minus one and seeing if the result, 7996, can work
n = 7996 can work so far, taking 1/5 (1599) of n minus one and seeing if the result, 6396, can work
n = 6396 can work so far, taking 1/5 (1279) of n minus one and seeing if the result, 5116, can work
n = 5116 can work so far, taking 1/5 (1023) of n minus one and seeing if the result, 4092, can work
----- 15621 - True
15621 worked!
"""

def can_work(n, mans_turn=6):
    if mans_turn < 1:
        return True
    if n < 6:
        print "n < 6 (%s)" % n
        return False
    if n % 5 == 0:
        print "n divisible by 5 (%s)" % n
        return False
    if (n - 1) % 5 != 0:
        print "n - 1 not divisible by 5 (%s)" % n
        return False
    print "n = %s can work so far, taking 1/5 (%s) of n minus one and seeing if the result, %s, can work" % (n, (n-1)/5, (4 * (n-1))/5)
    return can_work((4 * (n - 1)) / 5, mans_turn=mans_turn - 1)


coconuts = 6
while coconuts < 100000:
    worked = can_work(coconuts)
    print "----- %s - %s" % (coconuts, worked)
    if worked:
        print "%s worked!" % coconuts
        break
    coconuts += 1


# answer is 15621

