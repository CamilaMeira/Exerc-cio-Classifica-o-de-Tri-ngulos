print('-='*20)
print('Analisador de triangulos')
print('-='*20)
r1=float(input('Primeiro segmento:'))
r2=float(input('Segundo segmento:'))
r3=float(input('Terceiro segmento:'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima nao podem formar triangulo')
if r1==r2==r3:
    print('Esse triangulo recebe o nome de Escaleno')
elif r1==r2:
    print('Esse triangulo recebe o nome de Isósceles')
elif r1!=r2!=r3:
    print('Esse triangulo recebe o nome de Equilátero')
