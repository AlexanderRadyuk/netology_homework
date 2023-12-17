cooking_book = {}
ingredient_content = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
ingredients_count = []
dishes_list = []




with open('recipe.txt') as f:
  file_ = f.read()

dishes_list = file_.split('\n')


for dish in dishes_list:

  if dish.isdigit() == False and '|' not in dish and dish != '':
    cooking_book[dish] = None
    name = dish

  elif dish.isdigit() == True:

    count_ = int(dish)

  elif dish != '' and '|' in dish:

    ingredient = dish.strip().split('|')
    ingredient_content['ingredient_name'] = ingredient[0]
    ingredient_content['quantity'] = ingredient[1]
    ingredient_content['measure'] = ingredient[2]
    ingredients_count.append(ingredient_content.copy())
    cooking_book[name] = ingredients_count

  elif dish == '':
    ingredients_count = []



print(cooking_book)

