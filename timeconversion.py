import time
print(time.strftime('%H:%M:%S', time.strptime(input(), '%I:%M:%S%p')))
