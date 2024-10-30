import random
import time
import numpy
import matplotlib.pyplot as plt

# Função para gerar gráficos
def gerar_graficos(tamanhos, valores_dinamica, valores_guloso, tempos_dinamica, tempos_guloso):

    # Gráfico 1: Valor total de venda
    plt.figure(figsize=(10, 5))
    plt.plot(tamanhos, valores_dinamica, label='Dynamic Programming', marker='o')
    plt.plot(tamanhos, valores_guloso, label='Greedy', marker='x')
    plt.xlabel('n')
    plt.ylabel('Valor Total de Venda')
    plt.title('Valor Total de Venda - Dynamic Programming vs. Greedy')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico 2: Tempo de Execução
    plt.figure(figsize=(10, 5))
    plt.plot(tamanhos, tempos_dinamica, label='Dynamic Programming', marker='o')
    plt.plot(tamanhos, tempos_guloso, label='Greedy', marker='x')
    plt.xlabel('n')
    plt.ylabel('Tempo de Execução)')
    plt.title('Tempo de Execução - Dynamic Programming vs. Greedy')
    plt.legend()
    plt.grid(True)
    plt.show()

# Função para gerar preços aleatórios
def gerar_precos(n):
    precos = [random.randint(1, 3 * n) for i in range(1, n+1)]
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

"""
precos = [1, 20, 33, 36]
tamanho = 4
resultado_dinamico = dinamica(precos, tamanho) # Esperado: 40
resultado_guloso = guloso(precos, tamanho) # Esperado: 34

print(f"Resultado Dinâmico: {resultado_dinamico}")
print(f"Resultado Guloso: {resultado_guloso}")
"""

# Execução dos experimentos
def executar_experimentos(inc, fim, stp):

    tamanhos = []
    valores_dinamica = []
    valores_guloso = []
    tempos_dinamica = []
    tempos_guloso = []

    print(" n     vDP  tDP      vGreedy tGreedy       %")
    print("-" * 44)

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

        tamanhos.append(n)
        valores_dinamica.append(vDP)
        valores_guloso.append(vGreedy)
        tempos_dinamica.append(tDP)
        tempos_guloso.append(tGreedy)

    return tamanhos, valores_dinamica, valores_guloso, tempos_dinamica, tempos_guloso

# Parâmetros dos experimentos
inc = 1000
fim = 20000
stp = 1000

# Execução dos experimentos e coleta dos dados
tamanhos, valores_dinamica, valores_guloso, tempos_dinamica, tempos_guloso = executar_experimentos(inc, fim, stp)

# Geração dos gráficos
gerar_graficos(tamanhos, valores_dinamica, valores_guloso, tempos_dinamica, tempos_guloso)