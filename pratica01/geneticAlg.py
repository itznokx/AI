import random as rng
class AlgoritmoGenetico:
    def __init__(self, problema, tamanho_populacao, geracoes, taxa_crossover, taxa_mutacao):
        self.problema = problema
        self.tamanho_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.taxa_crossover = taxa_crossover
        self.taxa_mutacao = taxa_mutacao
        self.melhores_custos_por_geracao = []

    def _selecionar(self, populacao, fitnesses):
        total_fitness = sum(fitnesses)
        if total_fitness == 0:
            return rng.choice(populacao)
        
        pick = rng.uniform(0, total_fitness)
        current = 0
        for individuo, fitness in zip(populacao, fitnesses):
            current += fitness
            if current > pick:
                return individuo
        return rng.choice(populacao) # Fallback

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

                if rng.rng() < self.taxa_crossover:
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
