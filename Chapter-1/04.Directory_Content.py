import os

# Specify the directory path
directory_path = '/'

# Get the list of all entries in the directory
entries = os.listdir(directory_path)

# Iterate over the entries and print them
for entry in entries:
    print(entry)
