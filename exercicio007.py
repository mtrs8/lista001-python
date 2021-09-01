#Calcular Seno, cosseno, tangente, secante, co-tangente e co-secante
import math
figura_em_graus = 80
figura_em_rad = figura_em_graus * (3.14/180)

print("Cosseno: ", math.cos(figura_em_rad))
print("Seno: ", math.sin(figura_em_rad))
print("Tangente: ", math.tan(figura_em_rad))
print("Cotangente: ", 1 / math.tan(figura_em_rad))
print("Secante:", 1 / math.cos(figura_em_rad))
print("Cosecante: ", 1 / math.sin(figura_em_rad)) 