import csv
user_list = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open('users.csv', 'w', encoding='utf-8', newline='') as new_csv:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(new_csv, fields, delimiter=',')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)
