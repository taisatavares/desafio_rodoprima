# Desafio RPA + ETL + BigQuery + Looker Studio

Este repositório contém a solução completa para o desafio de dados proposto pela empresa Rodoprima Transportes.

## 🚀 Etapas do projeto

### 1. RPA com Playwright (automatização do download)
O script `download_rpa.py` automatiza o download da planilha base do desafio usando a biblioteca Playwright. O código foi desenvolvido no PyCharm.

### 2. ETL com Python no Google Colab
No notebook `Teste_Rodoprima.ipynb`, foram realizadas as seguintes etapas:
- Padronização dos nomes de colunas
- Remoção de registros cancelados e duplicados
- Tratamento de valores ausentes
- Cálculo do EBITDA por vendedor
- Exportação final dos dados tratados

### 3. Envio para o BigQuery
Após o tratamento, os dados foram exportados para o Google BigQuery via `pandas_gbq`. As tabelas `cte`, `frete` e `ebitda` foram criadas no dataset `desafio`.

### 4. Dashboard no Looker Studio
O dashboard foi criado a partir das tabelas no BigQuery e está disponível neste link:

🔗 [Acesse o dashboard aqui](https://lookerstudio.google.com/s/mqYj6I77lrc)

---

## 🛠 Tecnologias utilizadas

- Python (Pandas, Playwright)
- Google Colab
- Google BigQuery
- Looker Studio

