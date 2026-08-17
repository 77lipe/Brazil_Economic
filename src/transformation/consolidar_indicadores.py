""" Função que irá transformar as informações em DataFrame final utilizavel"""

import pandas as  pd

def dfInal_indicadores_bcb(resultados: dict) -> pd.DataFrame:

    df_indicadores = []
    for indicador, resultado in resultados.items():
        #print("resultado:", resultado)
        if resultado["status"] != "sucesso":
            continue

        df_indicador = resultado["resultado"]
        if df_indicador.empty:
            continue

        df_indicadores.append(df_indicador)
        if not df_indicadores:
            return pd.DataFrame()

        df_final = pd.concat(
            df_indicadores,
            ignore_index=True
        )
        df_final = df_final.sort_values(
            by=["data", "indicador"]
        )
        df_final = df_final.reset_index(drop=True)

    return df_final