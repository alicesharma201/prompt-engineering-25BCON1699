n = 10
a = 0
b = 1

print('Fibonacci series:', end=' ')

for i in range(0, n):
    print(a, end=' ')
    next = a + b
    a = b
    b = next