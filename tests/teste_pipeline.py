from src.pipeline.processar_indicador_bcb import processor_indicador_bcb

df_meta_selic = processor_indicador_bcb(
    nome_indicador="meta_selic",
    data_inicial="01/01/2025",
    data_final="31/01/2025"
)

print("META SELIC")
print(df_meta_selic.head())
print("\nTipos")
print(df_meta_selic.dtypes)
print("\nSHAPE")
print(df_meta_selic.shape)