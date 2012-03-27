# CS 373 Unit 3.15: Resampling

w = [0.6, 1.2, 2.4, 0.6, 1.2]
sum_w = sum(w)
normalized = [wi / sum_w for wi in w]
assert sum(normalized) == 1.0
print normalized
