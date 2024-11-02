class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Implementando Binary Search
        esquerda, direita = 0, len(nums)-1
        # Valores de esquerda e direita
        while esquerda <= direita:
            # Se os dois se encontrarem acaba
            meio = (esquerda + direita)// 2
            # Isso é dinamico.
            if nums[meio] < target: 
                esquerda = meio + 1 
                # Se o meio for maior que o objetivo
                # O ponteiro da esquerda recebe o valor do meio mais um, para cortar o que vem antes do meio
            elif nums[meio] > target:
                direita = meio - 1
                # Se o meio for menor que o objetivo
                # O ponteiro da direita recebe o valor do meio menos um, para cortar o que vem depois do meio
            else: 
                return meio
                # Como é dinamico o meio vai ser igual ao objetivo
        return -1
        # Se não houver o valor na tabela ele retornará -1
        
