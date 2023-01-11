import time
#date time imported

timenow = time.localtime(time.time())
year,month,day,hour,minute = timenow[0:5]

print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute))

#Epoch time
print(time.time())

#sequence call
print(time.gmtime())

#time to string
print(time.asctime())
print(time.ctime())

print("Hello")
time.sleep(1)
print("World")
time.sleep(1)

print(str(year) + "/" + str(month) + "/" + str(day))
