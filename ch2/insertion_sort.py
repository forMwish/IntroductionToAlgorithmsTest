import numpy as np

np.random.seed(0)

x = np.random.randint(0, 100, 20)
print(x)

def insertion_sort(x, forward="up"):
    """ 插入排序
    """
    for i in range(1, len(x)):
        cur_val = x[i]
        cur_i = i
        if forward == "up": # 升序
            while cur_i != 0  and cur_val < x[cur_i-1]:
                x[cur_i] = x[cur_i-1]
                cur_i -= 1
        elif forward == "down": # 降序
            while cur_i != 0 and cur_val > x[cur_i-1]:
                x[cur_i] = x[cur_i-1]
                cur_i -= 1
        else:
            assert False
        x[cur_i] = cur_val

insertion_sort(x, "up")
print(x)

insertion_sort(x, "down")
print(x)
