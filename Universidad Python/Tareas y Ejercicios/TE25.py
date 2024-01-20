def c_f(grados_celcius):
    grados_fahrenheit = (grados_celcius * 9/5) + 32
    return grados_fahrenheit


def f_c(grados_fahrenheit):
    grados_celcius = (grados_fahrenheit - 32) * 5/9
    return grados_celcius


grados_celcius = float(input('Dame los grados celcius que quieres convertir a Fahrenheit: '))
grados_fahrenheit = float(input('Dame los grados Fahrenheit que quieres convertir a Celcius: '))

print(c_f(grados_celcius))
print(f_c(grados_fahrenheit))
