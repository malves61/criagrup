import pandas as pd
from time import sleep
import pyautogui
from pathlib import Path

empresas_file = Path('/home/marcelo/Meus Programas/criagrup/Notificaveis.csv')

empresas_df = pd.read_csv(empresas_file, sep=';', dtype={'CPF_CNPJ Entidade Representada':str})
cnpjs_df = empresas_df[['Nome Entidade Representada','Notificar (Resumo)','CPF_CNPJ Entidade Representada']].copy()
cnpjs_df.drop(cnpjs_df[cnpjs_df['Notificar (Resumo)']==False].index,inplace=True)
cnpjs_df.drop_duplicates(subset=['CPF_CNPJ Entidade Representada'], keep='first', inplace=True)
cnpjs_df.reset_index(drop=True)
cnpjs_df['CNPJ']=(cnpjs_df['CPF_CNPJ Entidade Representada'].str[0:-12]+'.'+ \
                 cnpjs_df['CPF_CNPJ Entidade Representada'].str[-12:-9]+'.'+ \
                 cnpjs_df['CPF_CNPJ Entidade Representada'].str[-9:-6]+'/'+ \
                 cnpjs_df['CPF_CNPJ Entidade Representada'].str[-6:-2]+'-'+ \
                 cnpjs_df['CPF_CNPJ Entidade Representada'].str[-2:]).str.zfill(18)

sleep(5)

field=pyautogui.position()
i=0
for index, entity in cnpjs_df.iterrows():
    if i>=92:
        print(f"Entrada {i}, - {entity['Nome Entidade Representada']}")
        pyautogui.click(field.x,field.y)
        pyautogui.write(entity['CNPJ'], interval=0.05)
        sleep(10)
    i=i+1