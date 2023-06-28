import json

from utils.fixtures.settings import OPERATIONS_JSON
from utils.models.operation import Operation


class Data:
    def __init__(self):
        self.data_json = OPERATIONS_JSON

    def load_json(self):
        """метод считывает файл
        и возвращает его в формате
        список со словарями"""
        with open(self.data_json, 'r', encoding='utf-8') as file:
            return json.load(file)

    def delete_blank_data(self):
        """метод удаляет
        все пустые
        словари"""
        operations = self.load_json()
        operations.remove({})
        return operations

    def get_first_five_sorted_operations(self):
        """метод получает список со словарями
        и сортирует их:
        Сортируем по дате;
        Сортируем по ключую EXECUTED;
        Возвращаем только 5 последних операций"""
        operation_list = self.delete_blank_data()
        return sorted(
            operation_list,
            key=lambda operation_data: (operation_data['state'], operation_data['date']),
            reverse=True
        )[:5]

    def get_five_sorted_classes(self):
        """метод раскладывает 5 полученных операций
        в 5 экземпляров класса Operation
        и складывает полученные результаты
        в список и возвращает его"""
        five_operations = self.get_first_five_sorted_operations()
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

