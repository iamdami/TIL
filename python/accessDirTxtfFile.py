import os
import os.path

for root, dirs, files in os.walk("/path"):
    for file in files:
        if file.startswith(""):
            print(os.path.join(root, file))
