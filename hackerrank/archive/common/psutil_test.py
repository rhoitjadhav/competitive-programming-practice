import psutil

arr = psutil.net_connections()

for i in arr:
    print(i.laddr[0])
    break

