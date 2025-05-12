"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de los valores
    de la columna `c5a` y `c5b` (unidos por ':') de la tabla `tbl2.tsv`.
    """
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    df["combinado"] = df["c5a"] + ":" + df["c5b"].astype(str)
    agrupado = df.groupby("c0")["combinado"].apply(lambda x: ",".join(sorted(x))).reset_index()
    agrupado.columns = ["c0", "c5"]
    return agrupado

