import shutil
import os

os.makedirs("destination", exist_ok=True)

#cop
shutil.copy("s.txt", "destination/s.txt")
print("cop fail")

#mov
shutil.move("destination/s.txt", "destination/moved_sample.txt")
print("mov fail")