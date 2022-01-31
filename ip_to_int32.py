

def ip_to_int32(ip):
    list_ip = ip.split('.')
    result = 0
    for i in range(4):
        result += int(list_ip[i]) << 8*(3-i)
        print(result)
    return result

def _main():
    print(ip_to_int32("128.32.17.0"))

if __name__ == "__main__":
    _main()