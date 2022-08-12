import math
n = int(input('Diga um ângulo: '))
seno = math.sin(math.radians(n))
print('O seno desse ângulo é {:.2f}'.format(seno))
cos = math.cos(math.radians(n))
print('O cosseno desse ângulo é {:.2f}'.format(cos))
tan = math.tan(math.radians(n))
print('A tangente desse ângulo é {:.2f}.'.format(tan))