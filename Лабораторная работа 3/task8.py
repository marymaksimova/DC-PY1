money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
sum_ = money_capital + salary

while sum_ >= spend:
    month += 1
    sum_ = sum_ + salary
    spend *= 1.05
    sum_ = sum_ - spend

print(month)