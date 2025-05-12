"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.
    """
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    agrupado = df.groupby("c1")["c2"].apply(lambda x: ":".join(map(str, sorted(x)))).to_frame()
    return agrupado

