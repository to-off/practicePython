

def factorial(x):
    if x == 0: return 1
    else:
        return x * factorial(x-1)

def C(k,n):

    return factorial(n)/(factorial(k)*factorial(n-k))

def formula(n):
    result = ''
    if n == 0: return "1"
    if n < 0: result += '1/('
    abs_n = abs(n)
    deg_a = ''
    deg_b = ''
    for k in range(abs_n+1):
        koaf = str(C(k,abs_n)).split('.')[0]
        C_k_n = '' if koaf == '1' else koaf
        if koaf == '0': continue
        deg_b = '' if k == 1 else f'^{k}'
        deg_a = '' if abs_n-k == 1 else f'^{abs_n-k}'
        if abs_n-k == 0:
            result += C_k_n + 'b' + deg_b
        elif k == 0:
            result += C_k_n + 'a' + deg_a
        else:
            result += C_k_n + 'a' + deg_a + 'b' + deg_b
        if k < abs_n:
            result += '+'
    if n < 0: result += ')'

    return result

def _main():
    print(formula(0))
    print(formula(1))
    print(formula(2))
    print(formula(-2))
    print(formula(3))
    print(formula(5))

if __name__ == "__main__":
    _main()