#doctrings
print()
print('doctrings')
def function():
    """Строка, стоящая в самом начале функции (а также модуля, класса или метода),
    играет роль особого вида комментариев – документационной строки (docstring).
    """
    print("function colled")

function()
help(function)
help(print)
print(function.__doc__)

#radix-change
print()
print('radix-change')
number = int(input('Введите число: '))
print('Двоичная система:         ', bin(number))
print('Восьмеричная система:     ', oct(number))
print('Шестнадцатеричная система:', hex(number))

#reversed_example
print()
print('reversed_example')
for i in reversed(range(5)):
    print(i)

#min_max
print()
print('min_max')
a = 5
b = 7
c = 2
print(min(a, b, c))
print(max(a, b, c))


#nested_functions
print()
print('nested_functions')
def outer_function():
    def inner_function():
        print('Внутренняя функция')
    print('Внешняя функция')
    inner_function()
outer_function()

#scoping_example1
print()
print('scoping_example1')
var = "global variable"
def functions():
    print(var)

functions()

#scoping_example2
print()
print('scoping_example2')
def function():
    global var
    print(var)
    var = 'новое значение'
    print(var)

var = 'глобальная переменная'
function()
print(var)

#scoping_example3
print()
print('scoping_example3')
def function(c, d):
    global a, b
    a = 5
    b = 7
    c = 10
    d = 12

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)
function(c, d)
print(a, b, c, d)
#scoping_example4
print()
print('scoping_example4')
def outer_function():
    var = 8
    def inner_function():
        nonlocal var
        print(var)
        var = 10

    print(var)
    inner_function()
    print(var)


var = 0
print(var)
outer_function()
print(var)



#factorial
print()
print('factorial')
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#fibonacci
print()
print('fibonacci')
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


index = int(input('Введите номер числа Фибоначчи: '))
print(fib(index))

