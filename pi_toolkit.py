# os lets Python run Linux commands like hostname, free, df, and ping
import os

# shutil lets Python copy folders/files for backups
import shutil

# datetime lets Python create timestamps for backup names
from datetime import datetime


# This function displays the menu
def menu():
    print("\n=== PI TOOLKIT ===")
    print("1. System Report")
    print("2. Network Scan")
    print("3. Create Backup")
    print("4. Exit")


# This function shows information about the Raspberry Pi
def system_report():
    print("\n=== SYSTEM REPORT ===")

    print("\nHostname:")
    os.system("hostname")

    print("\nIP Addresses:")
    os.system("hostname -I")

    print("\nMemory:")
    os.system("free -h")

    print("\nDisk:")
    os.system("df -h /")


# This function scans your home network
def network_scan():
    # Start counting devices from 0
    devices_found = 0

    print("\n=== NETWORK SCAN ===")
    print("Scanning 192.168.0.1 to 192.168.0.254...")

    # Loop through IP addresses 192.168.0.1 to 192.168.0.254
    for i in range(1, 255):
        ip = f"192.168.0.{i}"

        # Ping each IP address once
        # Hide normal ping output using > /dev/null 2>&1
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")

        # If response is 0, the device replied
        if response == 0:
            print(ip, "is online")
            devices_found += 1

    print("\nDevices found:", devices_found)


# This function creates a backup of the projects folder
def create_backup():
    # Folder to back up
    source = "/home/joel/projects"

    # Folder where backups will be stored
    backup_folder = "/home/joel/backups"

    # Create a timestamp so each backup has a unique name
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Build the full backup folder name
    backup_name = backup_folder + "/projects_backup_" + time

    # Copy the whole projects folder into the backup folder
    shutil.copytree(source, backup_name)

    print("Backup created:", backup_name)


# Show the menu
menu()

# Ask the user what they want to do
choice = input("Choose an option: ")

# Run the correct function based on the user's choice
if choice == "1":
    system_report()
elif choice == "2":
    network_scan()
elif choice == "3":
    create_backup()
elif choice == "4":
    print("Goodbye!")
else:
    print("Invalid option.")
