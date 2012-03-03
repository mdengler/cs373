colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

# unfortunately I submitted this too late but as it gave the right
# results in all the test cases I'm pretty sure it was good!

def pp(m):
    """pretty print a matrix"""
    print
    print "\n".join([" ".join(["%0.2f" % e for e in r]) for r in m])


p = []

def normalize(q):
    """normalize a list or a matrix (list of lists)"""
    normalized = None

    if isinstance(q[0], float):
        sum_values = float(sum(q))
        normalized = [unnormalized / sum_values for unnormalized in q]
    else:
        normalized = []
        sum_matrix = sum([sum(r) for r in q])
        for r in q:
            normalized.append([unnormalized / sum_matrix
                               for unnormalized in r])

    normalized_sum = sum([sum(r) for r in normalized])
    assert 1.0 - abs(normalized_sum) < 0.00001, "Matrix not normalized properly (%s)" % normalized_sum
    return normalized


def sense(prior, observation, p_right=None):

    sensed = []

    if p_right is None:
        p_right = 1.0
    p_wrong = 1. - p_right

    for y in range(len(prior)):

        row = prior[y]
        unnormalized_row = []

        for x in range(len(row)):

            prior_xy = prior[y][x]
            reality = colors[y][x]

            # TODO: review why this works!
            if observation == reality:
                new_p = prior_xy * p_right
            else:
                new_p = prior_xy * p_wrong

            # print "x,y = %s, %s; sensed %s, reality is %s, thus %s --> %s" % (
            #     x, y, observation, reality, prior_xy, new_p)

            unnormalized_row.append(new_p)

        sensed.append(unnormalized_row)

    return normalize(sensed)


def move(prior, motion, p_succ=None):
    dy, dx = motion

    if p_succ is None:
        p_succ = 1.0
    p_fail = 1.0 - p_succ

    posterior = [[0.0] * len(row) for row in prior]
    #pp(posterior)

    for y_i in range(len(prior)):
        y_fail =  y_i
        y_succ = (y_i + dy) % len(prior)

        row = prior[y_i]

        for x_i in range(len(row)):
            x_fail =  x_i
            x_succ = (x_i + dx) % len(row)

            posterior[y_fail][x_fail] += p_fail * prior[y_i][x_i]
            posterior[y_succ][x_succ] += p_succ * prior[y_i][x_i]

    return posterior


# colors = [['green', 'green', 'green'],
#           ['green',   'red',   'red'],
#           ['green', 'green', 'green'],
#           ]
# measurements = ['red', 'red']
# motions = [[0, 0], [0, 1]]
# sensor_right = 1.0
# p_move = 0.5


# colors = [['red', 'green', 'green',   'red', 'red'],
#           ['red',   'red', 'green',   'red', 'red'],
#           ['red',   'red', 'green', 'green', 'red'],
#           ['red',   'red',   'red',   'red', 'red'],
#           ]

# measurements = ['green', 'green', 'green', 'green', 'green']
# motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
# sensor_right = 0.7
# p_move = 0.8

uniform_probability = 1 / float(sum([len(row) for row in colors]))
p = [[uniform_probability] * len(row) for row in colors]

#pp(p)

for s, m in zip(measurements, motions):
    #print "moving by %s" % m
    p = move(p, m, p_succ=p_move)
    #pp(p)

    #print "sensing %s" % s
    p = sense(p, s, p_right=sensor_right)
    #pp(p)

#print
#print "*" * 50
#print


#Your probability array must be printed 
#with the following code.

show(p)




