import shutil
import os

source = "s.txt"
backup = "backup_s.txt"

#4cop
shutil.copy(source, backup)
print("fail copyy")

#5del
if os.path.exists(backup):
    os.remove(backup)
    print("Backup file deleted.")
else:
    print("File does not exist.")