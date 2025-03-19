my_list = [34, 10, 27, 20, 22, 3, 1]

# i = 0

# while i < len(my_list):
#     item = my_list[i]
#     print(item)
#     i += 1

for item in my_list:
    print(item)

# results = []

# for item in my_list:
#     results.append(item + 3)

results = [item + 3 if item > 3 else 0 for item in my_list]
results1 = [item + 3 for item in my_list if item > 3]

print(results)
print(results1)

from enum import Enum

class Role(Enum):
    USER="user"
    SYSTEM="system"

def greet(name:str, role:Role) -> str:
    if role==Role.USER:
        return f"Hello {name}"
    return ""

print(greet("Kiitan", role=Role.USER))