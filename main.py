import argparse

from src.pipeline.execute_pipeline_complete import execute_pipeline_complete

def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Extrai indicadores econômicos do BCB e gera "
            "as camadas Bronze, Silver e Gold"
        )
    )

    parser.add_argument(
        "--data-inicial",
        required=True,
        help="Data Inicial no formato: 'DD/MM/AAAA'"
    )

    parser.add_argument(
        "--data-final",
        required=True,
        help="Data Final no formato: 'DD/MM/AAAA'"
    )

    return parser

def main() -> None:
    parser = criar_parser()
    argumentos = parser.parse_args()

    try:
        caminho_gold = execute_pipeline_complete(data_inicial=argumentos.data_inicial, data_final=argumentos.data_final)
    except Exception as erro:
        raise SystemExit(
            f"Falha na execução: {type(erro).__name__}: {erro}"
        )

    print(f'\nArquivo disponível para análise: {caminho_gold}')

# Quando o arquivo for chamado, 
if __name__ == "__main__":
    main()