import numpy as np
from scipy.stats import chi2


def generar_numeros_LCG(X0, a, c, m, n):
    numeros = []
    X = X0
    for _ in range(n):
        X = (a * X + c) % m
        numeros.append(X / m)  
    return numeros


X0 = 7
a = 3
c = 1
m = 127
n = 500


secuencia_numeros = generar_numeros_LCG(X0, a, c, m, n)


def prueba_chi_cuadrado(secuencia, C, W):
    observados = np.histogram(secuencia, bins=C, range=(0, 1))[0]
    esperados = np.array([n * W] * C)
    chi_cuadrado = sum((observados - esperados) ** 2 / esperados)
    return chi_cuadrado


C = 10  
W = 0.1  


valor_chi_cuadrado = prueba_chi_cuadrado(secuencia_numeros, C, W)


def prueba_runs(secuencia, alpha):
    runs = [1 if secuencia[i] > secuencia[i - 1] else -1 for i in range(1, len(secuencia))]
    n1 = len([r for r in runs if r == 1])
    n2 = len([r for r in runs if r == -1])
    n = n1 + n2
    mu = (2 * n1 * n2) / n + 1
    sigma = (2 * n1 * n2 * (2 * n1 * n2 - n)) / (n ** 2 * (n - 1))
    z = (n1 - mu) / np.sqrt(sigma)
    p_value = 2 * (1 - chi2.cdf(z ** 2, 1))
    return p_value


alpha = 0.05


p_value_runs = prueba_runs(secuencia_numeros, alpha)


print(f"Valor calculado de chi-cuadrado: {valor_chi_cuadrado}")
print(f"P-valor para la prueba de runs: {p_value_runs}")
