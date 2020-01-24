taskList = [23, "Jane",["Lesson 23", 560, {"Currency" : "Kes"}], 987, (76,"John")]
print(type(taskList))
print(taskList[2][2]["Currency"])
print(taskList[2][1])
print(len(taskList))
taskList.remove(987)
taskList.insert(3,789)
print(taskList)

print(str(taskList[3])[::-1])
print(taskList[::-1])
print(taskList[:-1])
