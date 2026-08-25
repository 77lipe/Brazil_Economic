from datetime import datetime

FORMATO_DATA_ENTRADA = "%d/%m/%Y"
FORMATO_DATA_SAIDA = "%Y-%m-%d"

def formatar_data(data: str) -> str:
    data_convertida = datetime.strptime(
        data,
        FORMATO_DATA_ENTRADA
    )
    data_formatada = data_convertida.strftime(FORMATO_DATA_SAIDA)
    return data_formatada