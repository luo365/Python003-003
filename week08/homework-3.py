# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

import time
import math


def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        elapsed = t1 - t0
        print(f'{result!r}: {elapsed}')
        return result
    return clocked


@clock
def my_gcd(n1, n2):
    return math.gcd(n1, n2)


if __name__ == "__main__":
    n1 = 40144129591
    n2 = 40145732447
    result = my_gcd(n1, n2)
