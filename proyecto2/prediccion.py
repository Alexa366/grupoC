from ml import modelo_filtrado


def prediccion(dato):
    modelo_filtrado(dato)
    diccionario = np.load("dicc.npy", allow_pickle="TRUE")

    test = []
    for datos, valor in zip(dato, seleccion):
        test.append(diccionario[datos][valor])

    test = np.array([test])

    test = X_scaler.transform(test)
    y_pred = model.predict(test)
    print([k for k, v in diccionario['class'].items() if v == y_pred[0]])