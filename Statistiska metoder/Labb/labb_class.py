import numpy as np
#import scipy.stats as stats

class LinearRegression:
    def __init__(self, X=None, Y=None):
        self._X = None
        self._Y = None
        self._b= None

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
    def SSE(self):
        if self.X is not None and self.Y is not None and self.b is not None:
            return np.sum(np.square(self.Y - (self.X @ self.b)))
        else:
            return None
    
    @property
    def MSE(self):
        return np.divide(self.SSE, self.n)
    
    @property
    def b(self):
        if self._b is None:
            self.fit()

        return self._b
    
    @property
    def var(self):
        return np.divide(self.SSE, (self.n - self.d - 1))
    
    @property
    def std(self):
        return np.sqrt(self.SSE)
    
    def pred(self, X):
        _X = np.asarray(X)

        if _X.ndim == 1:
            _X = _X.reshape(1, -1)

        return (np.column_stack((np.ones(_X.shape[0]), _X)) @ self.b).flatten()

    def fit(self, X=None, Y=None):
        if X is not None:
            self.X = X
        elif self.X is None:
            raise ValueError("You must define X and Y before comuting bias")
        
        if Y is not None:
            self.Y = Y
        elif self.Y is None:
            raise ValueError("You must define X and Y before comuting bias")
        
        self._b = np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y

        return self

    def __repr__(self):
        return f"LinearRegression(n={self.n}, d={self.d})"


if __name__ == "__main__":
    lin_reg = LinearRegression(X=[[1, 2, 3, 4], [2, 7, 3, 8], [1, 8, 4, 6], [2,5 ,3 ,7]], Y=[10, 15, 20, 25])
    print(f"X:\n{lin_reg.X}\n")
    print(f"Y:\n{lin_reg.Y}\n")
    print(f"coef:\n{lin_reg.b}\n")
    print(f"d: {lin_reg.d}")
    print(f"n: {lin_reg.n}")
    print(f"SSE: {lin_reg.SSE}")
    print(f"MSE: {lin_reg.MSE}")
    print(f"var: {lin_reg.var}")
    print(f"std: {lin_reg.std}")
    print(lin_reg.pred([2, 5, 7, 3]))