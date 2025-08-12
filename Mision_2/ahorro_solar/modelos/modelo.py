import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pickle


data = {
    "ubicacion": ["zona_1", "zona_2", "zona_1", "zona_3", "zona_2"],
    "tamano_hogar": [3, 4, 2, 5, 3],
    "costo_instalacion": [5000, 6000, 4500, 7000, 5200],
    "energia_generada": [3000, 3200, 2500, 4000, 2900],
    "ahorro_real": [1800, 2000, 1500, 2300, 1750],
}

df = pd.DataFrame(data)
df

# separar vairables independientes y dependientes
X = df.drop(columns=["ahorro_real"])
y = df["ahorro_real"]

X_encoded = pd.get_dummies(X)

# dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# guardar el modelo y las columnas
with open("modelo.pkl", "wb") as f:
    pickle.dump(model, f)

with open("columnas.pkl", "wb") as f:
    pickle.dump(X_encoded.columns.tolist(), f)
