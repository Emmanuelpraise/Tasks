from operator import itemgetter

from datetime import date

# Given an array of employee with the details: name, phone, email, department, salary, employment date.
employee = [
    {
        'name': 'David',
        'phone': 9139268581,
        'email': 'davie612@outlook.com',
        'department': 'accounting',
        'salary': 150_000,
        'employment_date': date(2019, 12, 30)
    },
    {
        'name': 'Thomas',
        'phone': 8181283984,
        'email': 'tom.fret@gmail.com',
        'department': 'engineering',
        'salary': 250_000,
        'employment_date': date(2018, 4, 4)
    },
    {
        'name': 'John',
        'phone': 9037571843,
        'email': 'johnny612@yhaoo.com',
        'department': 'marketing',
        'salary': 80_000,
        'employment_date': date(2022, 7, 30)
    },
    {
        'name': 'Peter',
        'phone': 7029348318,
        'email': 'mundanes_peter.gmail.com',
        'department': 'engineering',
        'salary': 200_000,
        'employment_date': date(2016, 12, 21)
    },
    {
        'name': 'Katerine',
        'phone': 8019847680,
        'email': 'katerina_dior@yhaoo.com m',
        'department': 'marketing',
        'salary': 105_000,
        'employment_date': date(2021, 2, 2)
    },
    {
        'name': 'Adam',
        'phone': 70234788458,
        'email': 'adam.eve@outlook.com',
        'department': 'accounting',
        'salary': 150_000,
        'employment_date': date(2020, 2, 3)
    },
    {
        'name': 'Esther',
        'phone': 8151384675,
        'email': 'queen_ester223@yahoo.com',
        'department': 'marketing',
        'salary': 105_000,
        'employment_date': date(2020, 10, 11)
    }
]

# for i in employee:
#     if '@gmail.com' not in i['email'] and '@yahoo.com' not in i['email'] and '@outlook.com' not in i['email']:
#         print(i)


def get_email():
    # Getting the list of emails in the employee list.
    email_list = [i['email'] for i in employee if 'email' in i]
    email_list.sort()

    # Getting the list of invalid emails from the email list.
    invalid_email = [x for x in email_list
                     if '@gmail.com' not in x and '@yahoo.com' not in x and '@outlook.com' not in x]

    # Getting the Employee details where emails are invalid
    for x in range(len(invalid_email)):
        for i in employee:
            if invalid_email[x] in i['email']:
                print(i)


get_email()

students = [
    {
        'name': 'ola',
        'age': 18,
        'sex': 'M'
    },
    {
        'name': 'Lola',
        'age': 16,
        'sex': 'F'
    },
    {
        'name': 'Bisi',
        'age': 17,
        'sex': 'F'
    },
    {
        'name': 'ayo',
        'age': 18,
        'sex': 'M'
    }
]

nameGetter = itemgetter("name")
getName = [nameGetter(item) for item in students]
print(getName)

# or
getName = [i['name'] for i in students if 'name' in i]
print(getName)

for i in students:
    if i.__contains__('F'):
        print(i)

name = 'Day'
if name in getName:
    print('True')
else:
    print('False')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# for x in range(len(date_between)):
#     for i in employee:
#         if date_between[x] in i['employment_date']:
#             print(i)

# How to iterate through a list of numbers
for x in numbers:
    if type(x) is list:
        for y in x:
            print(y)
    else:
        print(x)
# or
for x in numbers:
    if type(x) is not list:
        print(x)
