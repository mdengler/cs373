# CS 373 Unit 3.4: Efficiency

# Histogram Filters' efficiency in modeling the state space is
# exponential, mainly because of the need to model the full discrete
# range of each dimension and thus it's a full matrix with the curse
# of dimensionality

# Kalman Filters' efficiency in modeling the state space is quadratic,
# because as the dimensions grow only parameters of the gaussians are
# required to model the additional dimensions, which are kind of
# linear actually (?) -- he points out measurement space is
# represented as a covariance matrix, which is where the quadratic
# (squared) cost comes from.  This is a bit fast and loose, but the
# right idea IMO.
