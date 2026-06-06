import os

# Specify the directory path
path = "/"

# List and print the contents of the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)