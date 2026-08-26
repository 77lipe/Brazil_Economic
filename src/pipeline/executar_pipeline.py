""" Arquivo que executará o pipeline - parcial """

from src.config.indicadores_bcb import INDICADORES_BCB
from src.pipeline.processar_indicador_bcb import processar_indicador_bcb
from src.extraction.validar_datas import *

def execute_pipeline(data_inicial: str, data_final: str) -> dict:

    validar_periodo_bcb(
        data_inicial=data_inicial,
        data_final=data_final
    )

    resultados = {}

    for indicador in INDICADORES_BCB:
        print(f'\nProcessando indicador: {indicador}')
        try:

            resultado = processar_indicador_bcb(indicador, data_inicial=data_inicial, data_final=data_final)
        except Exception as erro:
            resultados[indicador] = {
                "status": "erro",
                "tipo_erro": type(erro).__name__,
                "erro": str(erro)
            }

            print(
                f"Erro ao processar {indicador}: {erro}"
                f"\n{type(erro).__name__}")

            continue
        resultados[indicador] = {
            "status": "sucesso",
            "resultado": resultado
        } 
        print(f"Indicador concluído: {indicador}")

    return resultados

if __name__ == "__main__":
    resultados = execute_pipeline("01/01/2025", "31/12/2025")
    # print("\nResultados:\n", resultados)

    print(f"\nResumo da execução:")
    for indicador, resultado in resultados.items():
        print(f"{indicador}: {resultado['status']}")