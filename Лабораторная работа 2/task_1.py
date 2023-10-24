money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

count_of_month = 0

while True:
    diff = salary - spend
    money_capital += diff

    # money_capital -= abs(diff)

    if money_capital <= 0:
        break
    else:
        count_of_month += 1

    spend += spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", count_of_month)
