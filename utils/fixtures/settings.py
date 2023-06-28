import json
from pathlib import Path

from utils.models.operation import Operation

HOME = Path(__file__).resolve().parent
OPERATIONS_JSON = Path.joinpath(HOME, 'operations.json')


def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def delete_blank_data(operations):
    operations.remove({})
    return operations


def get_first_five_sorted_operations(operation_list):
    return sorted(
        operation_list,
        key=lambda operation_data: (operation_data['state'], operation_data['date']),
        reverse=True
    )[:5]


def get_five_sorted_classes(five_operations):
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

