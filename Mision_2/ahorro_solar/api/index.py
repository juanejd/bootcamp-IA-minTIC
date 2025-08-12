from flask import Flask, request, render_template
import pickle
import pandas as pd
import os

app = Flask(__name__, template_folder="../templates")
model = pickle.load(
    open(os.path.join(os.path.dirname(__file__), "../modelos/modelo.pkl"), "rb")
)
columns = pickle.load(
    open(os.path.join(os.path.dirname(__file__), "../modelos/columnas.pkl"), "rb")
)


@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")


@app.route("/predecir", methods=["POST"])
def predict():
    data = {
        # nombres en el modelo -- nombres en el formulario
        "ubicacion": request.form["ubication"],
        "tamano_hogar": int(request.form["size_house"]),
        "costo_instalacion": float(request.form["cost_installation"]),
        "energia_generada": float(request.form["energy_generated"]),
    }
    df = pd.DataFrame([data])
    df_encoded = pd.get_dummies(df)
    for col in columns:
        if col not in df_encoded:
            df_encoded[col] = 0
    prediction = model.predict(df_encoded[columns])[0]
    return render_template("results.html", prediction=round(prediction, 2))


# ejecuta la aplicacion tanto en local como en produccion
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
