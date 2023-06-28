from tests.conftest import correct_data
from utils.models.data import Data
from utils.models.operation import Operation


def test_data_correct():
    data = Data().load_json()
    assert isinstance(data, list)
    assert isinstance(data[0], dict)


def test_delete_blank_data():
    data = Data()
    data.data = correct_data
    operation_list = data.delete_blank_data()
    assert isinstance(operation_list, list)
    assert isinstance(operation_list[1], dict)
    assert len(operation_list) == 100


def test_get_first_five_sorted_operations():
    data = Data().get_first_five_sorted_operations()
    assert isinstance(data, list)
    assert isinstance(data[1], dict)
    assert len(data) == 5


def test_get_five_sorted_classes(correct_data):
    data = Data()
    data.data = correct_data

    operation_list = data.get_five_sorted_classes()
    assert isinstance(operation_list, list)
    assert isinstance(operation_list[0], Operation)
    assert len(operation_list) == 5
    assert operation_list[1].state == "EXECUTED"
