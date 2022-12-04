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


# 1. Write a function that accept employee and add to the list of employee.
def addNew(name, phone, email, department, salary, employment_date):
    new_employee = dict(name=name, phone=phone, email=email, department=department,
                        salary=salary, employment_date=employment_date)
    employee.append(new_employee)
    print('1.', employee[-1])  # This is to check the newly added employee


# addNew('praise', 9193493993, 'emmanuelpraise36@gmai l.com', 'engineering', 200_000, date(2020, 12, 12))
addNew('emmanuel', 9194543493, 'emmanuel126@gmail.com', 'accounting', 210_000, date(2020, 8, 1))
# addNew('samuel', 9062349184, 'stainlessseyy2007@gmail.com', 'marketing', 250_000, date(2019, 1, 1))
addNew('julian', 8055347784, 'julianuary@com', 'marketing', 205_000, date(2018, 11, 6))
print('\n')


# 2. Write a function that accept 2 parameters 'date from' and 'date to'.
# And returns the employee that was employed within the date range in an array form.
def dateRange(date_from, date_to):
    # Getting the list of dates in the employee list.
    date_list = [i['employment_date'] for i in employee if 'employment_date' in i]
    date_list.sort()

    # Getting the date between date_from and date_to.
    date_between = [x for x in date_list if date_from <= x <= date_to]

    # Getting the Employee details where employment date between date range
    for x in range(len(date_between)):
        for i in employee:
            if i['employment_date'] == date_between[x]:
                print('2.', i)


dateRange(date(2019, 1, 1), date(2020, 8, 4))
print('\n')


# 3. write function that returns the array of employee with invalid email address.
def get_email():
    # Getting the invalid emails with the employee details.
    for i in employee:
        if '@gmail.com' not in i['email'] and '@yahoo.com' not in i['email'] and '@outlook.com' not in i['email']:
            print('3.', i)


get_email()
print('\n')


# 4. Write a function that return employee with highest and lowest pay.
def highest_lowest_pay():
    # Getting the list of salary in the employee list.
    salary_list = [i['salary'] for i in employee if 'salary' in i]

    # Getting the highest salary from the salary list
    high = salary_list[0]
    for x in salary_list:
        if x > high:
            high = x

    # Getting the lowest salary from the salary list
    low = salary_list[0]
    for x in salary_list:
        if x < low:
            low = x

    # Getting the Employee details with the highest and lowest salaries
    for i in employee:
        if i['salary'] == high or i['salary'] == low:
            print('4.', i)


highest_lowest_pay()
