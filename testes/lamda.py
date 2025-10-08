double = lambda x, y: x + y
print(double(5, 6)) 

arrange = lambda lst: sorted(lst)
print(arrange([5, 4, 3, 2, 1]))

ndLargest = lambda lst2: sorted(lst2)[-2]
print(ndLargest([5, 4, 3, 2, 1]))

ndLargest2 = lambda lst3: max(x for x in lst3 if x != max(lst3))
print(ndLargest([5, 4, 3, 2, 1]))