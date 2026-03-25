# Definindo valores booleanos para simular proposições
p = True   # Proposição p é Verdadeira
q = False  # Proposição q é Falsa

# 1. Operador AND (E lógico / Conjunção)
resultado_e = p and q  
# Lógica: V e F = F
print(f"p(V) ^ q(F) = {resultado_e}") 

# 2. Operador OR (Ou lógico / Disjunção Inclusiva)
resultado_ou = p or q    
# Lógica: V ou F = V
print(f"p(V) v q(F) = {resultado_ou}")

# 3. Operador NOT (Negação)
resultado_negação = not p    
# Lógica: não V = F
print(f"¬p(V) = {resultado_negação}")

# 4. Operador == (Igual a / Bicondicional)
resultado_igual = p == q   
# Lógica: V se e somente F = F
print(f"p(V) <=> q(F) = {resultado_igual}")

# 5. Operador != (Diferente de / Disjunção Exclusiva)
resultado_diferente = p != q   
# Lógica: ou V ou F = V
print(f"p(V)⊻ q(F) = {resultado_diferente}")