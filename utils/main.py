from utils.models.data import Data


def main():
    main_operation = Data()
    for operation in main_operation.get_five_sorted_classes():
        print(operation)


if __name__ == '__main__':
    main()
