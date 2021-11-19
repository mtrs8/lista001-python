# 3) Celsius to Fahrenheit

def celsius2fahrenheit(temperatura):
    return (temperatura * 9/5) + 32

temperatura = float(input('Digite a temperatura em celsius: '))
print('{} celsius = {:.1f} fahrenheit'.format(temperatura, celsius2fahrenheit(temperatura)))


