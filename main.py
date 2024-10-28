import random
import time
import numpy

def gerar_precos(n):
    precos = [random.randint(1, n) for i in range(1, n+1)]
    precos.sort()
    return precos

# Implementação da Programação Dinâmica usando estratégia: Bottom-Up 
def dinamica(precos, n):

    r = [0] * (n+1)

    for j in range(1, n+1):

        q = float('-inf')

        for i in range(1, j+1):
            q = max(q, precos[i-1] + r[j-i])

        r[j] = q

    return r[n]

# Implementação do Algoritmo Guloso
def guloso(precos, n):

    densidades = [(precos[i] / (i + 1), i + 1) for i in range(n)]
    densidades.sort(reverse=True)

    valor_total = 0
    tamanho_restante = n 

    for densidade, tamanho in densidades:

        while tamanho_restante >= tamanho:
            valor_total += precos[tamanho-1]
            tamanho_restante -= tamanho
        
    return valor_total

#precos = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
#tamanho = 4
#resultado_dinamico = dinamica(precos, tamanho) # Resultado Esperado = 10
#resultado_guloso = guloso(precos, tamanho) # Resultado Esperado = 9

#print(f"Resultado Dinâmico: {resultado_dinamico}")
#print(f"Resultado Guloso: {resultado_guloso}")

def executar_experimentos(inc, fim, stp):
    print(" n     vDP  tDP      vGreedy tGreedy       %")
    print("-" * 60)

    for n in range(inc, fim + 1, stp):

        precos = gerar_precos(n)

        inicio = time.time()
        vDP = dinamica(precos, n)
        tDP = time.time() - inicio

        inicio = time.time()
        vGreedy = guloso(precos, n)
        tGreedy = time.time() - inicio

        porcentagem = (vGreedy / vDP) * 100

        print(f"{n:5d} {vDP:5d} {tDP:8.6f} {vGreedy:7d} {tGreedy:8.6f} {porcentagem:6.2f}")

inc = 1000
fim = 3000
spt = 1000

executar_experimentos(inc, fim, spt)
