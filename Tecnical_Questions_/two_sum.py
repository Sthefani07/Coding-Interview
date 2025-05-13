from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary_tracker = {}                              # O que esse dicionário armazena? → Ele guarda números já vistos e seus respectivos índices.
        for index, num in enumerate(nums):                   # O que enumerate faz? → Ele retorna o índice e o valor do elemento na lista.
            missing = target - num                           # Por que calculamos isso? → Precisamos encontrar esse valor em num_indices para formar a soma desejada.
            if missing in dictionary_tracker:                # O que estamos verificando aqui? → Se já vimos o número necessário para formar o target.
                return [dictionary_tracker[missing], index]  # Por que retornamos esses índices? → Porque eles correspondem ao par cuja soma é target.
            dictionary_tracker[num] = index                  # Por que armazenamos isso no dicionário? → Para lembrar onde vimos esse número antes.
        return[]                                             # Em que situação essa linha será executada? → Se não houver uma solução, mas o problema garante que sempre há uma.   

# Criamos um objeto da classe Solution
sol = Solution()

# Chamamos o método corretamente usando o objeto
print(sol.twoSum([2, 7, 11, 15], 9))  # ✅ Retorna [0, 1]
print(sol.twoSum([3, 2, 4], 6))  # ✅ Retorna [1, 2]
print(sol.twoSum([1, 5, 3, 7], 8))  # ✅ Retorna [1, 2]



# Review the two sum -- 
