<<<<<<< HEAD
earnings = int(input('Введите значение выручки фирмы- '))
cost = int(input('Введите значение издержек фирмы- '))
profit = earnings - cost
print()

if cost >= earnings:
    print("Финансовый показатель фирмы- убыток")
else:
    print('Финансовый показатель фирмы- прибыль')

if earnings > cost:
    print('{:.2%}'.format((earnings - cost) / earnings)) #не сообразила как вывести с помощью f строки((
print()

number_of_employees = int(input("Введите число сотрудников- "))
print('Прибыль фирмы в расчете на одного сотрудника= ''{:.2%}'.format((earnings - cost) / number_of_employees))



















=======
earnings = int(input('Введите значение выручки фирмы- '))
cost = int(input('Введите значение издержек фирмы- '))
profit = earnings - cost
print()

if cost >= earnings:
    print("Финансовый показатель фирмы- убыток")
else:
    print('Финансовый показатель фирмы- прибыль')

if earnings > cost:
    print('{:.2%}'.format((earnings - cost) / earnings)) #не сообразила как вывести с помощью f строки((
print()

number_of_employees = int(input("Введите число сотрудников- "))
print('Прибыль фирмы в расчете на одного сотрудника= ''{:.2%}'.format((earnings - cost) / number_of_employees))



















>>>>>>> main
