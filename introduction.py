

#1 task
print('Hello, World!')

#2 task
print("value1","value2")

#3 task
name = 'Dima'
print(name)

#4 task
name = input('Whats is your name?')
print('Hello,', name)

#5 task
x = float(input('First number:'))
y = float(input('Second nubmer:'))
operation = input('Operation:')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
else:
    print('Unsupported operation')
if result is not None:
    print('Result:' , result)

#task 6
from flask import Flask, request, render_template

# Создаём объект веб-приложения
app = Flask(__name__)


@app.route('/')
def hello_world():

    return 'Hello World!'


@app.route('/hello/', methods=['GET', 'POST'])
def hello():

    if request.method == 'POST':     # если пользователь ввёл своё имя
        name = request.form['name']  # то получаем его
    else:
        name = None                  # иначе присвоим name значение None
    # После этого отдаём пользователю HTML-страницу на основе шаблона
    # hello_form.html, в который мы передаём имя пользователя
    # (HTML можно изучить на соответсвующем курсе по фронтенд-разработке).
    return render_template('hello_form.html', name=name)


@app.route('/<name>')
def hello_buddy(name):
    """
    Любой другой адрес мы считаем именем пользователя
    и выдаём соответствующее приветствие.
    """
    return 'Hello, ' + name + '!'


# Если данный файл был запущен как главный, а не импортирован
# из другого модуля, то запускаем сервер веб-приложения.
# По умолчанию он будет доступен по адресу http://localhost:5000/
if __name__ == '__main__':
    app.run()
