#Home work #3

#1
int_a = 55
print(id(int_a))
str_b = 'Cursor'
print(id(str_b))
set_c = {1, 2, 3}
print(id(set_c))
lst_d = [1, 2, 3]
print(id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))

#2
lst_d = [1, 2, 3]
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

#3
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

#4
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

#5
print("Anna has {} apples and {} peaches.".format(4, 5))

#6
print("Anna has {0} apples and {1} peaches.".format("four", "five"))

#7
print("Anna has {0} apples and {sx} peaches.".format("four", sx="six"))

#8
print("Anna has {0:5} apples and {1:3} peaches.".format("four", "five"))

#9
apple = 8
peache = 4
print(f"Anna has {apple} apples and {peache} peaches.")

#10
app = 9
peac = 6
print("Anna has %d apples and %d peaches" % (app, peac))

#11
app = 10
peac = 4
dict = {"apple": app, "peaches": peac}
print("Anna has %(apple)d apples and %(peaches)d peaches" % dict)

#12
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)

#13
lst = []
for num in range(10):
   if num % 2 == 0:
       lst.append(num // 2)
   else:
       lst.append(num * 10)
print(lst)


#14
dict_comprehension = {d: d ** 2 for d in range(1, 11) if d % 2 == 1}
print(dict_comprehension)


#15
dict_comprehension = {d: d ** 2 if d % 2 == 1 else d // 0.5 for d in range(1, 11)}
print(dict_comprehension)

#16
x = {}
for num in range(10):
   if num ** 3 % 4 == 0:
       x[num] = num ** 3
print(x)


#17
x = {}
for num in range(10):
   if num ** 3 % 4 == 0:
       x[num] = num ** 3
   else:
       x[num] = num
print(x)


#18
foo = lambda x, y: x if x < y else y
print(foo(2, 3))

#19
def foo(x, y, z):
   if y < x and x > z:
       return z
   else:
       return y
print(foo(5, 6, 8))


#20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

#21
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True))



#22
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst_to_sort)

#23
list_a = [2, 3, 4]
list_b = [5, 6, 7]
list_c = []
list_c = (list_a[0]**list_b[0], list_a[1]**list_b[1], list_a[2]**list_b[2])
print(list_c)


#24
import functools
fo = lambda a, b: a + b
foo = functools.reduce(fo, lst_to_sort)
print(foo)


#25
new_list = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(new_list)


#26
lst_neg=list(filter(lambda x: x<0, range(-10, 10)))
print(lst_neg)


#27
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
new_list = list(filter(lambda x: x in list_1, list_2))
print(new_list)

