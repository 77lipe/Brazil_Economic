""" Configurações das séries econômicas. """

INDICADORES_BCB = {
    "meta_selic": {
        "codigo": 432,
        "nome": "Meta Selic",
        "desc": "Meta da taxa Selic definida pelo copom",
        "unidade": "% por ano",
        "frequencia": "diaria",
    },
    "dolar_venda": {
        "codigo": 1,
        "nome": "Dólar comercial - venda",
        "descricao": "Taxa de câmbio do dólar americano para venda",
        "unidade": "R$ por US$",
        "frequencia": "diaria,"
    },
}

#print(INDICADORES_BCB)