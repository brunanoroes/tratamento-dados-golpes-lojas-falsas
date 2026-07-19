"""
Tradução da amostra do Fake Reviews Dataset para português.

Fonte externa (Externo 6 do BrScamsFacebook): Fake Reviews Dataset, disponível no
Kaggle. O arquivo original NÃO é redistribuído neste repositório por estar sujeito
à licença de seus autores — ver README.md, seção Dependências.

Uso:
    1. Baixe o dataset do Kaggle e salve o CSV nesta pasta como 'fake_reviews.csv'
       (ou ajuste ARQUIVO_ORIGEM abaixo).
    2. python tradutor.py

Saída: reviews_traduzidos.xlsx — 150 avaliações traduzidas para o português,
alimentando a categoria "Fraudes em Lojas Virtuais Falsas".
"""

import os
import sys

import pandas as pd
from deep_translator import GoogleTranslator

# ------------------------------------------------------------------
# Configuração
# ------------------------------------------------------------------
ARQUIVO_ORIGEM = "fake_reviews.csv"      # entrada: CSV baixado do Kaggle
ARQUIVO_DESTINO = "reviews_traduzidos.xlsx"  # saída versionada neste repositório
COLUNA_TEXTO = "text_"                    # coluna de texto no dataset original
N_LINHAS = 150                            # tamanho da amostra usado no trabalho

if not os.path.exists(ARQUIVO_ORIGEM):
    sys.exit(
        f"Arquivo de entrada '{ARQUIVO_ORIGEM}' nao encontrado.\n"
        "Baixe o Fake Reviews Dataset do Kaggle e salve o CSV nesta pasta com esse "
        "nome, ou ajuste a constante ARQUIVO_ORIGEM no topo deste script.\n"
        "Ver README.md, secao Dependencias."
    )

print("Carregando os dados...")
df = pd.read_csv(ARQUIVO_ORIGEM)

if COLUNA_TEXTO not in df.columns:
    sys.exit(
        f"Coluna '{COLUNA_TEXTO}' nao encontrada em '{ARQUIVO_ORIGEM}'.\n"
        f"Colunas disponiveis: {list(df.columns)}"
    )

df_subset = df.head(N_LINHAS).copy()
print(f"Coluna identificada para traducao: '{COLUNA_TEXTO}'")
print(f"Traduzindo {len(df_subset)} linhas... Isso leva cerca de 1 minuto.")

translator = GoogleTranslator(source="auto", target="pt")

try:
    df_subset["text_traduzido"] = df_subset[COLUNA_TEXTO].apply(
        lambda x: translator.translate(str(x))
    )
    df_subset.to_excel(ARQUIVO_DESTINO, index=False)
    print(f"\nSUCESSO! Arquivo salvo em: {ARQUIVO_DESTINO}")
except Exception as e:
    print(f"\nOcorreu um erro durante a traducao: {e}")
    sys.exit(1)
