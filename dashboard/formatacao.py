FORMATOS_INDICADORES = {
    "meta_selic": {
        "casas_decimais": 2,
        "prefixo": "",
        "sufixo": "% a.a.",
        "prefixo_variacao": "",
        "sufixo_variacao": " p.p"
    },
    "dolar_venda": {
        "casas_decimais": 4,
        "prefixo": "R$ ",
        "sufixo": "",
        "prefixo_variacao": "R$ ",
        "sufixo_variacao": ""
    }
}

def formatar_numero_brasileiro(valor: float, casas_decimais: int) -> str:
    texto = f"{valor:,.{casas_decimais}f}"
    texto = texto.replace(",","_")
    texto = texto.replace(".", ",")
    texto = texto.replace("_", ".")

    return texto

def formatar_valor_indicador(valor: float, nome_indicador: str) -> str:

    formato = FORMATOS_INDICADORES.get(
        nome_indicador,
        {
            "casas_decimais": 4,
            "prefixo": "",
            "sufixo": ""
        }
    )

    numero = formatar_numero_brasileiro(
        valor=valor,
        casas_decimais=formato["casas_decimais"]
    )

    return (
        f"{formato['prefixo']}"
        f"{numero}"
        f"{formato['sufixo']}"
    )

def formatar_variacao_indicador(
        variacao: float | None, 
        nome_indicador: str
) -> str | None:

    if variacao is None:
        return None

    formato = FORMATOS_INDICADORES.get(
        nome_indicador,
        {
            "casas_decimais": 4,
            "prefixo_variacao": "",
            "sufixo_variacao": ""
        }
    )

    sinal = "+" if variacao > 0 else ""
    numero = formatar_numero_brasileiro(
        valor=variacao,
        casas_decimais=formato["casas_decimais"]
    )

    return(
        f"{sinal}"
        f"{formato['prefixo_variacao']}"
        f"{numero}"
        f"{formato['sufixo_variacao']}"
    )