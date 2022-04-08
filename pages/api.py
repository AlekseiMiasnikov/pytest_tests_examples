from allure import step


@step('Проверка полей')
def asserts(assert_data, data):
    for item in data:
        if item == 'data':
            continue
        assert assert_data[item] == data[item], \
            f'Не совпадают данные: \nОжидалось: {data} \nПришло: {assert_data}'
