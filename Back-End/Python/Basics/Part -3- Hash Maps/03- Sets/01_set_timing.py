from timeit import timeit

n = 100_000
s = set(range(n))
l = list(range(n))
d = {i:None for i in range(n)}


number = 1_000_000
search = 9
t_list = timeit(f'{search} in l', globals=globals(), number=number)
t_set = timeit(f'{search} in s', globals=globals(), number=number)
t_dict = timeit(f'{search} in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)


number = 3_000
search = 99_999
t_list = timeit(f'{search} in l', globals=globals(), number=number)
t_set = timeit(f'{search} in s', globals=globals(), number=number)
t_dict = timeit(f'{search} in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)





number = 3_000
search = -1
t_list = timeit(f'{search} not in l', globals=globals(), number=number)
t_set = timeit(f'{search} not in s', globals=globals(), number=number)
t_dict = timeit(f'{search} not in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)

l = []
s = set()
d = {}

print('#', 'dict', 'set', 'list')
for i in range(50):
    print(i, d.__sizeof__(), s.__sizeof__(), l.__sizeof__())
    l.append(i)
    s.add(i)
    d[i] = None

l = []
s = set()
d = {}

print('#', 'dict', 'set', 'list')
for i in range(50):
    print(i, d.__sizeof__(), s.__sizeof__(), l.__sizeof__())
    l.append(i**1000)
    s.add(i*1000)
    d[i*1000] = None