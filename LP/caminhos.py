distancia_AB = int(input('Digite a distância entre A e B: '))
distancia_AC = int(input('Digite a distância entre A e C: '))
distancia_BD = int(input('Digite a distância entre B e D: '))
distancia_BE = int(input('Digite a distância entre B e E: '))
distancia_CF = int(input('Digite a distância entre C e F: '))
distancia_CG = int(input('Digite a distância entre C e G: '))

if distancia_AB < distancia_AC:
   print('Trajeto Inicial: A -> B')
   trajeto_inicial = 'A -> B'
   soma1 = distancia_AB
else:
    print('Trajeto Inicial: A -> C')
    trajeto_inicial2 = 'A -> C'
    soma1 = distancia_AC

if distancia_BD > distancia_BE:
    print('Trajeto Médio: B -> E')
    trajeto_medio = 'B -> E'
    soma2 = distancia_BE
else:
    print('Trajeto Médio: B -> D')
    trajeto_medio2 = 'B -> D'
    soma2 = distancia_BD
    
if distancia_CF < distancia_CG:
    print('Trajeto Final: C -> F')
    trajeto_final = 'C -> F'
    soma3 = distancia_CF
else:
    print('Trajeto Final: C -> G')
    trajeto_final = 'C -> G'
    soma3 = distancia_CG

soma_trajeto = soma1 + soma2 + soma3
print(f"A distância total do trajeto é: {soma_trajeto}")

trajeto_completo = trajeto_inicial + ' -> ' + trajeto_medio + ' -> ' + trajeto_final
print(f"Trajeto Completo: {trajeto_completo}")



