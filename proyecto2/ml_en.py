from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

# Métricas
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import pandas as pd

def modelo_filtrado_en(dato):
    df = pd.read_csv("proyecto2/modelo_en.csv")
    filtro = [c for c in df.columns if c.startswith(dato)]
    X = df[filtro]
    y = df["CLASS"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

    X_scaler = MinMaxScaler()

    X_train = X_scaler.fit_transform(X_train)

    X_test = X_scaler.transform(X_test)

    model = RandomForestClassifier(random_state=42)

    model.fit(X_train, y_train)

    yhat = model.predict(X_test)

    acc = accuracy_score(y_test, yhat)
    pre = precision_score(y_test, yhat)
    rec = recall_score(y_test, yhat)

    data_filtrado = [model, X_scaler, f"Accuracy {round(acc * 100, 2)}%", f"Precision {round(pre * 100, 2)}%",
                     f"Recall {round(rec * 100, 2)}%"]

    return data_filtrado