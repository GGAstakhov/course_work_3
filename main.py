from utils.fixtures.settings import load_json, OPERATIONS_JSON, delete_blank_data, get_first_five_sorted_operations, \
    get_five_sorted_classes


def main():
    data = load_json(OPERATIONS_JSON)

    new_data = delete_blank_data(data)

    five_operations = get_first_five_sorted_operations(new_data)

    new_five_operations = get_five_sorted_classes(five_operations)

    for operation in new_five_operations:
        print(operation)


if __name__ == '__main__':
    main()
