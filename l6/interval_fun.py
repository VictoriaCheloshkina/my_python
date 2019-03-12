def f(x):
    return x**2+3

sum1 = 0
for i in range(10, 31, 2):
    sum1 += f(i)
print(sum1)
