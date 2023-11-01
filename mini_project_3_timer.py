import time

# t = '0:0:12'    # 0:5:32
t = input('Insert time to count down (h:m:s): ')   

data = t.split(":")
h = int(data[0])
m = int(data[1])
s = int(data[2])
total_sec = h*60*60+m*60+s
print(total_sec)

while total_sec > 0:
    hours,remain = divmod(total_sec,3600)
    mins, secs = divmod(remain,60)
    timer = '{:02d}:{:02d}:{:02d}'.format(hours,mins,secs)
    print(timer)
    time.sleep(1)
    total_sec -= 1

print("time up!")
