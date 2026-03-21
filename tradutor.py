import pandas as pd
from deep_translator import GoogleTranslator

arquivo_origem = r''
arquivo_destino = r''

print("Carregando os dados...")
df = pd.read_csv(arquivo_origem)
df_subset = df.head(150).copy()

nome_coluna = 'text_'

print(f"Coluna identificada para tradução: '{nome_coluna}'")

translator = GoogleTranslator(source='auto', target='pt')

print(f"Traduzindo 150 linhas da coluna '{nome_coluna}'... Isso leva cerca de 1 minuto.")

try:
    df_subset['text_traduzido'] = df_subset[nome_coluna].apply(lambda x: translator.translate(str(x)))

    df_subset.to_excel(arquivo_destino, index=False)
    print(f"\n✅ SUCESSO! Arquivo salvo em:\n{arquivo_destino}")

except Exception as e:
    print(f"\n❌ Ocorreu um erro durante a tradução: {e}")