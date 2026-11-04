import pandas as pd
import os
# Hugo Fabian NC 0040
# URL del conjunto de datos
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
# Descargar y cargar
datos = pd.read_csv(url)
# Asegurar que la carpeta datasets exista antes de guardar
os.makedirs("datasets", exist_ok=True)
# Guardar archivo titanic.csv en carpeta dataset
datos.to_csv("datasets/titanic.csv", index=False)
# Explorar información
print("PRIMEROS 5 PASAJEROS")
print(datos.head())
print("\nDIMENSIONES")
print(datos.shape)
print("\nCOLUMNAS")
print(datos.columns.tolist())
print("\nINFORMACION GENERAL")
print(datos.info())
# Seleccionar características (X) eliminando la variable objetivo
X = datos.drop(columns=["survived"])
# Identificar variable objetivo
y = datos["survived"]
print("\nCARACTERISTICAS (X)")
print(X.head())
print("\nVARIABLE OBJETIVO (y)")
print(y.head())
print("\nCANTIDAD DE SUPERVIVIENTES")
print(y.value_counts())
print("\nVALORES FALTANTES")
print(datos.isnull().sum())