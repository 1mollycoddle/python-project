import re
import datetime
import time



print("О чем мне вам напомнить?")
message=str(input())

date=re.findall(r"\bзавтра\b",message)

task=re.findall("ть" or "ть" or "чь", message)

if date!=0:
    print(date, task)
