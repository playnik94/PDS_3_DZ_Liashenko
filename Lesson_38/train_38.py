import numpy as np


# Сигмоидная функция
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Функция стоимости (логистическая регрессия)
def compute_cost(X, y, weights):
    m = len(y)
    h = sigmoid(np.dot(X, weights))
    cost = (-1 / m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    return cost


# Градиентный спуск
def gradient_descent(X, y, weights, learning_rate, iterations):
    m = len(y)
    cost_history = []

    for i in range(iterations):
        # Прогноз
        h = sigmoid(np.dot(X, weights))
        # Градиент
        gradient = np.dot(X.T, (h - y)) / m
        # Обновление весов
        weights -= learning_rate * gradient

        # Запоминаем значение функции стоимости на каждой итерации
        cost = compute_cost(X, y, weights)
        cost_history.append(cost)

        # Вывод стоимости каждые 1000 итераций
        if i % 1000 == 0:
            print(f"Iteration {i}: Cost {cost}")

    return weights, cost_history


# Основная функция для обучения модели
def logistic_regression(X, y, learning_rate=0.01, iterations=10000):
    # Добавляем столбец единиц для свободного члена (смещения)
    X = np.c_[np.ones(X.shape[0]), X]

    # Инициализация весов
    weights = np.zeros(X.shape[1])

    # Запуск градиентного спуска
    weights, cost_history = gradient_descent(X, y, weights, learning_rate, iterations)

    return weights, cost_history


# Пример использования
np.random.seed(42)
n_samples = 1000
n_features = 10

# Генерация случайных данных
X = np.random.randn(n_samples, n_features)
y = np.random.randint(0, 2, n_samples)

# Обучение модели
weights, cost_history = logistic_regression(X, y)

# Вывод финальных весов
print(f"Final weights: {weights}")