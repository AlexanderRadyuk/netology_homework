cook_book = {
    'Омлет': [{
        'ingredient_name': 'Яйцо',
        'quantity': 2,
        'measure': 'шт.'
    }, {
        'ingredient_name': 'Молоко',
        'quantity': 100,
        'measure': 'мл'
    }, {
        'ingredient_name': 'Помидор',
        'quantity': 2,
        'measure': 'шт'
    }],
    'Утка по-пекински': [{
        'ingredient_name': 'Утка',
        'quantity': 1,
        'measure': 'шт'
    }, {
        'ingredient_name': 'Вода',
        'quantity': 2,
        'measure': 'л'
    }, {
        'ingredient_name': 'Мед',
        'quantity': 3,
        'measure': 'ст.л'
    }, {
        'ingredient_name': 'Соевый соус',
        'quantity': 60,
        'measure': 'мл'
    }],
    'Запеченный картофель': [
        {
            'ingredient_name': 'Картофель',
            'quantity': 1,
            'measure': 'кг'
        },
        {
            'ingredient_name': 'Чеснок',
            'quantity': 3,
            'measure': 'зубч'
        },
        {
            'ingredient_name': 'Сыр гауда',
            'quantity': 100,
            'measure': 'г'
        },
    ]
}



def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      # print(2, ingredient['quantity'], ingredient['measure'])
      new_shop_list_item = {'qauntity': ingredient['quantity'], 'measure': ingredient['measure']}
      # print(3, new_shop_list_item)
      new_shop_list_item['qauntity'] *= person_count
      # print(4, new_shop_list_item)
      ingredient_1 = ingredient['ingredient_name']
      if ingredient_1 not in shop_list:
        shop_list[ingredient_1] = new_shop_list_item
        # print(5, shop_list)
      else:
        shop_list[ingredient]['quantity'] += new_shop_list_item['quantity']
  return print(shop_list)

get_shop_list_by_dishes(['Омлет'], 3)

