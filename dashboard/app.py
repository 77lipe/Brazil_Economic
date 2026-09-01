import streamlit as st

from src.storage.ler_gold import carregar_dados_gold
from dashboard.formatacao import (formatar_valor_indicador, formatar_variacao_indicador)
from dashboard.graficos import criar_grafico_serie

st.set_page_config(
    page_title="Economia do Brasil",
    layout="wide"
)

st.title("Economia do Brasil")
st.caption(
    "Inidcadores econômicos obtidos do Banco Central do Brasil"
)

try:
    dados = carregar_dados_gold()
except (FileNotFoundError, TypeError, ValueError) as erro:
    st.error(f"Não foi possível carregar os dados da Gold: {erro}")
    st.stop()

tabela_indicadores = (
    dados[["indicador", "nome"]]
    .drop_duplicates()
    .sort_values(by="nome")
)

nomes_indicadores = dict(
    zip(
        tabela_indicadores["indicador"],
        tabela_indicadores["nome"],
    )
)

data_minima = dados["data"].min().date()
data_maxima = dados["data"].max().date()

def obter_resumo_serie(dataframe):

    serie_ordenada = dataframe.sort_values(
        by="data"
    ).reset_index(drop=True)

    registro_atual = serie_ordenada.iloc[-1]
    variacao = None

    if len(serie_ordenada) >= 2:
        valor_anterior = float(
            serie_ordenada.iloc[-2]["valor"]
        )

        variacao = float(registro_atual["valor"]) - valor_anterior

    return registro_atual, variacao

st.subheader("Visão Geral")
indicadores_disponiveis = (
    dados["indicador"]
    .drop_duplicates()
    .sort_values()
    .tolist()
)

colunas_resumo = st.columns(
    len(indicadores_disponiveis)
)

for coluna, nome_indicador in zip(
    colunas_resumo,
    indicadores_disponiveis
):
    serie_indicador = dados.loc[dados["indicador"] == nome_indicador]

    registro_atual, variacao = obter_resumo_serie(
        serie_indicador
    )
    valor_formatado = formatar_valor_indicador(
        valor=float(registro_atual["valor"]),
        nome_indicador=nome_indicador
    )
    variacao_formatada = formatar_variacao_indicador(
        variacao=variacao,
        nome_indicador=nome_indicador
    )

    coluna.metric(
        label=registro_atual["nome"],
        value=valor_formatado,
        delta=variacao_formatada,
        delta_color="off",
        border=True
    )

    coluna.caption(
        "Atualizada em "
        f"{registro_atual['data'].strftime('%d/%m/%Y')}"
    )

st.divider()

st.sidebar.header("Filtros")
indicador_selecionado = st.sidebar.selectbox(
    label="Indicador",
    options=tabela_indicadores["indicador"].tolist(),
    format_func=lambda indicador: nomes_indicadores[indicador]
)

data_inical = st.sidebar.date_input(
    label="Data inicial",
    value=data_minima,
    min_value=data_minima,
    max_value=data_maxima,
    format="DD/MM/YYYY"
)

data_final = st.sidebar.date_input(
    label="Data final",
    value=data_maxima,
    min_value=data_minima,
    max_value=data_maxima,
    format="DD/MM/YYYY"
)

if data_inical > data_final:
    st.sidebar.error(
        "A data inicial deve ser menor do que a data final!"
    )
    st.stop()

mascara_filtro = (
    (dados["indicador"] == indicador_selecionado)
    &(dados["data"].dt.date >= data_inical)
    &(dados["data"].dt.date <= data_final)
)

dados_filtrados = dados.loc[mascara_filtro].copy()
if dados_filtrados.empty:
    st.warning(
        "Não existem registros para o indicador e período selecionados."
    )
    st.stop()

dados_filtrados = dados_filtrados.sort_values(
    by="data"
).reset_index(drop=True)

registro_atual = dados_filtrados.iloc[-1]

valor_atual = float(registro_atual["valor"])
data_valor_atual = registro_atual["data"].strftime("%d/%m/%Y")
unidade = registro_atual["unidade"]

variacao = None

registro_atual, variacao = obter_resumo_serie(
    dados_filtrados
)

valor_formatado = formatar_valor_indicador(
    valor=float(registro_atual["valor"]),
    nome_indicador=indicador_selecionado
)

variacao_formatada = formatar_variacao_indicador(
    variacao=variacao,
    nome_indicador=indicador_selecionado
)

data_valor_atual = registro_atual["data"].strftime("%d/%m/%Y")

st.subheader(nomes_indicadores[indicador_selecionado])
coluna_valor, coluna_data, coluna_registros = st.columns(3)

coluna_valor.metric(
    label="Valor mais recente",
    value=valor_formatado,
    delta=variacao_formatada,
    delta_color="off"
)

coluna_data.metric(
    label="Data da observação",
    value=data_valor_atual
)
coluna_registros.metric(
    label="Registros no período",
    value=len(dados_filtrados)
)

st.caption(f"Unidade: {unidade}")
st.divider()

st.subheader("Evolução no período")

grafico = criar_grafico_serie(
    dataframe=dados_filtrados,
    nome_indicador=indicador_selecionado,
    unidade=unidade
)

st.altair_chart(
    grafico,
    width="stretch"
)

if indicador_selecionado == "meta_selic":
    st.caption(
        "O formato em degraus representa os momentos em que "
        "a Meta Selic foi mantida ou alterada."
    )
else:
    st.caption(
        "A linha conecta as cotações disponíveis em ordem cronológica."
    )
# st.line_chart(
#     data=dados_filtrados,
#     x="data",
#     y="valor",
#     x_label="Data",
#     y_label=unidade,
#     width="stretch"
# )
st.divider()

st.subheader("Observações")
dados_exibicao = dados_filtrados[
    [
        "data",
        "valor",
        "nome",
        "unidade",
        "frequencia",
        "fonte"
    ]
]

st.dataframe(
    dados_exibicao,
    width="stretch",
    hide_index=True
)