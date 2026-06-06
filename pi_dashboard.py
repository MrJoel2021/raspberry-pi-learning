import os
import socket
import shutil
print("===== PI DASHBOARD =====")

hostname = socket.gethostname()
ip = os.popen("hostname -I").read().strip()

print("Hostname:", hostname)
print("IP Address:", ip)

print("\nCPU Temperature:")
print(os.popen("vcgencmd measure_temp").read())

print("Memory:")
print(os.popen("free -h").read())

disk = shutil.disk_usage("/")

print("Disk Usage:")
print("Total:", round(disk.total / (1024**3), 1), "GB")
print("Used :", round(disk.used / (1024**3), 1), "GB")
print("Free :", round(disk.free / (1024**3), 1), "GB")
