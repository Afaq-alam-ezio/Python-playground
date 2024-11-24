import os

# creation below:
# for i in range(100):
#     if os.path.exists(f"sata\ babe {i}"):
#         os.rename(f"sata\ babe {i}", f"sata\ babe {i+1}")

for i in range(100):
    if os.path.exists(f"sata\ bye {i+1}"):
        os.removedirs(f"sata\ bye {i+1}")
