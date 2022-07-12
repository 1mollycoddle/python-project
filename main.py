import re
import datetime



format = "%d.%m.%Y"
print("О чем мне вам напомнить?")
message = input()
text1 = re.findall(r"[^0-9.,-]", message)
text2 = ''.join(text1)
day = re.findall('завтра|понедельник|вторник|среду|четверг|пятницу|субботу|воскресенье', message)
day1 = ''.join(day)
datex = re.findall('[0-9][0-9][.,-][0-9][0-9][.,-][0-9][0-9][0-9][0-9 ]', message)
date_string = ''.join(datex)
dt2 = datetime.datetime.strptime(date_string, format)
print (text2)
print(date_string)
print(datetime.date.today())
print(dt2)