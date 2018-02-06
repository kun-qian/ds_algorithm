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


def base_converter_re(n, base):
    base_string = '0123456789ABCDEF'
    if n < base:
        return base_string[n]
    else:
        return base_converter(n // base, base) + base_string[n % base]


print(base_converter(32, 2))
print(base_converter(3699, 8))
print(base_converter_re(32, 2))
print(base_converter_re(3699, 8))
