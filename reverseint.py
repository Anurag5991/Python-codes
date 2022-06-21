def reverseInt(num):
    y = str(abs(num))
    y = y[::-1]
    output = int(y)

    if num >= 2**32 - 1 or num <= - 2**31:
        return 0
    elif num < 0:
        return -1 * output
    else:
        return output

print(reverseInt(-120))