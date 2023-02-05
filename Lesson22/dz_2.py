
Days = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}

Rain = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

Windy = {1, 2, 3, 4, 5, 6, 7, 8}

Colds = {1, 2, 3, 4}

Rain_wind = {1, 2, 3, 4, 5}

Rain_colds = {1, 2, 3}

Windy_colds = {1, 2}

Rain_wind_cold = {1}

A = Days.difference(Rain_wind_cold)
print(len(A))

B = A.difference(Windy_colds)
print(len(B))

C = B.difference(Rain_colds)
print(len(C))

D = C.difference(Rain_wind)
print(len(D))

E = D.difference(Colds)
print(len(E))

F = E.difference(Windy)
print(len(F))

G = F.difference(Rain)
print(len(G))

V = A.symmetric_difference(G)
print(len(V))# 11 из 30 дней было с хорошей погодой.

