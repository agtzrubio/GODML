import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

# Generar features con correlación con target
data = pd.DataFrame({
    "monthly_charges": np.random.normal(70, 20, n),     # cargos mensuales
    "tenure": np.random.randint(1, 72, n),              # meses como cliente
    "contract_type": np.random.choice([0, 1], n),       # 0 = mes a mes, 1 = contrato anual
    "support_calls": np.random.poisson(1.5, n),         # llamadas al soporte
})

# Variable objetivo: churn = 1 si baja tenure + alto support_calls + bajo contrato anual
data["target"] = (
    (data["tenure"] < 12).astype(int) +
    (data["support_calls"] > 2).astype(int) +
    (data["contract_type"] == 0).astype(int)
) >= 2
data["target"] = data["target"].astype(int)

# Guardar a CSV
data.to_csv("./df/churn.csv", index=False)
print("Dataset churn.csv creado con éxito.")
