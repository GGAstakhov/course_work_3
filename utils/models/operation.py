import datetime
import re


class Operation:
    def __init__(self, pk, date, state, op_amount, description, fro, to):
        self.pk = pk
        self.date = self.edit_date_time(date)
        self.state = state
        self.op_amount = op_amount
        self.description = description
        self.fro = self.get_hidden_numbers(fro) if fro else "Создан новый счет"
        self.to = self.get_hidden_numbers(to)

    def edit_date_time(self, date):
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        date = datetime.datetime.strptime(date, date_format)
        edited_date = datetime.datetime.strftime(date, '%d.%m.%Y')
        return edited_date

    def get_hidden_numbers(self, number):
        if number.startswith('Счет'):
            delete_word = re.sub(r'[a-z]+\s?', '', number.lower()).strip()
            delete_digit = re.sub(r'\d+\s?', '', number).strip()
            replace_stars = (len(delete_word[:2]) * '*') + delete_word[-4:]
            return f"{delete_digit} {replace_stars}"

        delete_word = re.sub(r'[a-z]+\s?', '', number.lower()).strip()
        delete_digit = re.sub(r'\d+\s?', '', number).strip()
        git_asterisk_for_from = delete_word[:6] + (len(delete_word[6:-4]) * '*') + delete_word[-4:]
        replace_stars = " ".join([git_asterisk_for_from[i:i + 4] for i in range(0, len(git_asterisk_for_from), 4)])
        return f"{delete_digit} {replace_stars}"

    def __str__(self):
        value = self.op_amount["amount"] + " " + self.op_amount["currency"]["name"]
        return f'{self.date} {self.description}\n {self.fro} -> {self.to}\n {value}'
