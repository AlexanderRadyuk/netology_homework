cooking_book = {}
ingredients_list = []
ingredients_count = []
dishes_list = []

with open('recipe.txt') as f:
  for line in f.readlines():
    line = line.strip()
    if '|' in line:
      ingredients_list.append(line)
    elif line.isdigit():
      ingredients_count.append(line)
    elif line == '':
      pass
    else:
      cooking_book[line] = None
      dishes_list.append(line)

dish_component = dict.fromkeys(
    ['ingredient_name: ', 'quantity: ', 'measure: '])
dish_number = 0
component_number = 0
idx = 0

# Этот цикл не доработан, но в нем запутался вообще в попытке заполнить словарь
while idx <= int(ingredients_count[dish_number]):
  for entity_ in ingredients_list:
    dish_component['ingredient_name: '] = entity_.split('|')[0]
    dish_component['quantity: '] = entity_.split('|')[1]
    dish_component['measure: '] = entity_.split('|')[2]
    cooking_book[dishes_list[dish_number]] = dish_component.copy()
    component_number += 1
    idx += 1
print(cooking_book)