# Import the os module.
# This lets Python run Linux commands from inside the script.
import os

# Import datetime from the datetime module.
# This lets Python get the current date and time.
from datetime import datetime

# Print a title so the output is easy to read.
print("===== SYSTEM REPORT =====")

# Print the current date and time.
# datetime.now() gets the current time from the system.
print("Time:", datetime.now())

# Print a heading for the hostname section.
print("\nHostname:")

# Run the Linux command 'hostname'.
# This shows the name of the Raspberry Pi.
os.system("hostname")

# Print a heading for the IP address section.
print("\nIP Addresses:")

# Run the Linux command 'hostname -I'.
# This shows the IP addresses assigned to the Raspberry Pi.
os.system("hostname -I")

# Print a heading for memory usage.
print("\nMemory:")

# Run the Linux command 'free -h'.
# This shows RAM usage in a human-readable format.
os.system("free -h")

# Print a heading for disk usage.
print("\nDisk:")

# Run the Linux command 'df -h /'.
# This shows storage usage for the main filesystem.
os.system("df -h /")
