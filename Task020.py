#определить, присутствует ли в заданном списке строк некоторое число
from unicodedata import digit


lst=['2', 'ghj', '22', 'rty']
for x in lst:
    if x.isdigit():
        print(f'в списке присутствует число {x}')

if '4' in lst:
    print('присутствует')
else:
    print('нет')

