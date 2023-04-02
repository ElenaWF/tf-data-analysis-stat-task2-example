import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 1395253289 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    df = n - 1
    alpha = 1 - p
    s = np.var(x, ddof=1)
    chi_squared_upper = chi2.ppf(1 - alpha/2, df)
    chi_squared_lower = chi2.ppf(alpha/2, df)
    upper_bound = np.sqrt((df * s) / (chi_squared_lower * 9))
    lower_bound = np.sqrt((df * s) / (chi_squared_upper * 9))
    return lower_bound, upper_bound
