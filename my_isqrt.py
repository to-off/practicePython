
import typing

def int_sqrt_with_del(n):
    return int(pow(n,1/2))

def int_sqrt_with_while(n: int) -> int:
    "get integer part of sqrt "
    start = 0
    end = n//2
    smoller_int = end // 2
    bigger_int = smoller_int + 1
    degree = lambda x:x*x
    while degree(smoller_int) > n or degree(bigger_int) <= n:
        smoller_int = (end + start) // 2
        bigger_int = smoller_int + 1
        if degree(smoller_int) > n:
            end = smoller_int
        else:
            start = bigger_int

    return smoller_int

#def int_sqrt_2degree(n):


def _main():
    print(int_sqrt_with_while.__doc__)
    print(int_sqrt_with_while(5))
    print(int_sqrt_with_while(24))
    print(int_sqrt_with_while(102402102))
    print(int_sqrt_with_del(5))
    print(int_sqrt_with_del(24))
    print(int_sqrt_with_del(102402102))

if __name__ == "__main__":
    _main()