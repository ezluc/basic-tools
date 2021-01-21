import os
import shutil
import datetime
i = 1

for root, dirs, files in os.walk("N:\\ComplaintMatters\\Bank of America & Merrill Lynch\\Summers, Lawrence v. Bank of America Private Bank\\Documents Received\\2. Statements & Confirms\\CFI PART 2"):
    for file in files:
        now = str(datetime.datetime.now())[:19]
        now = now.replace(":","_")
        if file[-4:].lower() == '.pdf':
            shutil.copy(os.path.join(root, file), os.path.join("C:\\home\\projects\\automation_scripts\\2.samples\\summers\\cfipart2", str(now) + file))
