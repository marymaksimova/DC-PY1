salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
total_sum = 0

for i in range(1, months + 1):
    delta = spend - salary  # количество дополнительных денег из подушки безопасности
    spend *= 1.03
    total_sum += delta

need_money = total_sum

print(round(need_money))
