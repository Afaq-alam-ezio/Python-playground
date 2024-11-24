dic = {101: "Alan", 102: "Arm", 103: "Helen"}
print(dic[101])
print(dic.get(105))
print(dic.keys())
print(dic.values())
print(dic.items())

for key, value in dic.items():
    print(f"The keys is {key} and the value is {value}")

# ABOVE IS OF VIDEO 33 AND BELOW IS VIDEO 34

ep1 = {1: "a", 2: "b", 3: "c"}
ep1.update({4: "d"})
ep1.pop(2)  # 2 is key
print(ep1)
ep1.popitem()  # this will delete the last item from the dictionary
del ep1[1]  # removes the 1 : "a" pair
print(ep1)
del ep1     # deletes the whole dictionary
