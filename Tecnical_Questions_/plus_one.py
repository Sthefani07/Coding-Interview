from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits) - 1, -1, -1):       # Por que percorremos a lista de trás para frente?  Porque a soma começa pelo último dígito, assim como fazemos com a soma manual de números.
            if digits[i] == 9:                         #  O que acontece se o dígito atual for 9?  Definimos como 0, pois 9 + 1 = 10, e o 1 precisa ser "carregado" para a esquerda.
                digits[i] = 0  
            else:
                digits[i] = digits[i] + 1              # O que significa essa linha? → Estamos somando 1 ao dígito atual e retornando a lista modificada, pois não há mais carry-over.
                return digits                          #  Por que retornamos aqui? → Porque se não há mais necessidade de carregar 1, podemos devolver o resultado imediatamente.
        return [1] + digits                            # O que significa essa linha? → Se todos os dígitos eram 9 (ex: [9,9,9]), precisamos adicionar um novo 1 na frente para representar 1000.




if __name__ == "__main__":                             #  Como testamos nosso código? → Criamos instâncias da classe `Solution` e chamamos `plusOne` com diferentes entradas.
    sol = Solution()
    
 
    test_cases = [
        [1, 2, 3],     # → O número 123 vira 124
        [4, 3, 2, 1],  # → O número 4321 vira 4322
        [9, 9, 9],     # → O número 999 vira 1000
        [0]            # → O número 0 vira 1
    ]

    # O que esse loop faz?  → Ele percorre cada caso de teste, chama a função e imprime o resultado para verificar se está correto.
    for case in test_cases:
        print(f"Input: {case} -> Output: {sol.plusOne(case)}")


