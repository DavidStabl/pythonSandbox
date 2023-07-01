import os

path = os.getcwd()
files = os.listdir(path)
files_list = [f for f in files if os.path.isfile(os.path.join(path, f))]

print("Aktuální složka :", path)
print()

for file in files_list:
    print(file)
