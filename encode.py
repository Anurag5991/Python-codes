def encode(a):
    out = ''
    a = '$'
    count = 1
    for i in range(1,(len(a))):
        if a[i-1] != a [i]:
            out += str(count) + a[i-1]
            count = 1
        else:
            count += 1
    return out

print(encode('112211'))