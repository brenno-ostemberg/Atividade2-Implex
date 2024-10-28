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

precos = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
tamanho = 4
resultado_dinamico = dinamica(precos, tamanho)
resultado_guloso = guloso(precos, tamanho)

print(f"Resultado Dinâmico: {resultado_dinamico}")
print(f"Resultado Guloso: {resultado_guloso}")

#def executar_experimentos(inc, fim, stp): 
#    for n in range(inc, fim+1, stp):
#        precos = gerar_precos(n)
#
#        inicio_pd = time.time()
#        valor_pd = dinamica(precos, n)
#        tempo_pd = time.time() - inicio_pd
#       
#        inicio_greedy = time.time()
#        valor_greedy = guloso(precos, n)
#        tempo_greedy = time.time() - inicio_greedy
#        
#        porcentagem = (valor_greedy / valor_pd) * 100
#        
#        print(f"{n}: vPD={valor_pd} tPD={tempo_pd:.6f}s | vGreedy={valor_greedy} tGreedy={tempo_greedy:.6f}s | %={porcentagem:.2f}%")

#inc = 1000
#fim = 20000
#spt = 1000

#executar_experimentos(inc, fim, spt)
