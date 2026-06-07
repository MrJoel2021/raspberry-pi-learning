import os

# Start counting devices
devices_found = 0

print("Scanning network...")

# Open a file and create a fresh report each time
with open("network_results.txt", "w") as f:

    # Write a title into the file
    print("=== Network Scan Results ===", file=f)

    # Scan IP addresses
    for i in range(1, 255):

        ip = f"192.168.0.{i}"

        response = os.system(
            f"ping -c 1 -W 1 {ip} > /dev/null 2>&1"
        )

        if response == 0:

            # Show on screen
            print(ip, "is online")

            # Save to file
            print(ip, "is online", file=f)

            devices_found += 1

    # Save total to file
    print("\nDevices found:", devices_found, file=f)

# Show total on screen
print("\nScan complete")
print("Devices found:", devices_found)
