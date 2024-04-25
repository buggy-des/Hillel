import json
import csv
import random

with open('example.json') as file:
    users = json.load(file)

print(users)

keys = ['ID', 'Name', 'Age', 'Phone number']
data_rows = []


def generate_phone_num():
    has_phone = random.random() < 0.75
    if not has_phone:
        return '-'.center(7, ' ')
    operators = ['095', '066', '098', '096', '050', '097']
    operator = random.choice(operators)
    number = ''.join(random.choice('0123456789') for _ in range(7))
    return operator + number


for id, (name, age) in users.items():
    phone_number = generate_phone_num()
    data = [id, name, age, phone_number]
    data_rows.append(data)

with open('example.csv', 'w', encoding='UTF-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',')
    file_writer.writerow(keys)
    file_writer.writerows(data_rows)
