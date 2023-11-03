import employee_info


def test_get_employees_by_age_range():
    test_age_lower_limit = 25
    test_age_higher_limit = 32
    test_answer = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000}]
    result = employee_info.get_employees_by_age_range(test_age_lower_limit, test_age_higher_limit)

    assert test_answer == result


def test_calculate_average_salary():
    total = 0
    for items in employee_info.employee_data:
        total += items["salary"]
    test_answer = round(total / (len(employee_info.employee_data)), 2)
    result = employee_info.calculate_average_salary()

    assert test_answer == result


def test_get_employees_by_dept():
    input_test = "Sales"
    test_answer = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                   {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result = employee_info.get_employees_by_dept(input_test)
    assert test_answer == result
