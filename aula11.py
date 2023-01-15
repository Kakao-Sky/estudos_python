# Precedência dos operadores aritméticos

# 1. (n + n) - parênteses
# 2. **
# 3. * / // %
# 4. + - 
conta_1 = 1 + 1 ** 5 + 5 
conta_2 = (1 + 1) ** (5 + 5) 
conta_3 = (1 + 1) ** 5 + 5 
print(conta_1, conta_2, conta_3)