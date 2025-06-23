from datetime import datetime
import time

f = open('log.txt', 'w')

for i in range(0,10):
    time_now = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
    print(time_now, i)
    f.write(time_now)
    time.sleep(1)
    f.write(str(i))
    f.write("\n")

f.close()