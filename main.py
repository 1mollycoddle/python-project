import re
import datetime
import time



print("О чем мне вам напомнить?")
message=str(input())

date=re.findall(r"\bзавтра\b",message)

task=(re.search(r'\w+(ть|чь)', message).group())

if date!=0:
    print(date[0],task)
