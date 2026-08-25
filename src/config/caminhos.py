from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parents[2]

CAMINHO_DADOS = RAIZ_PROJETO / "data"
CAMINHO_BRONZE = CAMINHO_DADOS / "bronze"
CAMINHO_SILVER = CAMINHO_DADOS / "silver"
CAMINHO_GOLD = CAMINHO_DADOS / "gold"