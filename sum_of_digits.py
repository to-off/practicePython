def _sum_dig(dig):
    result = 0
    while dig > 0:
        result += dig % 10
        dig //= 10
    return result


def sum_of_digits(digits):
    if digits is not None:
        result = _sum_dig(int(digits))
        list_of_digits = [digit for digit in str(digits)]
        return ' + '.join(list_of_digits) + ' = ' + str(result)
    return ""



def _main():
    print(sum_of_digits("3433"))
    print(sum_of_digits(64323))
    print(sum_of_digits("0003433"))

if __name__ == "__main__":
    _main()