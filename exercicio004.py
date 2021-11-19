# 4) Imprimir a conversao de 0° a 100°C

def celsius2fahrenheit(temperatura):
    return (temperatura * 9/5) + 32

for i in range(100):
    print('{}°C = {}°F'.format(i, celsius2fahrenheit(i)))