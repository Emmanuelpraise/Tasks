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


# 1. write a function that accept employee and add to the list of employee.
def addNew(name, phone, email, department, salary, employment_date):
    new_employee = dict(name=name, phone=phone, email=email,
                        department=department, salary=salary,
                        employment_date=employment_date)
    employee.append(new_employee)
    print(employee[len(employee) - 1])  # This is to check the newly added employee


# addNew('praise', 9193493993, 'emmanuelpraise36@gmail.com', 'engineering', 200_000, date(2020, 12, 12))
addNew('samuel', 9062349184, 'stainlessseyy2007@gmail.com', 'marketing', 250_000, date(2019, 1, 1))


# 2. write a function that accept 2 parameters 'date from' and 'date to'.
# And returns the employee that was employed within the date range in an array form.
def dateRange(date_from, date_to):
    date_list = [i['employment_date'] for i in employee if 'employment_date' in i]
    date_list.sort()
    date_between = [x for x in date_list if date_from <= x <= date_to]
    print(date_between)


dateRange(date(2018, 3, 14), date(2020, 8, 4))


# 3. write function that returns the array of employee with invalid email address.
def get_email():
    email_list = [i['email'] for i in employee if 'email' in i]
    invalid_email = [x for x in email_list
                     if not x.__contains__('@gmail.com') and not x.__contains__('@yahoo.com')
                     and not x.__contains__('@outlook.com')]
    print(invalid_email)

    # for i in employee:
    #     if invalid_email[0] in i['email']:
    #         print(i)

    # Try in to get Employee details where emails are invalid
    # for x in range(len(invalid_email)):
    #     print(x)
    #     for i in employee:
    #         if i['name'].__contains__(invalid_email[x]):
    #             print(i)


get_email()


# 4.write a function that return employee with highest and lowest pay.
def highest_pay():
    salary_list = [i['salary'] for i in employee if 'salary' in i]
    high = salary_list[0]
    for x in salary_list:
        if x > high:
            high = x
    print(high)


def lowest_pay():
    salary_list = [i['salary'] for i in employee if 'salary' in i]
    low = salary_list[0]
    for x in salary_list:
        if x < low:
            low = x
    print(low)


def highest_lowest_pay():
    lowest_pay(), highest_pay()


highest_lowest_pay()