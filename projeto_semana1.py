import numpy as np

cargas_15_dias = np.array([40, 42, 45, 45, 48, 50, 52, 55, 60, 62, 65, 65, 70, 72, 75])

print(f"Evolução de carga entre o primeiro e último dia: {cargas_15_dias[-1] - cargas_15_dias[0]}")

recuperacao = np.delete(cargas_15_dias,[4, 9, 14])
print(f"Cargas com descanso: {recuperacao}")

print(f"Maiores cargas: {cargas_15_dias[cargas_15_dias > 60]}")