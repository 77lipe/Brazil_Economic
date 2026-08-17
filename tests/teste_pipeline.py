from src.pipeline.processar_indicador_bcb import processar_indicador_bcb
from src.pipeline.executar_pipeline import execute_pipeline
from src.transformation.consolidar_indicadores import consolidar_indicadores_bcb
from src.storage.cmd_gold import salvar_gold

result_execute = execute_pipeline(
    data_inicial="01/01/2025",
    data_final="31/01/2025"
)

df_gold = consolidar_indicadores_bcb(result_execute)

caminho_gold = salvar_gold(df_gold, "Indicadores_bcb")
print(f"Tabela Gold salva em: {caminho_gold}")