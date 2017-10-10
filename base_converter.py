def base_converter(n, base):
    stack = []
    while n > 0:
        rem = n % base
        stack.append(rem)
        n = n // base
    label = '0123456789abcdef'
    res = ''
    while len(stack) > 0:
        res += label[stack.pop()]
    return res

print(base_converter(32, 2))
print(base_converter(32, 8))
