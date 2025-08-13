num = 10
binary = bin(num)
print(binary)
binary = bin(num)[2:]
print(binary)
num = 10
binary = format(num, 'b')
print(binary)
def to_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary or '0'

print(to_binary(10))
binary = '1010'
num = int(binary, 2)
print(num)