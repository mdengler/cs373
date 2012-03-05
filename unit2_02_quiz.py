# CS 373 Unit 2.2: Bonus Question: Coconuts 1

# so monkey ends up with 6 coconuts
# 5 from guys in the night, 1 from the morning division
#
# the original number has been divided by five six times and at no
# step (originally) is it not divisible by five, but the remainder - 1
# is

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

