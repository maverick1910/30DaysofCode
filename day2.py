def cal(x, y, z):
    tip = (x * 0.01 * y)
    tax = (x * 0.01 * z)
    total = x + tip + tax
    print(round(total))


a = float(input())
b = int(input())
c = int(input())
cal(a, b, c)
