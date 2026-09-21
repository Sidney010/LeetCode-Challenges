"""
🧠 Two Sum (Dois Somas)
📌 Descrição do Problema
O problema Two Sum é um dos desafios mais clássicos e famosos de lógica e algoritmos (frequentemente encontrado em plataformas como o LeetCode).

A premissa é simples:
Dado um array de números inteiros (nums) e um número inteiro alvo (target), você deve encontrar os índices de dois números dentro desse array cuja soma seja exatamente igual ao target.

📋 Regras e Premissas
Cada entrada terá exatamente uma única solução.

Você não pode usar o mesmo elemento duas vezes (ou seja, os dois índices devem ser diferentes).

Você pode retornar a resposta em qualquer ordem.

🔍 Exemplos Práticos
Exemplo 1:
Entrada: nums = [2, 7, 11, 15], target = 9

Saída: [0, 1]

Explicação: Porque nums[0] + nums[1] (2 + 7) é igual a 9.

Exemplo 2:
Entrada: nums = [3, 2, 4], target = 6

Saída: [1, 2]

Explicação: Porque nums[1] + nums[2] (2 + 4) é igual a 6.

💡 Abordagens de Resolução
1. Abordagem Força Bruta (O(n²))
Como funciona: Utiliza dois loops for aninhados para testar todas as combinações possíveis de pares de números até encontrar a soma correta.

Prós: Lógica muito simples de entender e implementar.

Contras: Muito lenta para arrays grandes, pois o número de operações cresce de forma quadrática.

2. Abordagem Otimizada com Hash Map / Dicionário (O(n))
Como funciona: Percorre o array apenas uma vez. Em cada passo, calcula o complemento necessário para atingir o alvo (target - número atual). Se o complemento já estiver salvo em um dicionário de números "já vistos", a resposta é encontrada imediatamente. Caso contrário, o número atual é salvo no dicionário e o loop continua.

Prós: Extremamente rápida e eficiente (tempo linear).

Contras: Exige um consumo levemente maior de memória para armazenar o dicionário.
"""

class Solution(object):

    # Solução mais simples porem com compexiade O elevado a 2 (quadratica)
    def twoSum1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j] # faz todas as somas possiveis para achar os dois que somados geram o codigo
                # comparando como um bumble sort
                # com um array de  de 10 numeros geram 100 comparaçãoes
                
    # Solução mais complexa porem com complexibilidade O de n (linear)
    def twoSum2(self, nums, target):
        vistos = {} # cria um dicionario, nele iremos guardar seu complemento e sua chave para fazer o minimo de comparações
        # ou seja, os numeros que ja vimos, se o alvo for 9 e o item avaliado for 2, basta achar um 7 (complemento)

        for i, num in enumerate(nums): # neste for ele pega o incremento e conteudo do array
            complete = target - num # salva o completo, diferenca do alvo
            
            if complete in vistos: # comparamos se os complementos aprecem nos numeros ja vistos
                return [vistos[complete], i] # se encontararmos enviamos o output e acabamos por aqui
            
            vistos[num] = i # senão adicionamos ele no dicionario


#  Testando a função
if __name__ == "__main__":
    solucao = Solution()
    
    # Teste 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Resultado 1: {solucao.twoSum1(nums1, target1)}")  # Esperado: [0, 1]
    
    # Teste 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Resultado 2: {solucao.twoSum1(nums2, target2)}")  # Esperado: [1, 2]