import pandas as pd
from pandas_gbq import to_gbq

xls = pd.ExcelFile('/content/planilha.xlsx')

df_cte = pd.read_excel(xls, sheet_name='CTE')
df_frete = pd.read_excel(xls, sheet_name='CONTRATOS DE FRETE')


project_id = 'projeto-rodoprima'

to_gbq(df_cte, 'desafio.cte', project_id=project_id, if_exists='replace')
to_gbq(df_frete, 'desafio.frete', project_id=project_id, if_exists='replace')