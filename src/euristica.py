# exemplo de euristica simples

pesos = {'car': 1, 'bus': 2, 'truck': 3}


def calcular_peso(modais, pesos):
    total = 0
    for modal, quantidade in modais.items():
        total += quantidade * pesos.get(modal, 1) #exemplo de calculo de pesos
    return total


modais_ns = {'car': 3, 'bus': 2} # nome e quantidade, norte-sul

modais_lo = {'car': 5, 'truck': 0} # leste-oeste

Wns = calcular_peso(modais_ns, pesos)
Wlo = calcular_peso(modais_lo, pesos)


# decisão sobre qual semáforo abrir
if Wns > Wlo:
    print("Abrir semáforo para Norte-Sul")
    print("retorna 1 para o semaforo")
elif Wlo > Wns:
    print("Abrir semáforo para Leste-Oeste")
    print("retorna 2 para o semaforo")
else:
    print("Semáforos terao um tempo x para ficar aberto")