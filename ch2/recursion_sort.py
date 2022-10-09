import numpy as np
import math

np.random.seed(0)

# 创建待排序的序列
x = np.random.randint(0, 100, 20)
print(x)

def merge(x:np.array, i_beg:int, i_mid:int, i_end:int):
    """ 合并俩有序序列
    """
    y = np.zeros_like(x[:i_end-i_beg])
    i_cur = 0

    i_l = i_beg
    i_r = i_mid

    while(i_cur < i_end-i_beg):
        if x[i_l] < x[i_r]:
            y[i_cur] = x[i_l]
            i_l += 1
            i_cur += 1

            # 如果左边序列已经排完，则直接拷贝右边剩余的序列到y
            if i_l == i_mid:
                y[i_cur:] = x[i_r:i_end]
                break
        else :
            y[i_cur] = x[i_r]
            i_r += 1
            i_cur += 1

            # 如果右边序列已经排完，则直接拷贝左边剩余的序列到y
            if i_r == i_end:
                y[i_cur:] = x[i_l:i_mid]
                break   
    
    x[i_beg:i_end] = y

def recurve_sort(x):
    """ 非递归的合并排序
    """

    # 通过有序序列长度计算循环次数 deep
    x_len = len(x)
    deep = math.ceil(math.log2(x_len))
    
    for i in range(deep):
        # 通过循环次数，计算合并后序列的最大长度
        per_len = 2**(i+1)

        i_beg = 0	# 待排序序列的起始坐标
        i_mid = int(per_len/2) # 待排序序列的分割坐标
		
        # 如果 per_len ≤ x_len ，则 i_end = per_len, 否则选 i_end = x_len
        i_end = per_len if per_len <= x_len else x_len # 待排序序列的结尾坐标

        while(i_mid < x_len):
            merge(x, i_beg, i_mid, i_end)
            i_beg += per_len
            i_mid += per_len 

            i_end = i_end + per_len if i_end+per_len < x_len else x_len


def recurve_sort_core(x, i_beg, i_end):
    print(i_beg, i_end, int((i_end-i_beg)/2))
    if i_end - i_beg > 1:
        recurve_sort_core(x, i_beg, i_beg + int((i_end-i_beg)/2))
        recurve_sort_core(x, i_beg + int((i_end-i_beg)/2), i_end)
        merge(x, i_beg, i_beg + int((i_end-i_beg)/2), i_end)
    elif i_end - i_beg < 1:
        assert(False) # 应该不会触发
    else:
        return 1


def recurve_sort_2(x):
    """ 递归的合并排序
    """

    recurve_sort_core(x, 0, len(x))
    
recurve_sort_2(x)
print(x)
recurve_sort(x)

print(x)