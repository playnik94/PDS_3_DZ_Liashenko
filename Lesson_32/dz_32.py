import numpy as np
import pandas as pd

data = {
    "Name": ["Alexander", "Igor", " Vlad", "Sergei", "Georgi", "Ivan", "Anna", "Nikita", "Ekaterina", "Mchail", "Victoria", "Victor", "Artur", "Artem", "Olga"],
    "Average mark": [5, 4, 3, 5, 3, 4, 4, 3, 3, 4, 5, 3, 4, 5, 3],
    "Exam score" : [4, 3, 4, 4, 5, 4, 3, 5, 3, 3, 5, 4, 5, 4, 4],
    "Attempts" : [2, 5, 7, 1, 3, 8, 15, 2, 1, 9, 3, 10, 2, 11, 13]

}
indexs_rol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Studens = pd.DataFrame(data=data, index=indexs_rol)

# 2 Доступ до экзамена
Studens["Passed"] = np.array(["True", "False", "True ", "True", "False", "True", "True", "True", "True", "False", "False", "True", "False", "True", "True"])
print(Studens)

a = Studens["Average mark"].max()
print(f"Максимальный средний бал: {a}")

b = Studens["Average mark"].min()
print(f"Минимальный средний бал: {b}")

c = Studens["Average mark"].mean()
print(f"Средний бал:  {c}")

f = Studens["Average mark"].median()
print(f" Медиана: {a}\n")

# 4 Кол.во студентов прошедших экзамен
Passed = Studens.groupby("Passed")["Name"].count()
print(Passed)

Studens = pd.Series(data=indexs_rol, index=['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
print(Studens)