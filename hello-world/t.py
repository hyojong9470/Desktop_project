import datetime

now = datetime.datetime.now()

nowtime = now.strftime("%Y-%m-%d %H:%M:%S")
print(nowtime)
print(type(nowtime))