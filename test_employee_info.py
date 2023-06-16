import employee_info

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(34, 45)
    names = []
    for person in result:
        names.append(person["name"])
    answer = ["Chloe", "Peter"]
    assert(answer == names)


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    answer = 60166.666666666664

    assert(answer == result)


def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Sales")
    names = []
    for person in result:
        names.append(person["name"])
    answer = ["John", "Peter"]

    assert(answer == names)