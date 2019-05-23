import os

print(os.system("tasklist"))

pid = input('Put your PID : ')

os.system("taskkill /f /pid {}".format(pid))