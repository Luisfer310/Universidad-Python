# Calculadora de impuesto
def calcular_impuesto(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)


pagoSinImpuesto = int(input('Proporcione el pago sin impuesto: '))
imPuesto = int(input('Proporcione el monto del impuesto: '))
pago_total = calcular_impuesto(pagoSinImpuesto, imPuesto)
print(pago_total)
