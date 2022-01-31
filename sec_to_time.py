

def to_time(seconds):
    hours = seconds // 3600
    minuts = seconds // 60 % 60
    return "{} hour(s) and {} minute(s)".format(hours, minuts)


def _main():
    print(to_time(3600))
    print(to_time(3601))
    print(to_time(3500))
    print(to_time(323500))


if __name__ == "__main__":
    _main()
