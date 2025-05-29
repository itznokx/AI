import random
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

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

# Especificações da Aeronave
CONSUMO_POR_KM = 2  # litros/km
CAPACIDADE_TANQUE = 500  # litros

class ProblemInterface(ABC):
    """Interface que define as operações específicas do problema"""

    @abstractmethod
    def gerar_individuo(self):
        """Gera um indivíduo aleatório"""
        pass

    @abstractmethod
    def calcular_fitness(self, individuo):
        """Calcula o fitness de um indivíduo"""
        pass

    @abstractmethod
    def crossover(self, pai1, pai2):
        """Realiza crossover entre dois pais"""
        pass

    @abstractmethod
    def mutacao(self, individuo, taxa_mutacao):
        """Aplica mutação em um indivíduo"""
        pass

class MissaoAerea(ProblemInterface):
    def __init__(self):
        self.num_locais = len(INDICES)

    def gerar_individuo(self):
        """Gera uma rota aleatória começando na base (índice 0) e retornando a ela."""
        locais_intermediarios = list(range(1, self.num_locais))  # Alvos (exceto a base)
        random.shuffle(locais_intermediarios)
        # A rota começa na base, visita os alvos intermediários, e retorna à base.
        # [Base, Alvo1, Alvo2, ..., AlvoN, Base]
        return [0] + locais_intermediarios + [0]

    def calcular_custo(self, individuo):
        """Calcula o custo total de uma rota."""
        distancia_total = 0
        soma_riscos = 0

        # Calcular distância total e soma dos riscos
        for i in range(len(individuo) - 1):
            origem = individuo[i]
            destino = individuo[i+1]
            distancia_total += DISTANCIAS[origem][destino]
            if destino != 0: # Não considerar o risco da base na soma, mas sim o risco dos alvos
                soma_riscos += RISCOS[destino]

        # Custo Total = Distância Total + (Soma dos Riscos × 5)
        custo_total = distancia_total + (soma_riscos * 5)
        return custo_total, distancia_total

    def calcular_fitness(self, individuo):
        """Calcula o fitness de um indivíduo."""
        custo_total, _ = self.calcular_custo(individuo)
        # Fitness = 1 / Custo Total. Para evitar divisão por zero, caso o custo seja 0.
        return 1 / custo_total if custo_total > 0 else float('inf')

    class MissaoAerea(ProblemInterface):
   def __init__ (self,consume,tank_capacity,index,distances,risks):
        self.consumo_por_km = consume
        self.capacidade_tanque = tank_capacity
        self.indices = index
        self.distancias = distances
        self.riscos = risks
        self.chaves = list(index.keys())

    def gerar_individuo(self):
        caminho = list(range(1, self.chaves))  # Alvos (exceto a base)
        random.shuffle(caminho)
        return [0] + caminho + [0]
    def custo_total(self, individuo) -> float: #Calcula custo total (distancia_total + 5x risco_total) e a distancia
        distancia_total = 0;
        riscos_soma = 0;
        old = 0;
        for x in individuo:
            distancia_total += self.distancias[old][x]
            riscos_soma += self.riscos[x]
            old = x
        return (custo_total+(riscos_soma*5)),distancia_total
    def calcular_fitness(self, individuo):
        custo_total, _ = self.calcular_custo(individuo)
        if (custo_total > 0):
            return 1/custo_total
        else:
            return float(inf)
    def fill_offspring(offspring_target_middle, parent_source_middle, mapping_dict_source_to_target):
        copied_segment_values = set(offspring_target_middle[cut1:cut2])
        for i in range(size):
            if i < cut1 or i >= cut2:
                gene_padrao = parent_source_middle[i]

                geracao_atual = gene_padrao
                while geracao_atual in copied_segment_values:
                    if geracao_atual in mapping_dict_source_to_target:
                        geracao_atual = mapping_dict_source_to_target[geracao_atual]
                    else:
                        break
                offspring_target_middle[i] = geracao_atual
        return offspring_target_middle
    def crossover(self, parent1, parent2):
        size = len(parent1) - 2 # Exclui a base do início e do fim
        p1_meio = parent1[1:-1]
        p2_meio = parent2[1:-1]

        offspring1_meio = [None] * size
        offspring2_meio = [None] * size

        cut1, cut2 = sorted(random.sample(range(size), 2))

        offspring1_meio[cut1:cut2] = p1_meio[cut1:cut2]
        offspring2_meio[cut1:cut2] = p2_meio[cut1:cut2]

        map_p1_to_p2 = {p1_meio[i]: p2_meio[i] for i in range(cut1, cut2)}
        map_p2_to_p1 = {p2_meio[i]: p1_meio[i] for i in range(cut1, cut2)}

    
        offspring1_meio = fill_offspring(offspring1_meio, p2_meio, map_p2_to_p1)
        offspring2_meio = fill_offspring(offspring2_meio, p1_meio, map_p1_to_p2)
    
        return [0] + offspring1_meio + [0], [0] + offspring2_meio + [0]
    def mutacao(self, individuo, taxa_mutacao):
        """
        Aplica mutação em um indivíduo sem mover a base.
        Troca aleatoriamente dois alvos intermediários.
        """
        if random.random() < taxa_mutacao:
            # Não mutar a base (índice 0 e último)
            indices_mutaveis = list(range(1, len(individuo) - 1))
            if len(indices_mutaveis) >= 2:
                idx1, idx2 = random.sample(indices_mutaveis, 2)
                individuo[idx1], individuo[idx2] = individuo[idx2], individuo[idx1]
        return individuo

# Algoritmo Genético
class AlgoritmoGenetico:
    def __init__(self, problema, tamanho_populacao, geracoes, taxa_crossover, taxa_mutacao):
        self.problema = problema
        self.tamanho_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.taxa_crossover = taxa_crossover
        self.taxa_mutacao = taxa_mutacao
        self.melhores_custos_por_geracao = []

    def _selecionar(self, populacao, fitnesses):
        """Seleção por roleta."""
        total_fitness = sum(fitnesses)
        if total_fitness == 0:
            # If all fitness are zero (e.g., very high costs), select randomly
            return random.choice(populacao)
        
        pick = random.uniform(0, total_fitness)
        current = 0
        for individuo, fitness in zip(populacao, fitnesses):
            current += fitness
            if current > pick:
                return individuo
        return random.choice(populacao) # Fallback

    def executar(self):
        populacao = [self.problema.gerar_individuo() for _ in range(self.tamanho_populacao)]
        melhor_individuo = None
        melhor_custo = float('inf')

        for geracao in range(self.geracoes):
            fitnesses = [self.problema.calcular_fitness(ind) for ind in populacao]
            
            # Encontra o melhor da geração atual
            melhor_fitness_geracao = -1
            melhor_individuo_geracao = None
            for i, individuo in enumerate(populacao):
                if fitnesses[i] > melhor_fitness_geracao:
                    melhor_fitness_geracao = fitnesses[i]
                    melhor_individuo_geracao = individuo
            
            custo_melhor_geracao, _ = self.problema.calcular_custo(melhor_individuo_geracao)
            self.melhores_custos_por_geracao.append(custo_melhor_geracao)

            if custo_melhor_geracao < melhor_custo:
                melhor_custo = custo_melhor_geracao
                melhor_individuo = melhor_individuo_geracao

            nova_populacao = []
            while len(nova_populacao) < self.tamanho_populacao:
                pai1 = self._selecionar(populacao, fitnesses)
                pai2 = self._selecionar(populacao, fitnesses)

                if random.random() < self.taxa_crossover:
                    filho1, filho2 = self.problema.crossover(pai1, pai2)
                else:
                    filho1, filho2 = pai1, pai2

                filho1 = self.problema.mutacao(filho1, self.taxa_mutacao)
                filho2 = self.problema.mutacao(filho2, self.taxa_mutacao)

                nova_populacao.append(filho1)
                if len(nova_populacao) < self.tamanho_populacao:
                    nova_populacao.append(filho2)

            populacao = nova_populacao

        return melhor_individuo, melhor_custo

# Execução
problema = MissaoAerea()
ag = AlgoritmoGenetico(
    problema=problema,
    tamanho_populacao=100,
    geracoes=500,
    taxa_crossover=0.8,
    taxa_mutacao=0.1
)

melhor_rota_indices, custo_total_rota = ag.executar()

# Obter a rota em nomes
melhor_rota_nomes = [INDICES[i] for i in melhor_rota_indices]

# Calcular distância total para a melhor rota
_, distancia_total_rota = problema.calcular_custo(melhor_rota_indices)

# Verificar viabilidade
consumo_rota = distancia_total_rota * CONSUMO_POR_KM
missao_viavel = consumo_rota <= CAPACIDADE_TANQUE

print("Resultados do Algoritmo Genético:")
print(f"Melhor rota encontrada (índices): {melhor_rota_indices}")
print(f"Melhor rota encontrada (nomes): {melhor_rota_nomes}")
print(f"Custo total dessa rota: {custo_total_rota:.2f}")
print(f"Distância total percorrida: {distancia_total_rota:.2f} km")
print(f"Consumo de combustível da rota: {consumo_rota:.2f} litros")
print(f"Capacidade do tanque: {CAPACIDADE_TANQUE} litros")
print(f"A missão é viável com o combustível disponível? {'Sim' if missao_viavel else 'Não'}")

# Plotar gráfico de custo
plt.figure(figsize=(10, 6))
plt.plot(ag.melhores_custos_por_geracao)
plt.title('Melhor Custo por Geração')
plt.xlabel('Geração')
plt.ylabel('Custo Total')
plt.grid(True)
plt.show()