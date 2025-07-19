import pandas as pd
import numpy as np
import os

np.random.seed(42)
n = 1000

# Generar features
data = pd.DataFrame({
    "monthly_charges": np.random.normal(70, 20, n),
    "tenure": np.random.randint(1, 72, n),
    "contract_type": np.random.choice([0, 1], n),
    "support_calls": np.random.poisson(1.5, n),
})

# Generar target
data["target"] = (
    (data["tenure"] < 12).astype(int) +
    (data["support_calls"] > 2).astype(int) +
    (data["contract_type"] == 0).astype(int)
) >= 2
data["target"] = data["target"].astype(int)

# Crear carpeta si no existe
output_path = "./data/churn.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Guardar CSV
data.to_csv(output_path, index=False)
print(f"✅ Dataset generado: {output_path}")

