def dec2bin(num):
    """

    """
    res = []
    while num > 0:
        res.append(str(num % 2))
        num = num // 2
    return res

if __name__ == '__main__':
    num = 783758973498324923462974623874928974928738497234898892347948728948475982374982364962346239649328462396496239468235423659328649234623876942384982364923649234236429364
    print(type(num))
    res = dec2bin(num)
    print("".join(res))