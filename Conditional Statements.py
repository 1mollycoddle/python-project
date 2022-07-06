#simple_if
print()
print('simple_if')
number = int(input("Enter a number: "))
if number > 5:
    print("This number is greater than five.")

if number is not None:
    pass #TODO: add some logic here later

#if_else
print()
print('if_else')
x = float(input("x = "))
if x > 0:
    y = x ** 0.5
else:
    y = x ** 2
print(y)




#nested_if
print()
print('nested_if')

x = int(input('x = '))
if 0 < x < 7:
    print('Value is in range, let`s continue')
    y = 2 * x - 5
    if y < 0:
        print('y is negative')
    else:
        if y > 0:
            print('y is positive')
        else:
            print('y = 0')


#elif
print()
print('elif')
x = int(input('x = '))
if 0 < x < 7:
    print('Value is in range, let`s continue')
    y = 2 * x - 5
    if y < 0:
        print('y is negative')
    elif y > 0:
        print('y is positive')
    else:
        print('y = 0')

#elif_switch
print()
print('elif_switch')
print("""Menu:
1.File
2.View
3.Exit
""")

choice = input('Your choise: ')
if choice == '1':
    print('You have selected "File" menu')
elif choice == '2':
    print('You have selected "View" menu')
elif choice == '3':
    print('Stopping...')
else:
    print('Incorrect choise')

#condition
print()
print('condition')
is_ready = True
if is_ready:
    state_msg = "Ready"
else:
    state_msg = "Not ready yet"
print(state_msg)

is_ready = False
state_msg = is_ready and "Ready" or "Not ready yet"
print(state_msg)

is_ready = True
state_msg = "Ready" if is_ready else "Not ready yet"
print(state_msg)

#truth_value_testing
print()
print('truth_value_testing')
string = input('Enter a string: ')
if string:
    print('The string is {}'.format(string))

number = int(input('Enter a number: '))
if number:
    print('The number is not zero')
else:
    print('The number is zero')