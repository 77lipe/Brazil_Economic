""" Função de execução do pipeline COMPLETO """

from pathlib import Path

from src.pipeline.executar_pipeline import execute_pipeline
from src.transformation.consolidar_indicadores import dfInal_indicadores_bcb
from src.storage.cmd_gold import salvar_gold

def execute_pipeline_complete(data_inicial: str, data_final: str) -> Path:
    resultados = execute_pipeline(
        data_inicial=data_inicial,
        data_final=data_final
    )

    df_gold = dfInal_indicadores_bcb(
        resultados=resultados
    )
    if df_gold.empty:
        raise ValueError(
            "Nenhum dado válido foi encontrado para gerar a camada Gold."
        )

    caminho_gold = salvar_gold(
        dataframe=df_gold,
        nome_tabela="indicadores_bcb"
    )

    print("\nPipeline concluído com sucesso.")
    print(f"arquivo Gold: {caminho_gold}")

    return caminho_gold

if __name__ == "__main__":
    execute_pipeline_complete(
        data_inicial="01/01/2025",
        data_final="31/12/2025"
    )