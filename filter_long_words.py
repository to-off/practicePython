

def filter_long_words(sentence, n):

    if sentence is not None:
        list_of_words = sentence.split()
        result_list = [word for word in list_of_words if len(word) > n]
        return result_list


def _main():
    print(filter_long_words("The quick brown fox jumps over the lazy dog", 4))


if __name__ == "__main__":
    _main()

