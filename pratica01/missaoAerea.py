import random as rng
from abc import ABC, abstractmethod

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
        pass
class MissaoAerea(ProblemInterface):
    def __init__ (self,consume,tank_capacity,index,distances,risks):
        self.consumo_por_km = consume
        self.capacidade_tanque = tank_capacity
        self.indices = index
        self.distancias = distances
        self.riscos = risks
        self.chaves = list(index.keys())

    def gerar_individuo(self):
        caminho = list(range(1, len(self.chaves)))  # Alvos (exceto a base)
        rng.shuffle(caminho)
        return [0] + caminho + [0]

    def calcular_custo(self, individuo) -> float: #Calcula custo total (distancia_total + 5x risco_total) e a distancia
        distancia_total = 0;
        riscos_soma = 0;
        old = 0;
        for x in individuo:
            distancia_total += self.distancias[old][x]
            riscos_soma += self.riscos[x]
            old = x
        return (distancia_total+(riscos_soma*5)),distancia_total
    def calcular_fitness(self, individuo):
        custo_total, _ = self.calcular_custo(individuo)
        if (custo_total > 0):
            return 1/custo_total
        else:
            return float(inf)

    def fill_offspring(self,offspring_target_middle, parent_source_middle, mapping_dict_source_to_target,cut1,cut2,size):
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

        cut1, cut2 = sorted(rng.sample(range(size), 2))

        offspring1_meio[cut1:cut2] = p1_meio[cut1:cut2]
        offspring2_meio[cut1:cut2] = p2_meio[cut1:cut2]

        map_p1_to_p2 = {p1_meio[i]: p2_meio[i] for i in range(cut1, cut2)}
        map_p2_to_p1 = {p2_meio[i]: p1_meio[i] for i in range(cut1, cut2)}


        offspring1_meio = self.fill_offspring(offspring1_meio, p2_meio, map_p2_to_p1,cut1,cut2,size)
        offspring2_meio = self.fill_offspring(offspring2_meio, p1_meio, map_p1_to_p2,cut1,cut2,size)

        return [0] + offspring1_meio + [0], [0] + offspring2_meio + [0]
    def mutacao(self, individuo, taxa_mutacao):
        if rng.rng() < taxa_mutacao:
            # Não mutar a base (índice 0 e último)
            indices_mutaveis = list(range(1, len(individuo) - 1))
            if len(indices_mutaveis) >= 2:
                idx1, idx2 = rng.sample(indices_mutaveis, 2)
                individuo[idx1], individuo[idx2] = individuo[idx2], individuo[idx1]
        return individuo