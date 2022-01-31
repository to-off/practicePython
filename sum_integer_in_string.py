

def sum_of_integers_in_string(s):
    number = 0
    summ = 0
    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        else:
            summ += number
            number = 0
    return summ + number

def _main():
    print(sum_of_integers_in_string("12.4"))
    print(sum_of_integers_in_string("h3ll0w0rld"))
    print(sum_of_integers_in_string("2 + 3 = "))
    print(sum_of_integers_in_string("Our company made approximately 1 million in gross revenue last quarter."))
    print(sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))

if __name__ == "__main__":
    _main()