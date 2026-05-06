def safe_num(num):
    if num < 0:
        return 255
    
    elif num > 255:
        return 0

    return num


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


def get_bin(number):
    return dec2bin(safe_num(number))