import numpy as np
import scipy.stats as stats

class LinearRegression:
    def __init__(self, X=None, Y=None, confidence_level=95):
        self._X = None
        self._Y = None
        self._b= None
        self.confidence_level = confidence_level #add and implement completely

        if X is not None and Y is not None:
            self.fit(X=X, Y=Y)
    
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
    def confidence_level(self):
        return self._confidence_level
    @confidence_level.setter
    def confidence_level(self, conf_level):
        self._confidence_level = conf_level

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
            raise ValueError("You must define X and Y before computing SSE")
    
    @property
    def MSE(self):
        return np.divide(self.SSE, self.n)
    
    @property
    def RMSE(self):
        return np.sqrt(self.MSE)
    
    @property
    def Syy(self):
        if self.Y is not None:
            return np.sum(np.square(self.Y - np.mean(self.Y)))
        else:
            raise ValueError("You must define Y before computing Syy")
    
    @property
    def SSR(self):
        return self.Syy - self.SSE
    
    @property
    def Rsq(self):
        return np.divide(self.SSR, self.Syy)
    
    @property
    def MSR(self):
        return np.divide(self.SSR, self.d)
    
    @property
    def b(self):
        if self._b is None:
            self.fit()

        return self._b
    
    @property
    def var(self): #sigma 2
        return np.divide(self.SSE, (self.n - self.d - 1))
    
    @property
    def std(self): #sigma
        return np.sqrt(self.SSE)
    
    @property
    def F_stat(self):
        return np.divide(np.divide(self.SSR, self.d), self.var)
    
    @property
    def p_value(self):
        return stats.f(self.d, self.n - self.d - 1).sf(self.F_stat)
    
    @property
    def T_stat_array(self): #maybe rename
        _C = np.multiply(np.linalg.pinv(self.X.T @ self.X), self.var)
        return np.divide(self.b.flatten(), np.multiply(self.std, np.sqrt(np.diag(_C))))

    @property
    def params_p_values(self): #review calculations
        return np.multiply(2, stats.t.sf(np.abs(self.T_stat_array), self.n - self.d - 1))
    
    @property
    def corr_matrix(self):
        _i, _j = np.indices((self.d, self.d))
        return stats.pearsonr(self.X[:, _i + 1], self.X[:, _j + 1])[0]
    
    def predict(self, X):
        _X = np.asarray(X)

        if _X.ndim == 1:
            _X = _X.reshape(1, -1)

        return (np.column_stack((np.ones(_X.shape[0]), _X)) @ self.b).flatten()

    def fit(self, X=None, Y=None):
        if X is not None:
            self.X = X
        elif self.X is None:
            raise ValueError("You must define X and Y before comupting bias")
        
        if Y is not None:
            self.Y = Y
        elif self.Y is None:
            raise ValueError("You must define X and Y before computing bias")
        
        self._b = np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y

        return self

    def __repr__(self):
        return f"LinearRegression(n={self.n}, d={self.d})"


if __name__ == "__main__":
    lin_reg = LinearRegression(
        X=[[1, 2, 3], [2, 7, 3], [1, 8, 4], [2, 5 ,3], [1, 6, 7]], 
        Y=[10, 15, 20, 25, 35]
    )
    print(f"X:\n{lin_reg.X}\n")
    print(f"Y:\n{lin_reg.Y}\n")
    print(f"coef:\n{lin_reg.b}\n")
    print(f"d: {lin_reg.d}")
    print(f"n: {lin_reg.n}")
    print(f"SSE: {lin_reg.SSE}")
    print(f"MSE: {lin_reg.MSE}")
    print(f"RMSE:: {lin_reg.RMSE}")
    print(f"Syy: {lin_reg.Syy}")
    print(f"SSR: {lin_reg.SSR}")
    print(f"Rsq, R^2: {lin_reg.Rsq}")
    print(f"MSR: {lin_reg.MSR}")
    print(f"var: {lin_reg.var}")
    print(f"std: {lin_reg.std}")
    print(f"predict test: {lin_reg.predict([2, 5, 7])}")
    print(f"\ncorr:\n{lin_reg.corr_matrix}\n")
    print(f"F val: {lin_reg.F_stat}")
    print(f"p val: {lin_reg.p_value}")
    print(f"params T array: {lin_reg.T_stat_array}")
    print(f"params p vals: {lin_reg.params_p_values}")