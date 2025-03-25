import numpy as np


class DecisionTreeRegressorManual:
    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def _calculate_mse(self, y):
        """ Вспомогательная функция для расчета MSE """
        if len(y) == 0:
            return 0
        mean_y = np.mean(y)
        return np.mean((y - mean_y) ** 2)

    def _best_split(self, X, y):
        """ Поиск наилучшего разбиения """
        best_mse = float('inf')
        best_split = None
        n_samples, n_features = X.shape

        for feature_idx in range(n_features):
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                left_mask = X[:, feature_idx] < threshold
                right_mask = X[:, feature_idx] >= threshold

                y_left, y_right = y[left_mask], y[right_mask]
                mse_left, mse_right = self._calculate_mse(y_left), self._calculate_mse(y_right)

                weighted_mse = (len(y_left) / n_samples) * mse_left + (len(y_right) / n_samples) * mse_right

                if weighted_mse < best_mse:
                    best_mse = weighted_mse
                    best_split = {
                        'feature_idx': feature_idx,
                        'threshold': threshold,
                        'mse': best_mse,
                        'left_mask': left_mask,
                        'right_mask': right_mask
                    }
        return best_split

    def _build_tree(self, X, y, depth=0):
        """ Рекурсивное построение дерева """
        n_samples, n_features = X.shape

        # Условие остановки
        if depth >= self.max_depth or n_samples < self.min_samples_split or np.unique(y).size == 1:
            return {'value': np.mean(y)}

        # Поиск наилучшего разбиения
        best_split = self._best_split(X, y)

        if not best_split:
            return {'value': np.mean(y)}

        left_tree = self._build_tree(X[best_split['left_mask']], y[best_split['left_mask']], depth + 1)
        right_tree = self._build_tree(X[best_split['right_mask']], y[best_split['right_mask']], depth + 1)

        return {
            'feature_idx': best_split['feature_idx'],
            'threshold': best_split['threshold'],
            'left': left_tree,
            'right': right_tree
        }

    def fit(self, X, y):
        """ Обучение модели """
        self.tree = self._build_tree(np.array(X), np.array(y))

    def _predict_sample(self, x, tree):
        """ Предсказание для одного объекта """
        if 'value' in tree:
            return tree['value']
        feature_value = x[tree['feature_idx']]
        if feature_value < tree['threshold']:
            return self._predict_sample(x, tree['left'])
        else:
            return self._predict_sample(x, tree['right'])

    def predict(self, X):
        """ Предсказание для множества объектов """
        return np.array([self._predict_sample(x, self.tree) for x in np.array(X)])

