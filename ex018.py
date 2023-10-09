from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O seno de {}º vale {:.2f}'.format(ang, seno))
print('O cosseno de {}º vale {:.2f}'.format(ang, cosseno))
print('A tangente de {}º vale {:.2f}'.format(ang, tangente))

