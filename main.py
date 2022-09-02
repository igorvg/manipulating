from pprint import pprint
import os 

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_name in dishes:
        if dish_name in cook_book.keys():
            for ingred in cook_book[dish_name]:
                ingredient = ingred['ingredient_name']
                quantity = int(ingred['quantity']) * person_count
                measure = ingred['measure']
                if ingredient not in shop_list.keys():
                    shop_list[ingredient] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient]['quantity'] += quantity
        else:
            print(f'Блюдо {dish_name} не найдено')
    return shop_list

def open_txt():
    path = os.getcwd()
    file_name = 'recipes.txt'
    full_path = os.path.join(path, file_name)
    with open(full_path) as file_obj:
        cook_book = {}  
        for item in file_obj:
            key = item.strip()
            for line in file_obj:
                quantity = int(line)
                lines = []
                for item in range(quantity):
                    data = file_obj.readline().strip().split('|')
                    keys = ['ingredient_name','quantity','measure']
                    temp_data = []
                    for items in data:
                        stripped = items.strip()
                        temp_data.append(stripped)
                    sorted = dict(zip(keys, temp_data))
                    lines.append(sorted)
                cook_book[key] = lines
                file_obj.readline()
                key = file_obj.readline().strip()
    return(cook_book)

cook_book = open_txt()
pprint(cook_book)

pprint(get_shop_list_by_dishes(['Омлет'], 2))

def sorting_files():
    all_files_name = [str(num_file) + '.txt' for num_file in range(1, 4)]
    result_file = 'result.txt'
    file_len_dict = {}

    for file in all_files_name:
        with open(os.path.join(os.getcwd(), file)) as reading_file:
            keys_in_dict = len(reading_file.readlines())
            if keys_in_dict not in file_len_dict.keys():
                file_len_dict[keys_in_dict] = list(file.split())
            else:
                file_len_dict.get(keys_in_dict).append(file)
            sort_keys = sorted(file_len_dict.keys())
            sort_dict = {i: file_len_dict[i] for i in sort_keys}

    with open(os.path.join(os.getcwd(), result_file), 'a') as result:
        for strings, name_file in sort_dict.items():
            for i in range(len(name_file)):
                result.write(str(name_file[i]) + '\n')
                result.write(str(strings) + '\n')
                with open(os.path.join(os.getcwd(), name_file[i])) as reading_file:
                    for rw_string in reading_file:
                        result.write(rw_string + reading_file.readline())
                result.write('\n\n')
    return file_len_dict

print(sorting_files())





