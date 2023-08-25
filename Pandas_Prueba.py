import pandas as pd

datos = {
    "nombre": ["Maria", "Luis", "Carmen"],
    "materia": ["Matematicas", "Programacion", "Mercadotecnia"],
    "promedio": [80, 90, 100]
}
df_alumnos = pd.DataFrame(datos)
print(df_alumnos)

df_colesterol= pd.read_csv("https://raw.githubusercontent.com/asalber/"
                          "manual-python/master/datos/colesteroles.csv", sep=";",decimal=",")
#print(df_colesterol)
#print(df_colesterol.head())
#print(df_colesterol.sample())
#print(df_colesterol.info)
#Sacar estadistica basica sonbre los datos que son numericos
#print(df_colesterol.describe())
#Imprimir las columas
#print(df_colesterol.columns)
#Tipo de datos
#print(df_colesterol.dtypes)
#print(df_colesterol.index)

print(df_colesterol[["nombre", "edad", "colesterol"]])