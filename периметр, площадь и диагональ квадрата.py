# Это я подсмотрел, я не знаю как высчетать диагональ
def square(sd):
    return (4 * sd, sd ** 2, (2 * sd ** 2) ** .5)


result = square(int(input("Введите сторону квадрата: ")))

print(result)