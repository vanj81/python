x = int(input("Введите число"))
print('Максимальная цифра в числе ', x, end = '')
max_digit = 0
while x%10 > 1:
    digit = x%10
    x //= 10
    if digit > max_digit:
        max_digit = digit
print(' - ', max_digit)
