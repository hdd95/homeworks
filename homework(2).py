import sys
import timeit

print("hello world")
print("great work")


a = [1, 4, 4, 4, 46, 8, 9]
b = [1, 44, 'let', 8, 9]

print(type(a))
print(len(a))
print(a[0])
print(a[-1])
a.extend(b)
print(a)
a = a+b
print(a)
print(a.count(4))
print(a.index(46))
# help(list)
lst = ['egf', 'ywe', 'hgt', 'qwew']

lst.sort()
x = 22
print('list size', sys.getsizeof(lst))

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuples_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)
sets_test = timeit.timeit(stmt="([1,2,3,4,5])", number=1000000)
dict_test = timeit.timeit(stmt="{1,2,3,4,5}",  number=1000000)
print('sets timing:',  sets_test)
print('list timing :', list_test)
print('tuple timing:', tuples_test)
print('dict timing', dict_test)
if a > b:
    print('a bigger then b')

























