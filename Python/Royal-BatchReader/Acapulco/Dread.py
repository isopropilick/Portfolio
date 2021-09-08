import pandas as pd
import json


def run():
    f = open('Out/availabledata.json',)
    data = json.load(f)
    f.close()
    print("\n\033[92mData files processed:")
    for i in data['files']:
        print("\033[93m"+str(i['file']))
        xlsx_file = ("Data/" + i['file'])
        dfs = pd.read_excel(xlsx_file, sheet_name='recibos204', header=1)
        dfs.dropna(subset=['Personnel Name', 'Sales Volume USD', 'Comision Total a Pagar'], inplace=True, how='all')
        filename = "Out/"+str(i['data'])
        dfs = dfs[~dfs['Personnel Name'].str.contains('Total')]
        dfs.to_json(path_or_buf=filename+".json", orient='records',force_ascii=False,indent=4)
        dfs.to_csv(path_or_buf=filename+".csv")
