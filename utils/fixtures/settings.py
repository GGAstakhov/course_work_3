import json
from pathlib import Path

from utils.models.operation import Operation

# Прописываем пути к файлу
HOME = Path(__file__).resolve().parent
OPERATIONS_JSON = Path.joinpath(HOME, 'operations.json')
