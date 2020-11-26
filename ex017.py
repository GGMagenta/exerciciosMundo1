# Pegue a medida dos catetos e calcule a hipotenusa
import math
catetoOp = float(input('comprimento do cateto oposto: '))
catetoAd = float(input('comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetoOp,catetoAd)
print('a hipotenusa e {}'.format(hipotenusa))
