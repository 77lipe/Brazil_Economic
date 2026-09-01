import altair as alt
import pandas as pd

CORES_INDICADORES = {
    "meta_selic": "#D62728",
    "dolar_venda": "#1F77B4"
}

def criar_grafico_serie(
        dataframe: pd.DataFrame,
        nome_indicador: str,
        unidade: str
) -> alt.Chart:

    if dataframe.empty:
        raise ValueError(
            "Não é possivel criar um gráfico sem dados."
        )

    if nome_indicador == "meta_selic":
        interpolacao = "step-after"
        exibir_pontos = False
    else:
        interpolacao = "linear"
        exibir_pontos = True

    cor = CORES_INDICADORES.get(
        nome_indicador,
        "#4c78a8"
    )

    grafico = (
        alt.Chart(dataframe)
        .mark_line(
            color=cor,
            strokeWidth=3,
            interpolate=interpolacao,
            point=exibir_pontos
        )

        .encode(
            x=alt.X(
                "data:T",
                title="Data",
                axis=alt.Axis(
                    format="%d/%m/%Y",
                    labelAngle=-45
                )
            ),
            y=alt.Y(
                "valor:Q",
                title=unidade,
                scale=alt.Scale(zero=False)
            ),
            tooltip=[
                alt.Tooltip(
                    "data:T",
                    title="Data",
                    format="%d/%m/%Y"
                ),
                alt.Tooltip(
                    "valor:Q",
                    title="Valor",
                    format=".4f"
                )
            ]
        )

        .properties(
            height=420
        )
        .interactive()
    )

    return grafico