import json
from pathlib import Path

from utils.models.operation import Operation

# Прописываем пути к файлу
HOME = Path(__file__).resolve().parent
OPERATIONS_JSON = Path.joinpath(HOME, 'operations.json')


def load_json(path):
    """функция считывает файл
    и возвращает его в формате
    список со словарями"""
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def delete_blank_data(operations):
    """функция удаляет
    все пустые
    словари"""
    operations.remove({})
    return operations


def get_first_five_sorted_operations(operation_list):
    """функция получает список со словарями
    и сортирует их:
    Сортируем по дате;
    Сортируем по ключую EXECUTED;
    Возвращаем только 5 последних операций"""
    return sorted(
        operation_list,
        key=lambda operation_data: (operation_data['state'], operation_data['date']),
        reverse=True
    )[:5]


def get_five_sorted_classes(five_operations):
    """функция раскладывает 5 полученных операций
    в 5 экземпляров класса Operation
    и складывает полученные результаты
    в список и возвращает его"""
    picked_out_list = []
    for operation in five_operations:
        picked_out_list.append(Operation(pk=operation['id'],
                                         date=operation['date'],
                                         state=operation['state'],
                                         op_amount=operation['operationAmount'],
                                         description=operation['description'],
                                         fro=operation.get("from"),
                                         to=operation['to']))
    return picked_out_list

