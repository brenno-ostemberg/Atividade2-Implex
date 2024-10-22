import random
import time
import numpy

def gerar_precos(n):
    precos = [random.randint(1, n) for i in range(1, n+1)]
    precos.sort()
    return precos

def dinamica(precos, n):

    if n == 0:
        return 0

    q = float("-inf")
 
    for i in range(1, n + 1):
        q = max(q, precos[i - 1] + dinamica(precos, n - i))

    return q

def guloso(precos, n):
    precos.sort(reverse=True)
    valor_total = 0
    while n > 0:
        for preco in precos:
            if preco <= n:
                valor_total += preco
                n -= preco
                break
    return valor_total

def executar_experimentos(inc, fim, stp): 
    for n in range(inc, fim+1, stp):
        precos = gerar_precos(n)

        inicio_pd = time.time()
        valor_pd = dinamica(precos, n)
        tempo_pd = time.time() - inicio_pd
        
        inicio_greedy = time.time()
        valor_greedy = guloso(precos, n)
        tempo_greedy = time.time() - inicio_greedy
        
        porcentagem = (valor_greedy / valor_pd) * 100
        
        print(f"{n}: vPD={valor_pd} tPD={tempo_pd:.6f}s | vGreedy={valor_greedy} tGreedy={tempo_greedy:.6f}s | %={porcentagem:.2f}%")

inc = 1000
fim = 20000
spt = 1000

executar_experimentos(inc, fim, spt)
