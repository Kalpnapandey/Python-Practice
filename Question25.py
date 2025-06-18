# Merge two dictionaries into one.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# dict1.update(dict2)
# dict3=dict1|dict2
# print(dict3)
dict3={**dict1, **dict2}
print(dict3)


