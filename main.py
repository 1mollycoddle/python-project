import re
import datetime



format = "%d.%m.%Y"
print("О чем мне вам напомнить?")
message = input()
text1 = re.findall(r"[^0-9.,;:-]", message)
text = ''.join(text1)
date1 = re.findall('[0-9][0-9][.,-][0-9][0-9][.,-][0-9][0-9][0-9][0-9 ]', message)
date = ''.join(date1)
day1 = re.findall('завтра|(в понедельник)|(в? вторник)|в среду|в четверг|пятницу|субботу|воскресенье', message)
day = ''.join(day1)
time1 = re.findall('(в [0-9][0-9][./:;-][0-9][0-9])|(в [0-9][0-9])|(в [0-9][./:;-][0-9][0-9])', message)
time = ''.join(time1)

print(text,date,day,time)



'''day = re.findall('завтра|понедельник|вторник|среду|четверг|пятницу|субботу|воскресенье', message)
day1 = ''.join(day)
datex = re.findall('[0-9][0-9][.,-][0-9][0-9][.,-][0-9][0-9][0-9][0-9 ]', message)
date_string = ''.join(datex)
dt2 = datetime.datetime.strptime(date_string, format)
print (text2)
print(date_string)
print(datetime.date.today())
print(dt2)'''