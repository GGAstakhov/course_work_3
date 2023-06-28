from utils.fixtures.settings import load_json, OPERATIONS_JSON, delete_blank_data, get_first_five_sorted_operations, \
    get_five_sorted_classes

# Основная функция
def main():
    # получаем список со словарями
    data = load_json(OPERATIONS_JSON)
    # получаем обработанный список
    new_data = delete_blank_data(data)
    # выбераем 5 последних операций
    five_operations = get_first_five_sorted_operations(new_data)
    # получаем 5 обработанных эземпляров классов последних пяти операций
    new_five_operations = get_five_sorted_classes(five_operations)
    # выводим статистику
    for operation in new_five_operations:
        print(operation)


if __name__ == '__main__':
    main()
