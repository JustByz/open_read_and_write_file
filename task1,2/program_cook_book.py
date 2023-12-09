import os.path

def file_reader(file_name):
    result = {}
    p = os.path.dirname(os.path.abspath(__file__))
    with open(f'{p}\\recipes.txt', encoding='utf-8') as recipes:
        heads = ['ingredient_name', 'quantity', 'measure']
        for line in recipes:
            dish_name = line.strip()
            result[dish_name] = []
            components_number = recipes.readline()
            for component in range(int(components_number)):
                component = recipes.readline().strip().split(' | ')
                component_dict = dict(zip(heads, component))
                result[dish_name].append(component_dict)
            recipes.readline()
    return result


def get_shop_list_by_dishes(*dishes, person_count):
    cook_book = file_reader('recipes.txt')
    result_list = {}
    cook_book_lower = dict((k.lower(), v) for k, v in cook_book.items())
    for dish in dishes:
        if dish.lower() in cook_book_lower:
            for component in cook_book[dish]:
                if component['ingredient_name'] not in result_list:
                    result_list[component['ingredient_name']] = {}
                    result_list[component['ingredient_name']]['measure'] = component['measure']
                    result_list[component['ingredient_name']]['quantity'] = int(component['quantity']) * person_count
                else:
                    result_list[component['ingredient_name']]['quantity'] += int(component['quantity']) * person_count
        else:
            print(f'В кулинарной книге нет блюда {dish}\n')
    return result_list


print(file_reader('recipes.txt'))
print(get_shop_list_by_dishes('Омлет', 'Фахитос', 'Уха', person_count = 2))