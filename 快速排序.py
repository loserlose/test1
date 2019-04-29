import random
def quick_sort(arr):
    #快速排序
    if len(arr) < 2:
        return arr
    mid = arr[len(arr)//2]
    left,right = [],[]
    arr.remove(mid)
    for item in arr:
        if item >=mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left) + [mid] +quick_sort(right)

def random_int_list(start, stop, length):
    #生成随机数组
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0
  random_list = []
  for i in range(length):
    random_list.append(random.randint(start, stop))
  return random_list
# print(random_int_list(1,100,10))

list = random_int_list(1,100,100)
print(list)
print(quick_sort(list))

#quick_sort = lambda array:array if len(array)<=1 else quick_sort([item for item in array[1:] if item<=array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])