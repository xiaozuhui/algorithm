def find(num:int) -> int:
    """
    寻找回文
    """
    while 1:
        if str(num) == "".join(list(reversed(str(num)))) and str(bin(num)) == "".join(list((reversed(str(bin(num)))))) and str(oct(num)) == "".join(list((reversed(str(oct(num)))))):
            return num
        num += 2

if __name__ == "__main__":
    res = find(11)
    print(res)