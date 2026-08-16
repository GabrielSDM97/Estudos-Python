from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.7')
print('Com função \'decimal\'')
print(a + b)

print('Sem função \'decimal\'')
print(f'{0.1 + 0.7}')

# Em python, valores float as vezes não são tão precisos, sendo necessário utilizar a biblioteca 'decimal'.
