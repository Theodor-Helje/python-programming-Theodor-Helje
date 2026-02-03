import numpy as np
import scipy.stats as stats

class LinearRegression:
    def __init__(self, X=None, Y=None):
        self._X = None
        self._Y = None
        self._coef = None

        if X is not None and Y is not None:
            self.X = X
            self.Y = Y
            self.fit()
    
    @property
    def X(self):
        return self._X
    @X.setter
    def X(self, X):
        _X = np.asarray(X)
        self._X = np.column_stack([np.ones(_X.shape[0]), _X])
    
    @property
    def Y(self):
        return self._Y
    @Y.setter
    def Y(self, Y):
        self._Y = np.asarray(Y).reshape(-1, 1)

    @property
    def n(self):
        if self.X is not None:
            return self.X.shape[0]
        else:
            return None

    @property
    def d(self):
        if self.X is not None:
            return self.X.shape[1]-1
        else:
            return None
    
    @property
    def coef(self):
        return self._coef
    
    def variance(self):
        pass

    def std(self):
        pass

    def fit(self, X=None, Y=None):
        if X is not None:
            self.X = X
        if Y is not None:
            self.Y = Y
        
        self._coef = np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y

        return self

    def __repr__(self):
        return f"LinearRegression(d={self.n}, n={self.n})"


if __name__ == "__main__":
    lin_reg = LinearRegression(X=[1, 2, 3, 4], Y=[10, 15, 20, 25])
    print(f"X:\n{lin_reg.X}\n")
    print(f"Y:\n{lin_reg.Y}\n")
    print(f"coef:\n{lin_reg.coef}\n")
    print(f"d: {lin_reg.d}")
    print(f"n: {lin_reg.n}")