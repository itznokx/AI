import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from missaoAerea import MissaoAerea 
from geneticAlg import AlgoritmoGenetico
# Índices dos locais
INDICES = {
    0: "Base Aérea",
    1: "Radar Inimigo",
    2: "Ponte Estratégica",
    3: "Depósito de Armas",
    4: "Porto Militar",
    5: "Fábrica de Munições"
}

# Matriz de distâncias
DISTANCIAS = [
    [0,  45, 30, 50, 65, 40],
    [45, 0,  55, 40, 60, 35],
    [30, 55, 0,  25, 40, 45],
    [50, 40, 25, 0,  30, 50],
    [65, 60, 40, 30, 0,  25],
    [40, 35, 45, 50, 25, 0]
]

# Níveis de risco
RISCOS = [0, 8, 3, 5, 6, 4]

CONSUMO_POR_KM = 2
CAPACIDADE_TANQUE = 500

# Globais Locais

TAMANHO_POPULACAO=100
GERACOES=500
TAXA_CROSSOVER=0.8
TAXA_MUTACAO=0.1

def main():
    m1 = MissaoAerea(CONSUMO_POR_KM,CAPACIDADE_TANQUE,INDICES,DISTANCIAS,RISCOS)
    ag = AlgoritmoGenetico(m1,TAMANHO_POPULACAO,GERACOES,TAXA_CROSSOVER,TAXA_MUTACAO)
    print("Resultados da Missao Aerea:")
    melhor_rota_indices, custo_total_rota = ag.executar()
    melhor_rota_nomes = [INDICES[i] for i in melhor_rota_indices]
    _, distancia_total_rota = m1.calcular_custo(melhor_rota_indices)
    consumo_rota = distancia_total_rota * m1.consumo_por_km
    print(f"Melhor rota encontrada (índices): {melhor_rota_indices}")
    print(f"Melhor rota encontrada (nomes): {melhor_rota_nomes}")
    print(f"Custo total dessa rota: {custo_total_rota:.2f}")
    print(f"Distância total percorrida: {distancia_total_rota:.2f} km")
    print(f"Consumo de combustível da rota: {consumo_rota:.2f} litros")
    print(f"Capacidade do tanque: {m1.capacidade_tanque} litros")
    print(f"A missão é viável com o combustível disponível? {'Sim' if (consumo_rota <= m1.capacidade_tanque) else 'Não'}")
    # Plotar gráfico de custo
    plt.figure(figsize=(10, 6))
    plt.plot(ag.melhores_custos_por_geracao)
    plt.title('Melhor Custo por Geração')
    plt.xlabel('Geração')
    plt.ylabel('Custo Total')
    plt.grid(True)
    plt.show()
main()



