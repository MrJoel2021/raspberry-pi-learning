import os

print("Scanning network...")

for i in range(1, 255):
    ip = f"192.168.0.{i}"
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")

    if response == 0:
        print(ip, "is online")# Import the os module so we can run Linux commands from Python
import os

# Print a message so the user knows the scan has started
print("Scanning network...")

# Loop through numbers 1 to 254
# These numbers will become the last part of the IP address
for i in range(1, 255):

    # Create an IP address like 192.168.0.1, 192.168.0.2, etc.
    ip = f"192.168.0.{i}"

    # Ping the IP address once
    # -c 1 means send 1 ping
    # -W 1 means wait 1 second
    # > /dev/null hides normal output
    # 2>&1 hides error messages too
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")

    # If response is 0, the device replied to the ping
    if response == 0:
        print(ip, "is online")
