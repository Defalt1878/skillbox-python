print('Задача 9. Аннуитетный платёж')


def calc_annuity_payment(debt: float, interest_rate: float, years: int):
    x = (1 + interest_rate) ** years
    return round(debt * interest_rate * x / (x - 1), 2)


def calc_print_periods(debt: float, interest_rate: float, annuity_payment: float, periods_count: int):
    for period in range(1, periods_count + 1):
        print(f'\nПериод: {period}')
        print(f'Остаток долга на начало периода: {debt:.2f}')
        interest_paid = debt * interest_rate
        print(f'Выплачено процентов: {interest_paid:.2f}')
        debt_body_paid = annuity_payment - interest_paid
        print(f'Выплачено тела кредита: {debt_body_paid:.2f}')
        debt -= debt_body_paid
    return debt


debt = float(input('Введите сумму кредита: '))
years = int(input('На сколько лет выдан? '))
interest_rate = float(input('Сколько процентов годовых? ')) / 100

annuity_payment = calc_annuity_payment(debt, interest_rate, years)
debt = calc_print_periods(debt, interest_rate, annuity_payment, 3)

print(f'\nОстаток долга: {debt:.2f}\n')
print('==============================\n')

prolong_years = int(input('На сколько лет продляется договор? '))
interest_rate = float(input('Увеличение ставки до: ')) / 100
years = prolong_years + years - 3

annuity_payment = calc_annuity_payment(debt, interest_rate, years)
debt = calc_print_periods(debt, interest_rate, annuity_payment, years)

print(f'\nОстаток долга: {debt:.2f}')
