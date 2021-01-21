import os
import shutil
import datetime
i = 1

for root, dirs, files in os.walk("PATH TO FILES"):
    for file in files:
        now = str(datetime.datetime.now())[:19]
        now = now.replace(":","_")
        if file[-4:].lower() == '.pdf':
            shutil.copy(os.path.join(root, file), os.path.join("PATH TO DEST", str(now) + file))
