# Inteligência Artificial — UniFAP 2026.2

**Aluno:** Lemuel Lopes Sousa
**Curso:** Sistemas de Informação — Centro Universitário Paraíso (UniFAP)
**Professor:** Alexsandro Oliveira Alexandrino

Repositório único com as atividades, tutoriais, testes de conhecimento e TDEs da disciplina.

## Índice

| Pasta | Conteúdo |
|---|---|
| [`01-tutoriais/`](01-tutoriais) | Tutoriais feitos em sala |
| [`02-teste-de-conhecimento-1/`](02-teste-de-conhecimento-1) | Teste de Nivelamento — Python puro e estatística básica |
| [`03-tdes/`](03-tdes) | TDEs em grupo — Previsão de volatilidade de ações (Optiver) |

### 01 — Tutoriais

| Notebook | Assunto |
|---|---|
| [`Cepagri_Pandas.ipynb`](01-tutoriais/Cepagri_Pandas.ipynb) | Leitura, escrita e tratamento de dados com Pandas (Titanic e dados meteorológicos do Cepagri) |
| [`House_Pricing_Regressao.ipynb`](01-tutoriais/House_Pricing_Regressao.ipynb) | Regressão: `SGDRegressor`, `LinearRegression`, regressão polinomial e One-Hot Encoding, avaliados com MAE e MSE |

Os notebooks leem os dados do Google Drive (`/content/drive/MyDrive/2025.2/IA/Tutoriais/`); para executar, ajuste o caminho dos arquivos `.csv`.

### 02 — Teste de Conhecimento 1 (Nivelamento)

- [`Teste_de_Nivelamento.pdf`](02-teste-de-conhecimento-1/Teste_de_Nivelamento.pdf) — enunciado
- [`resolucao_nivelamento_python_puro.py`](02-teste-de-conhecimento-1/resolucao_nivelamento_python_puro.py) — resolução das questões 1 a 6 (sem Pandas/NumPy) e respostas das teóricas

```bash
python 02-teste-de-conhecimento-1/resolucao_nivelamento_python_puro.py
```

| Questão | Tema | Resposta |
|---|---|---|
| 1 | Inner join manual + presença ≥ 75 | `questao_1_manipular_dados` |
| 2 | Média e desvio padrão amostral | `questao_2_estatistica` |
| 3 | Divisão treino/teste com slicing | `questao_3_divisao_manual` |
| 4 | Substituição de `None` pela média | `questao_4_dados_nulos` |
| 5 | Erro Quadrático Médio (MSE) | `questao_5_calculo_erro` |
| 6 | Média de horas por turno | `questao_6_agrupamento` |
| 7 | List comprehension | **B** — `[1, 9]` |
| 8 | Junção de tabelas | **B** — Inner Join |

### 03 — TDEs (em grupo)

Projeto: **Optiver Realized Volatility Prediction** (Kaggle) — prever a volatilidade realizada de ações.
Repositório oficial do grupo: <https://github.com/JoaoGabrielOSdev/Tde-do-ia>

| TDE | Arquivos | Etapa |
|---|---|---|
| TDE 01 | [`notebook`](03-tdes/tde01-analise-exploratoria/TDE01_Analise_Volatilidade_Acoes_Optiver_corrigido.ipynb) · [`apresentação`](03-tdes/tde01-analise-exploratoria/TDE01_Apresentacao.pdf) | Análise exploratória dos dados |
| TDE 03 | [`notebook`](03-tdes/tde03-baseline/TDE03_Baseline_Volatilidade_Acoes_Optiver.ipynb) | Baseline: Regressão Linear, Árvore de Decisão e Random Forest sem otimização, avaliados com MAE, MSE, RMSE e R² |

Os notebooks dos TDEs baixam os dados do Kaggle e devem ser executados no Google Colab (instruções dentro de cada notebook).
