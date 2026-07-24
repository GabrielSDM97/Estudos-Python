# Condicional para testar se uma determinada função de uma biblioteca está disponível para uso.

'''

import biblioteca

if hasattr(biblioteca, "função"):
    print("✅ Módulo disponível na biblioteca")
else:
    print("❌ Módulo NÃO disponível - biblioteca pode estar corrompida")

'''
