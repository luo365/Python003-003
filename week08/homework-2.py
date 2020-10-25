# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。


from collections import abc
import math


def my_map(func, iter_objs):
    if isinstance(iter_objs, abc.Iterable):
        for item in iter_objs:
            yield func(item)
    else:
        raise Exception('输入变量不可迭代')



if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    it = my_map(math.sqrt, input_list)

    for item in it:
        print(item)