import streamlit as st

from src.storage.ler_gold import carregar_dados_gold

st.set_page_config(
    page_title="Economia do Brasil",
    layout="wide"
)

@st.cache_data
def carregar_dados_dashboard():
    return carregar_dados_gold()

st.title("Economia do Brasil")
st.caption(
    "Indicadores econômicos obtidos do Banco Central do Brasil."
)

try:
    dados = carregar_dados_dashboard()
except (FileNotFoundError, TypeError, ValueError) as erro:
    st.error(f"Não foi possivel carregar a camada Gold: {erro}")
    st.stop()

quantidade_registros = len(dados)
quantidade_indicadores = dados["indicador"].nunique()
data_inicial = dados["data"].min().strftime("%d/%m/%Y")
data_final = dados["data"].max().strftime("%d/%m/%Y")

coluna_registros, coluna_indicadores, coluna_inicio, coluna_final  = (
    st.columns(4)
)

coluna_registros.metric(
    label="Registros",
    value=quantidade_registros
)

coluna_indicadores.metric(
    label="Indicadores",
    value=quantidade_indicadores
)

coluna_inicio.metric(
    label="Início do período",
    value=data_inicial
)

coluna_final.metric(
    label="Final do período",
    value=data_final
)

st.divider()
st.subheader("Dados consolidados")

st.dataframe(
    dados,
    use_container_width=True,
    hide_index=True
)