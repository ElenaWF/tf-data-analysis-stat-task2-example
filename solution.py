import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 1395253289 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    s = np.std(x, ddof=1)/3
    lower = ((n - 1) * s**2) / chi2.ppf(1 - alpha/2, n - 1)
    upper = ((n - 1) * s**2) / chi2.ppf(alpha/2, n - 1)
    return (np.sqrt(lower), np.sqrt(upper))
