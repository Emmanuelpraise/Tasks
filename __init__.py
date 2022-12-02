from operator import itemgetter

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
