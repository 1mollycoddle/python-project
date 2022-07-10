#function_examples
print()
print('function_examples')
def print_numbers(limit):
    for i in range(limit):
        print(i)

n = int(input())
print_numbers(n)

#example1
print()
print('example1')
def hello_world():
    print('Hello, World!')
hello_world()

#example2
print()
print('example2')
def print_numbers(limit):
    for i in range(limit):
        print(i)

def main():
    print_numbers(3)
    print()
    print_numbers(5)

if __name__ == "__main__":
    main()

#example3
print()
print('example3')
def add_numbers(first,second):
    return first + second
result = add_numbers(2,3)
print(result)


#example4
print()
print('example4')
def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3
def main():
    for i in range(-3,4):
        y = function(i)
        print('function(', i, ')=', y ,sep='')
main()

#example5
print()
print('example5')

def print_info(object_name,color,price):
    print('Object:', object_name)
    print('Color:', color)
    print('Price:', price)
    print()
print_info('pen','blue', 1 )
print_info(price=5, object_name='чашка', color='оранжевый')

#example6
print()
print('example6')
def hello(name='Alex'):
    print('Hello, ', name, '!', sep='')

hello('Python')
hello()