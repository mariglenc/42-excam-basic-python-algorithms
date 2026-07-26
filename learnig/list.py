py_list = [0, 1, 2, 3, 4, 5]

# [start : stop] -> stop is not included

print("[0:] -> ", py_list[0:])   # [0, 1, 2, 3, 4, 5]   whole list
print("[1:] -> ", py_list[1:])   # [1, 2, 3, 4, 5]      skip first
print("[2:] -> ", py_list[2:])   # [2, 3, 4, 5]         skip first 2
print("[3:] -> ", py_list[3:])   # [3, 4, 5]            skip first 3
print(" - - - - - - - - - - ")
print("[:1] -> ", py_list[:1])   # [0]                  first 1
print("[:2] -> ", py_list[:2])   # [0, 1]               first 2
print("[:3] -> ", py_list[:3])   # [0, 1, 2]            first 3
print(" - - - - - - - - - - ")
print("[-1:] -> ", py_list[-1:])   # [5]            last 1
print("[-2:] -> ", py_list[-2:])   # [4, 5]         last 2
print("[:-1] -> ", py_list[:-1])   # [0,1,2,3,4]    all but last
print("[:-2] -> ", py_list[:-2])   # [0,1,2,3]      all but last 2