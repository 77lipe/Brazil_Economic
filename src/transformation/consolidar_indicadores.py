""" Função que irá transformar as informações em DataFrame final utilizavel"""

import pandas as  pd

def consolidar_indicadores_bcb(resultados: dict) -> pd.DataFrame:

    if not isinstance(resultados, dict):
        raise TypeError(
            "O argumento esperado para 'resultados' precisar ser um dicionário!"
        )
    
    df_indicadores = []
    for resultado in resultados.values():
        #print("resultado:", resultado)
        if resultado.get("status") != "sucesso":
            continue

        df_indicador = resultado.get("resultado")
        if not isinstance(df_indicador, pd.DataFrame):
            continue

        if df_indicador.empty:
            continue

        
        df_indicadores.append(df_indicador)
        
    if not df_indicadores:
            return pd.DataFrame()

    dataframe_final = pd.concat(
        df_indicadores,
        ignore_index=True
    )
    dataframe_final = dataframe_final.sort_values(
        by=["data", "indicador"]
    )
    dataframe_final = dataframe_final.reset_index(drop=True)

    return dataframe_final