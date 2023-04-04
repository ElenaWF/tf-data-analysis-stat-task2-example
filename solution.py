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
    lower = (np.sum(x*x)) / chi2.ppf(1 - alpha/2, 2*n)
    upper = (np.sum(x*x)) / chi2.ppf(alpha/2, 2*n)
    return (1/3*np.sqrt(lower), 1/3*np.sqrt(upper))
