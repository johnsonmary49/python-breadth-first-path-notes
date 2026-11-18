from solution import solve

value = {'graph': {'a': ['b', 'c'], 'b': ['d'], 'c': ['d']}, 'start': 'a', 'goal': 'd'}
print(solve(value))
