# tratamento-dados-golpes-lojas-falsas — Tradução do Fake Reviews Dataset para Português

**Artigo relacionado:** *VeritaPlugin: Uma Extensão de Navegador para Detecção Semântica de Fraudes no Facebook* — Universidade Federal Fluminense (UFF)

**Resumo do artigo.** A Engenharia Social em redes sociais explora vulnerabilidades para
iludir usuários, tornando defesas técnicas tradicionais insuficientes. Este trabalho
apresenta o VeritaPlugin, uma extensão de navegador que detecta fraudes no Facebook por
meio de um pipeline híbrido BERTimbau, RAG determinístico e GPT-4o. A arquitetura opera em
conformidade com a LGPD e o resultado apresenta ao usuário a categoria do golpe,
enquadramento legal e ações recomendadas. Para calibração, foi construído e disponibilizado
o dataset BrScamsFacebook, com 450 instâncias de golpes reais do contexto brasileiro. Na
avaliação técnica, o classificador obteve F1-macro de 0,763 ± 0,034 na validação cruzada
k=5, superando o baseline.

**Resumo do artefato.** Este repositório contém o script de **tradução automática de uma
amostra do Fake Reviews Dataset para o português**, responsável pela fonte *Externo 6* do
dataset **BrScamsFacebook**. O Fake Reviews Dataset reúne cerca de 40.000 avaliações de
produtos, distinguindo avaliações escritas por consumidores reais daquelas geradas
artificialmente — material diretamente relevante para a categoria **Fraudes em Lojas
Virtuais Falsas**, já que avaliações fabricadas são o principal instrumento de legitimação
de uma loja fraudulenta perante a vítima. O script recorta 150 avaliações, traduz a coluna
de texto para o português via `deep-translator` e exporta para Excel, preservando as
colunas originais ao lado da tradução para permitir auditoria. A saída versionada,
`reviews_traduzidos.xlsx`, é o produto efetivamente incorporado ao dataset final.

**Artefato principal:** [VeritaPlugin](https://github.com/brunanoroes/VeritaPlugin)
**Autora:** Bruna Norões — brunanoroes@id.uff.br

---

# Estrutura do readme.md

Este README segue os requisitos mínimos do Comitê Técnico de Artefatos do SBSeg 2026:

| Seção | Conteúdo |
|---|---|
| **Título projeto** | Identificação do artefato, vínculo com o artigo e resumo |
| **Estrutura do readme.md** | Esta seção — mapa do documento e organização do repositório |
| **Selos Considerados** | Selos pleiteados na avaliação |
| **Informações básicas** | Ambiente de execução, funcionamento do script e parâmetros |
| **Dependências** | Versões de linguagem, bibliotecas e a base de origem **não redistribuída** |
| **Preocupações com segurança** | Conteúdo, licenciamento e limitações da tradução automática |
| **Instalação** | Passo a passo, incluindo a obtenção do arquivo de entrada |
| **Teste mínimo** | Execução que demonstra o funcionamento, com e sem o arquivo de entrada |
| **Experimentos** | Papel deste repositório na composição do dataset |
| **LICENSE** | Licença do artefato |

## Organização do repositório

```
tratamento-dados-golpes-lojas-falsas/
├── tradutor.py                # Script de tradução EN → PT
├── reviews_traduzidos.xlsx    # Saída — 150 avaliações traduzidas
├── LICENSE
└── README.md
```

> **O arquivo de entrada não está versionado.** O Fake Reviews Dataset original está
> sujeito à licença de seus autores e **não é redistribuído** neste repositório. Para
> reexecutar o script é necessário obtê-lo no Kaggle — ver *Instalação*, Passo 4. A saída
> versionada permite verificar o resultado **sem** essa etapa.

---

# Selos Considerados

Os selos considerados são: **Artefatos Disponíveis (SeloD)** e **Artefatos Funcionais
(SeloF)**.

| Selo | Onde é atendido neste README |
|---|---|
| **Disponíveis (D)** | Repositório público e estável no GitHub, com este README e licença MIT |
| **Funcionais (F)** | Seções *Dependências* (com versões), *Informações básicas* (ambiente), *Instalação* e *Teste mínimo* |

> Este repositório documenta a **origem de parte dos dados** do artefato principal
> [VeritaPlugin](https://github.com/brunanoroes/VeritaPlugin). Ele não sustenta uma
> reivindicação quantitativa própria — ver *Experimentos*.
>
> **Nota de transparência para o avaliador:** por depender de um arquivo de entrada não
> redistribuível, a execução completa deste script exige um download manual do Kaggle. O
> **Teste A** do *teste mínimo* verifica o artefato **sem** essa dependência, e é o caminho
> recomendado para a avaliação.

---

# Informações básicas

## Ambiente de execução

| Item | Especificação |
|---|---|
| Sistema operacional | Windows 11 (também validado em Ubuntu 22.04 LTS) |
| Python | 3.10+ |
| Rede | **Necessária** — o script chama a API de tradução do Google |
| GPU | Não necessária |

## Requisitos de hardware

| Recurso | Mínimo |
|---|---|
| CPU | 2 núcleos x86-64 |
| RAM | 512 MB |
| Disco | 80 MB (dependências) + ≈ 60 MB (dataset do Kaggle, se baixado) |
| Banda | ≈ 3 MB para 150 avaliações |
| Tempo | ≈ 1 minuto para 150 avaliações |

## Como o script funciona

```
fake_reviews.csv  (baixado do Kaggle)
      │
      ▼
 verificação: o arquivo existe? a coluna 'text_' existe?
      │        └── se não, encerra com mensagem explicativa
      ▼
 pandas.read_csv()  →  DataFrame
      │
      ▼
 head(150)  →  recorte da amostra
      │
      ▼
 traduz a coluna 'text_'  EN → PT  via GoogleTranslator(source='auto', target='pt')
      │
      ▼
 grava o resultado em NOVA coluna 'text_traduzido'
      │        (a coluna original é preservada para auditoria)
      ▼
 to_excel()  →  reviews_traduzidos.xlsx
```

### Decisões de projeto relevantes

| Decisão | Motivo |
|---|---|
| Tradução em **nova coluna** (`text_traduzido`) | Diferentemente das outras fontes do trabalho, aqui o texto original em inglês é **preservado ao lado** da tradução, permitindo auditar caso a caso a qualidade da tradução automática |
| Amostra de 150 avaliações | O BrScamsFacebook é balanceado em 75 instâncias por categoria; 150 dá margem para a curadoria manual sem traduzir as 40.000 avaliações da base |
| `source='auto'` | Detecção automática do idioma de origem |
| Verificação prévia de arquivo e coluna | O script encerra com mensagem explicativa se o arquivo de entrada estiver ausente ou a coluna não existir, em vez de falhar com um traceback obscuro |
| Entrada não versionada | Respeita a licença dos autores do Fake Reviews Dataset |

## Parâmetros configuráveis

No topo de `tradutor.py`:

| Constante | Descrição | Valor padrão |
|---|---|---|
| `ARQUIVO_ORIGEM` | CSV de entrada, baixado do Kaggle | `"fake_reviews.csv"` |
| `ARQUIVO_DESTINO` | Planilha de saída | `"reviews_traduzidos.xlsx"` |
| `COLUNA_TEXTO` | Coluna de texto no dataset original | `"text_"` |
| `N_LINHAS` | Tamanho da amostra | `150` |

Se você salvar o CSV do Kaggle com outro nome, ajuste `ARQUIVO_ORIGEM`.

---

# Dependências

## Linguagem e runtime

| Dependência | Versão |
|---|---|
| Python | 3.10+ |
| pip | 22+ |

## Bibliotecas Python

| Biblioteca | Versão testada | Finalidade |
|---|---|---|
| `pandas` | 2.x | Leitura do `.csv` e escrita do `.xlsx` |
| `deep-translator` | 1.11.x | Tradução automática inglês → português (backend Google) |
| `openpyxl` | 3.1.x | Engine de escrita do `.xlsx` |

## Recursos de terceiros

| Recurso | Acesso | Custo |
|---|---|---|
| **API de tradução do Google** (via `deep-translator`) | Endpoint público, sem chave de API | Gratuito |
| **Fake Reviews Dataset** | Kaggle — requer conta gratuita para download | Gratuito |

**Nenhuma chave de API é necessária.** Não há custo financeiro.

## Base de origem — não redistribuída

| Base | Origem | Situação neste repositório |
|---|---|---|
| **Fake Reviews Dataset** | Kaggle (~40.000 avaliações de produtos, reais *vs.* geradas por computador) | **Não versionada.** Sujeita à licença dos autores originais. Deve ser baixada manualmente para reexecutar o script |

> Esta é a **única dependência de acesso restrito** do repositório — restrita no sentido de
> exigir uma conta gratuita no Kaggle, não de exigir autorização especial. A saída
> versionada (`reviews_traduzidos.xlsx`) torna a verificação possível sem esse passo.

---

# Preocupações com segurança

A execução deste artefato **não oferece risco à máquina do avaliador**: o script lê um CSV
local, faz chamadas HTTPS ao serviço de tradução e escreve um `.xlsx` no próprio diretório.
Não há privilégios administrativos nem execução de código de terceiros.

## 1. Conteúdo dos dados

Diferentemente das demais fontes do trabalho, o Fake Reviews Dataset contém **avaliações de
produtos**, não mensagens de golpe dirigidas a vítimas. O conteúdo é, portanto,
**substancialmente menos sensível**: não há links maliciosos, solicitações de dados
bancários nem contatos de golpistas.

O risco relevante aqui é de outra natureza: as avaliações "falsas" da base foram **geradas
artificialmente por modelo de linguagem**, e não coletadas de fraudes reais. Ver item 3.

## 2. Dados pessoais

As avaliações da base original são de produtos, majoritariamente sem identificação de
autor. Ainda assim, o material é disponibilizado **exclusivamente para fins acadêmicos**.

## 3. Validade da fonte — limitação metodológica importante

Esta é a ressalva mais relevante deste repositório, e deve ser considerada na leitura dos
resultados do artigo:

- As avaliações "falsas" do dataset original foram **geradas por modelo de linguagem** para
  fins de pesquisa, e **não são avaliações fraudulentas reais** capturadas de lojas falsas
- Consequentemente, elas representam o fenômeno "texto gerado artificialmente", que **não é
  idêntico** ao fenômeno "avaliação fraudulenta plantada por uma loja falsa brasileira"
- Somando-se a isso a **tradução automática** (item 4), o material passa por duas camadas de
  artificialidade antes de chegar ao classificador

A mitigação adotada no trabalho foi a **curadoria manual** e a combinação com material
coletado originalmente em português — ver *Experimentos*. Ainda assim, esta é a fonte
externa de menor fidelidade ao fenômeno-alvo, e isso é registrado aqui por transparência.

## 4. Qualidade da tradução automática

A tradução é automática e **não foi revisada linha a linha**. O script preserva a coluna
original em inglês ao lado da tradução, o que **permite auditar a qualidade caso a caso** —
uma garantia que as demais fontes traduzidas do trabalho não oferecem.

## 5. Licenciamento da base de origem

O Fake Reviews Dataset é de terceiros e **não é redistribuído** neste repositório. Quem
baixá-lo do Kaggle fica sujeito aos termos de uso da plataforma e à licença dos autores.

## 6. Dependência de serviço externo

A API de tradução do Google está sujeita a limite de taxa e a mudanças sem aviso. Por isso a
saída está versionada e é a fonte de verdade para a reprodução do dataset.

---

# Instalação

Tempo total: aproximadamente **3 minutos** (sem o download do Kaggle) ou **8 minutos** (com
ele).

## Passo 1 — Obter o repositório

```bash
git clone https://github.com/brunanoroes/tratamento-dados-golpes-lojas-falsas.git
cd tratamento-dados-golpes-lojas-falsas
```

## Passo 2 — Criar o ambiente virtual

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Passo 3 — Instalar as dependências

```bash
pip install pandas openpyxl deep-translator
```

> Tempo esperado: 1–2 minutos. Espaço em disco: ≈ 80 MB.

## Passo 4 — Obter o arquivo de entrada (**opcional**)

**Necessário apenas para reexecutar a tradução.** Para verificar o artefato, o Teste A do
*teste mínimo* dispensa este passo.

1. Acesse o **Fake Reviews Dataset** no Kaggle (requer conta gratuita)
2. Baixe o arquivo CSV
3. Salve-o **nesta pasta** com o nome `fake_reviews.csv`

Se preferir outro nome, ajuste a constante `ARQUIVO_ORIGEM` no topo de `tradutor.py`.

> O script verifica a presença do arquivo e encerra com instruções caso ele não seja
> encontrado — não é possível executá-lo por engano sem a entrada correta.

## Passo 5 — Verificar a instalação

```bash
python -c "
import pandas, openpyxl
from deep_translator import GoogleTranslator
print('dependencias ok')
print('traducao:', GoogleTranslator(source='en', target='pt').translate('This product is excellent'))
"
```

Saída esperada:
```
dependencias ok
traducao: Este produto é excelente
```

Ao final deste passo, o ambiente está pronto.

---

# Teste mínimo

## Teste A — Verificar a saída versionada (≈ 30 segundos, **sem rede e sem o Kaggle**)

**Este é o teste recomendado para a avaliação.** Ele verifica o produto efetivamente usado
no trabalho, sem exigir o download do dataset original:

```bash
python - <<'PY'
import pandas as pd

df = pd.read_excel("reviews_traduzidos.xlsx")
print(f"Registros : {len(df)}")
print(f"Colunas   : {list(df.columns)}")

assert "text_traduzido" in df.columns, "coluna de tradução ausente"
print("\n--- 3 pares original / tradução ---")
for orig, trad in df[["text_", "text_traduzido"]].head(3).values:
    print(f"\n  EN: {str(orig)[:110]}")
    print(f"  PT: {str(trad)[:110]}")
PY
```

**Resultado esperado:** o arquivo carrega com **150 registros**, contendo tanto a coluna
original `text_` (em inglês) quanto `text_traduzido` (em português). Os pares permitem
verificar diretamente a qualidade da tradução.

> Recursos: < 512 MB de RAM, ≈ 30 segundos. Sem rede, sem custo.

## Teste B — Tradução de uma amostra reduzida (≈ 30 segundos, requer rede)

Exercita a lógica de tradução sem precisar do arquivo do Kaggle, usando os textos originais
já presentes na saída versionada:

```bash
python - <<'PY'
import pandas as pd
from deep_translator import GoogleTranslator

df = pd.read_excel("reviews_traduzidos.xlsx").head(3)
tradutor = GoogleTranslator(source="auto", target="pt")

for orig, trad_versionada in df[["text_", "text_traduzido"]].values:
    nova = tradutor.translate(str(orig)[:400])
    print(f"\nEN            : {str(orig)[:90]}")
    print(f"PT (versionada): {str(trad_versionada)[:90]}")
    print(f"PT (agora)     : {str(nova)[:90]}")
PY
```

**Resultado esperado:** três blocos comparando a tradução versionada com uma nova tradução
do mesmo texto. Elas devem ser **semanticamente equivalentes**, ainda que não idênticas
palavra a palavra — o que evidencia diretamente o não determinismo discutido em
*Experimentos*.

## Teste C — Execução completa (opcional, requer o arquivo do Kaggle, ≈ 1 minuto)

```bash
python tradutor.py
```

**Resultado esperado (com o arquivo presente):**
```
Carregando os dados...
Coluna identificada para traducao: 'text_'
Traduzindo 150 linhas... Isso leva cerca de 1 minuto.

SUCESSO! Arquivo salvo em: reviews_traduzidos.xlsx
```

**Resultado esperado (sem o arquivo):** o script encerra com a mensagem explicativa
indicando como obter a entrada — este é o comportamento correto e também vale como
verificação.

> **Atenção:** com o arquivo presente, este comando **sobrescreve**
> `reviews_traduzidos.xlsx`. Para restaurar: `git checkout reviews_traduzidos.xlsx`.

## Solução de problemas

| Problema | Causa provável | Solução |
|---|---|---|
| `Arquivo de entrada 'fake_reviews.csv' nao encontrado` | Dataset do Kaggle ausente | Comportamento esperado — use o Teste A, ou complete o Passo 4 da instalação |
| `Coluna 'text_' nao encontrada` | CSV do Kaggle com esquema diferente | O script lista as colunas disponíveis; ajuste `COLUNA_TEXTO` no topo do arquivo |
| Erro durante a tradução | Limite de taxa da API do Google | Aguarde alguns minutos e repita |
| `ModuleNotFoundError: openpyxl` | Engine de Excel ausente | `pip install openpyxl` |
| `PermissionError` ao salvar | Planilha aberta no Excel | Feche o arquivo e repita |
| Execução lenta | Uma chamada de rede por linha | Comportamento esperado: ≈ 0,4 s por avaliação |

---

# Experimentos

Este repositório **não sustenta uma reivindicação quantitativa própria**: ele documenta a
**procedência** de parte dos dados do artefato principal.

As reivindicações do artigo são reproduzidas em:
**#1** [treinamento-BERTimbau](https://github.com/brunanoroes/treinamento-BERTimbau) ·
**#2** [Treinamento_TF-IDF-SVM](https://github.com/brunanoroes/Treinamento_TF-IDF-SVM) ·
**#3** [evolucao-prompt-RAG](https://github.com/brunanoroes/evolucao-prompt-RAG) ·
**#4** [VeritaPlugin](https://github.com/brunanoroes/VeritaPlugin) ·
**#5 e #6** [ConteudoExtraVeritaPlugin](https://github.com/brunanoroes/ConteudoExtraVeritaPlugin).

## Contribuição para o dataset BrScamsFacebook

| Item | Valor |
|---|---|
| Identificação da fonte | **Externo 6** |
| Base de origem | Fake Reviews Dataset (Kaggle) |
| Avaliações traduzidas | 150 |
| Categoria alimentada | **Fraudes em Lojas Virtuais Falsas** |
| Produto | `reviews_traduzidos.xlsx` |

A consolidação das seis fontes externas está documentada em
[ConteudoExtraVeritaPlugin](https://github.com/brunanoroes/ConteudoExtraVeritaPlugin),
arquivo `Datasets Externos/Golpes Datasets Externos.xlsx`.

## Por que avaliações falsas alimentam a categoria de lojas virtuais falsas

Uma loja virtual fraudulenta não convence a vítima apenas pela oferta: ela precisa parecer
legítima. O instrumento central dessa legitimação é o **conjunto de avaliações plantadas** —
textos entusiasmados, genéricos e repetitivos que simulam a satisfação de compradores que
nunca existiram. Reconhecer esse padrão textual é, portanto, parte de reconhecer a fraude,
e é essa capacidade que a fonte pretende ensinar ao classificador.

## Da saída bruta ao dataset final — a curadoria manual

O `reviews_traduzidos.xlsx` **não entra diretamente** no dataset de treinamento. Entre a
saída deste script e o dataset final há uma etapa de curadoria:

```
reviews_traduzidos.xlsx  (150 avaliações traduzidas, reais e geradas)
        │
        ▼
 curadoria manual: seleção das avaliações cujo padrão textual é
 representativo de legitimação fraudulenta, descarte de traduções
 degradadas e das avaliações legítimas
        │
        ▼
 subconjunto  →  compõe parte das 75 instâncias da categoria no BrScamsFacebook
```

Essa etapa é também onde a limitação registrada em *Preocupações com segurança*, item 3, é
mitigada: avaliações geradas artificialmente que não se assemelham a fraude real foram
descartadas.

## Reivindicações #1 e #2 — Procedência dos dados do BrScamsFacebook

As reivindicações #1 (F1-macro do BERTimbau) e #2 (comparação com o baseline) só são
interpretáveis se a origem dos dados de treinamento for auditável. Esta subseção descreve
como o revisor verifica a contribuição deste repositório para essa cadeia de procedência.

**Procedimento (≈ 5 minutos, sem custo):**

1. Execute o **Teste A** para confirmar o conteúdo da saída versionada
2. Percorra os pares `text_` / `text_traduzido` e verifique que cada tradução corresponde
   ao original em inglês
3. Opcionalmente, execute o **Teste B** para observar o não determinismo da tradução

**Resultado esperado:** correspondência semântica linha a linha entre as duas colunas. A
preservação da coluna original é o que torna esta verificação possível **sem** acesso ao
dataset do Kaggle.

**Recursos esperados:** leitor de planilhas. Tempo: ≈ 5 minutos. Custo: zero.

**Sobre o determinismo.** A tradução automática **não é determinística**: o serviço do
Google pode retornar formulações diferentes para o mesmo texto ao longo do tempo — o Teste
B demonstra isso empiricamente. Reexecutar `tradutor.py` produzirá um arquivo semelhante,
mas não idêntico. A fonte de verdade para a reprodução do dataset é o
**`reviews_traduzidos.xlsx` versionado**. O que é determinístico e verificável é a
**correspondência linha a linha** entre a coluna original e a traduzida.

---

# LICENSE

Este artefato é distribuído sob a **Licença MIT**. O texto completo está no arquivo
[LICENSE](LICENSE) deste repositório.

```
MIT License

Copyright (c) 2026 Bruna Norões

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: [...]
```

A licença MIT cobre o **código do tradutor** e a organização dos dados derivados. O **Fake
Reviews Dataset** original permanece sujeito à licença de seus autores e **não é
redistribuído** neste repositório; apenas a amostra traduzida é disponibilizada, para fins
de pesquisa acadêmica, nas condições da seção *Preocupações com segurança*.
