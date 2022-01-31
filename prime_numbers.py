
def check_prime_with_for(n: int) -> bool:
    if not n or n == 1: return False
    for i in range(2, int(n**1/2) +1):
        if n % i == 0:
            return False
    return True


def check_prime_with_while(n: int) -> bool:
    if not n or n == 1: return False
    i = 2
    while i <= int(n**1/2):
        if n % i == 0:
            return False
        i+=1
    return True

def _main():
    print(check_prime_with_for(2), check_prime_with_while(2))
    print(check_prime_with_for(3), check_prime_with_while(3))
    print(check_prime_with_for(4), check_prime_with_while(4))
    print(check_prime_with_for(7), check_prime_with_while(7))
    print(check_prime_with_for(24), check_prime_with_while(24))


if __name__ == "__main__":
    _main()