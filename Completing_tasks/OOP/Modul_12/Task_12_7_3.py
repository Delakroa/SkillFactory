money = int(input("Введите сумму: "))   # вводится сумма, которую человек планирует положить под проценты.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []  # пустой список для последующего сохранения в нем значений.

for value in per_cent.values():  # крутим в цикле вытаскивая значения
    result = int(money / 100 * value)
    deposit.append(result)  # добавляем результат в конец списка
print(f"Накопленные средства за год вклада, в каждом из банков: \n {deposit}\n", )
print(f"Максимальная сумма которую вы можете заработать -- {max(deposit)}")
