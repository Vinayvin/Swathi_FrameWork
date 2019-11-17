import itertools as iter

all_ones=iter.repeat(1)
print(list(next(all_ones) for i in range(5)))

three_fours = iter.repeat(4, 3)  # 4, 4, 4
print(list(next(three_fours) for j in range(5)))
