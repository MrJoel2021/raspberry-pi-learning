# Import shutil so Python can copy folders and files
import shutil

# Import datetime so we can add the current date and time to the backup name
from datetime import datetime

# This is the folder we want to back up
source = "/home/joel/projects"

# This is where the backup will be saved
backup_folder = "/home/joel/backups"

# Create a timestamp like 2026-06-07_23-45-10
# This makes each backup name unique
time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create the full backup folder name
# Example: /home/joel/backups/projects_backup_2026-06-07_23-45-10
backup_name = backup_folder + "/projects_backup_" + time

# Copy the entire projects folder into the new backup folder
shutil.copytree(source, backup_name)

# Tell the user where the backup was created
print("Backup created:", backup_name)
