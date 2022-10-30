print('Задача 5. Текстовый калькулятор')


def try_get_result(expression: str):
    expression = expression.split()
    if len(expression) != 3:
        raise ValueError

    left = int(expression[0])
    right = int(expression[2])
    match expression[1]:
        case '+':
            return left + right
        case '-':
            return left - right
        case '*':
            return left * right
        case '/':
            return left / right
        case '//':
            return left // right
        case '%':
            return left % right
        case _:
            raise ValueError


results_sum = 0
with open('calc.txt', 'r') as calc_file:
    for expression_line in calc_file:
        expression_line = expression_line.replace('\n', '')
        while True:
            try:
                results_sum += try_get_result(expression_line)
            except (ValueError, ArithmeticError):
                answer = input(f'Обнаружена ошибка в строке: {expression_line}   Хотите исправить? ')
                if answer.lower() == 'да':
                    expression_line = input('Введите исправленную строку: ')
                    continue
            break

print('\nСумма результатов:', results_sum)
