
# TODO Оформить решение
money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
sum_money = money_capital + salary

while sum_money > 0:
    sum_money = sum_money - spend
    spend = spend + spend * increase
    month = month + 1


print(month)
