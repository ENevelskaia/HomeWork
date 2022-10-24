import pprint

cook_book = {}
with open('dishes.txt', 'rt', encoding="utf-8") as file:
    for line in file:
        dish_ingredients = []
        dish_name = line.strip()
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ingredients = file.readline()
            ingredient_name, quantity, measure = ingredients.strip().split(' | ')
            dish_ingredients.append({'ingredient_name': ingredient_name,
                                     'quantity': quantity,
                                     'measure': measure})

        cook_book[dish_name] = dish_ingredients
        blank_line = file.readline()


pprint.pprint(cook_book)

def get_shop_list_by_dishes(dish_list, person_count):
    ingredients_list = {}
    for dish in dish_list:
        dish_ingredient_list = cook_book[dish]
        for ingredient in dish_ingredient_list:
            product, qnty, meas = ingredient.values()
            if product not in ingredients_list.keys():
                ingredients_list[product] = {'measure': meas,'quantity': float(qnty)*person_count}
            else:
                ingredients_list[product]['quantity'] += float(qnty) * person_count

    return ingredients_list

menu = cook_book.keys()
pprint.pprint(get_shop_list_by_dishes(menu, 6))
