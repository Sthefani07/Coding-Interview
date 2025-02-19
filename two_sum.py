class Solution:
    def twoSum(self, nums, target):
        num_dicionario = {}

        for index, num in enumerate(nums):
            missing = target - num
            if missing in num_dicionario:
                return [num_dicionario[missing], index]
            num_dicionario[num] = index
        
        return []    

# Criamos um objeto da classe Solution
sol = Solution()

# Chamamos o método corretamente usando o objeto
print(sol.twoSum([2, 7, 11, 15], 9))  # ✅ Retorna [0, 1]
print(sol.twoSum([3, 2, 4], 6))  # ✅ Retorna [1, 2]
print(sol.twoSum([1, 5, 3, 7], 8))  # ✅ Retorna [1, 2]
