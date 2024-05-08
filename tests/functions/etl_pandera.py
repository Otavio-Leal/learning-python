import pandas as pd
import os
import glob


def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json ]
    df_total = pd.concat(df_list,ignore_index=True)
    return df_total

def calcular_kpi(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["quantidade"] * df["preço"]
    return df

def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv")
        if formato == 'parquet':
            df.to_parquet("dados.parquet")

def pipeline(pasta: str, format_saida: list):

    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi(data_frame)

    carregar_dados(data_frame_calculado, format_saida)
   
format_saida: list = ['csv']
pasta = 'tests/functions/data/' 

pipeline(pasta, format_sada)

