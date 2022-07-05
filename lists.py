#list_defnition
print()
print("list_defnition")
int_list = [1, 2, 3, 5]
char_list = ['a', 'c', 'z', 'x']
empty_list = []
print('Numbers:', int_list)
print('Chars:', char_list)
print('Empty lisy:', empty_list)
list_from_range = list(range(5))
print("From range:", list_from_range)
list_from_string = list("a string")
print("From string:" , list_from_string)

#list_indexing
print()
print("list_indexing")
my_list = [5, 7, 9, 1, 1, 2]
print(my_list[0])
print(my_list[1])
index = int(input('Enter an index: '))
element = my_list[index]
print(element)

#negative_indices
print()
print("negative_indices")
my_list = [5, 7, 9, 1, 1, 2]
pre_last = my_list[-2]
print(pre_last)
result = my_list[0] + my_list[-1]
print(result)

#slicing1
print()
print('slicing1')
my_list = [5, 7, 9, 1, 1, 2]
sub_list = my_list[0:3]
print(sub_list)
print(my_list[2:-2])
print(my_list[4:5])
#slicing2
print()
print('slicing2')


my_list = [5, 7, 9, 1, 1, 2]

sub_list = my_list[0:-1:2]
print(sub_list)
print(my_list[2:-2:2])
print(my_list[-1:0:-1])
print(my_list[2:])
print(my_list[2::2])
print(my_list[:-2])
print(my_list[::-2])

#in_example
print()
print('in_example')
my_list = [5, 7, 9, 1, 1, 2]
value = int(input('Enter a number'))
if value in my_list:
    print('This number is in list')
else:
    print('This number is not in list')

#len_example
print()
print('len_example')
my_list = [5, 7, 9, 1, 1, 2, 123]
print("Number of elements", len(my_list))


#sting_indexing
print()
print('sting_indexing')
string = "a string"
print(string[0])
print(string[2])
print(string[-1])
print(string[2:5])
print(string[:5])
print(string[2:])
print(string[::2])
print(string[::-1])

print(string[2]+string[-3:])

#in_str
print()
print('in_str')
string = input("Enter a string: ")
if 'q' in string:
    print('There`s a "q" in the string')
else:
    print("There isn`t a 'q' in the string ")

#str_len
print()
print('str_len')
string = "a string"
print(len(string))


#append
print()
print('append')
my_list =[]
my_list.append(3)
my_list.append(5)
my_list.append(my_list[0] + my_list[1])
print(my_list)

#del
print()
print('del')
my_list = [5, 1, 5, 7, 8, 1, 0, -23]
print(my_list)
del my_list[2]
print(my_list)

#mutation
print()
print('mutation')
my_list = [5, 1, 5, 7, 8, 1, 0, -23]
print(my_list)
my_list[3] = 18
print(my_list)

#traversal
print()
print('traversal')
my_list = [5, 1, 5, 7, 8, 1, 0, -23]
for x in my_list:
    print('{} ^ 2 = {}'.format(x, x ** 2))

#fibonacci
print()
print('fibonacci')
n = 10
fibs = [1, 1]
for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])
print(fibs)





