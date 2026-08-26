""" Função de validar as datas correspondentes a API """

from datetime import datetime

FORMATO_DATA_BCB = "%d/%m/%Y"

def validar_periodo_bcb(
        data_inicial: str,
        data_final: str
) -> None:

    if not isinstance(data_inicial, str) or not isinstance(data_final, str):
        raise TypeError(
            "As datas dever estar no formato de string"
        )
    try:
        data_inicial_convertida = datetime.strptime(
            data_inicial,
            FORMATO_DATA_BCB
        )

        data_final_convertida = datetime.strptime(
            data_final,
            FORMATO_DATA_BCB
        )
    except (TypeError, ValueError) as erro:
        raise ValueError(
            "As datas devem utilizar o formato DD/MM/AAAA"
        ) from erro

    if data_inicial_convertida > data_final_convertida:
        raise ValueError(
            "A data inicial não pode ser posterior a data final"
        )