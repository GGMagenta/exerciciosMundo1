# Pegue um ângulo e calcule o seno, cosseno e tangente
import math
a = float(input('digite um ângulo: '))
rad = math.radians(a)
print('O seno de {} e {:.2f}\no cosseno e {:.2f}\n e a tangente e {:.2f}'.format(a, math.sin(rad), math.cos(rad), math.tan(rad)))
