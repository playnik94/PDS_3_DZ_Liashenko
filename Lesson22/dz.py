Students = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37}

grade_math = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

grade_phys = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

grade_chem = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

grade_math_phys = {1, 2, 3, 4, 5, 6, 7}

grade_math_chem = {1, 2, 3, 4, 5, 6, 7, 8, 9}

grade_phys_chem = {1, 2, 3, 4, 5, 6}

grade_math_phys_chem = {1, 2, 3, 4}

A = grade_math_chem.intersection(grade_math_phys,grade_math_phys) # 7 студентов получили хорошо по двум предметам
print(A)

B = grade_chem.intersection(grade_phys,grade_math) # 15 студентов получили хорошо по 1 предмету
print(B)